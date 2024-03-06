import requests

from django.conf import settings
from django.http import HttpResponseForbidden
from django.core.cache import cache

from ipware import get_client_ip

API_BASE_URL = 'https://zenvpn.net/api/v1'


def get_allowed_ips(hostname):
    allowed_ips = cache.get(f'allowed_ips_{hostname}')
    if allowed_ips is None:
        r = requests.get(f'{API_BASE_URL}/get_ips', params={'domain_name': hostname,
                                                            'access_token': settings.ZENVPN_ACCESS_TOKEN})
        if r.status_code == 200:
            allowed_ips = r.json()['ipAddresses']
            cache.set(f'allowed_ips_{hostname}', allowed_ips,
                      timeout=getattr(settings, 'ZENVPN_ALLOWED_IPS_CACHE_DURATION', 30))
        else:
            allowed_ips = []
    else:
        assert isinstance(allowed_ips, list)
    return allowed_ips


def wrap_view(view):
    def wrapped(request, *args, **kwargs):
        client_ip, _ = get_client_ip(request, proxy_count=settings.ZENVPN_PROTECT_PROXY_COUNT)
        allowed_ips = get_allowed_ips(request.META['HTTP_HOST'].split(':')[0])
        if client_ip not in allowed_ips:
            return HttpResponseForbidden()
        return view(request, *args, **kwargs)
    return wrapped


def wrap_resolve(resolve):
    def patched_resolve(*args, **kwargs):
        match = resolve(*args, **kwargs)
        if match is not None:
            match.func = wrap_view(match.func)
        return match
    return patched_resolve


def protect(path):
    path.resolve = wrap_resolve(path.resolve)
    return path