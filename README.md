
# Restrict access to parts of Django application to IP addresses in your ZenVPN account

Use this module to restrict access to parts of your Django application to members of your 
teams in [ZenVPN](https://zenvpn.net/) using IP address check. 

## Security warning
This module uses HTTP headers to deduce the user's IP address. Misconfiguring it may make 
your application vulnerable to IP address spoofing. Make sure to set `ZENVPN_PROTECT_PROXY_COUNT` in
your `settings.py` to the actual number of proxies in front of your app. 

**django-zenvpn-protect** relies on [django-ipware](https://github.com/un33k/django-ipware) for IP address
deduction. Please refer to the **django-ipware** documentation for further details.

## Installation

    pip install django-zenvpn-protect 

In your project's **settings.py** add the following settings:

    ZENVPN_PROTECT_PROXY_COUNT = 0 # Number of reverse proxies in front of your application. Mandatory.
    ZENVPN_ACCESS_TOKEN = '' # API acess key from your ZenVPN account. Mandatory.
    ZENVPN_ALLOWED_IPS_CACHE_DURATION = 30 # Number of seconds to cache allowed IPs returned by ZenVPN API. Optional. 

## Usage

To restrict a view or group or views, simply wrap the respective *path* entry in your project's urlconf 
into a **protect** function like this:

    from zenvpn.protect import protect
    ...
    urlpatterns = [
        ...
        protect(path('admin/', admin.site.urls),)
        protect(re_path('^some/path/$', MyView.as_view())),

