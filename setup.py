from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
    name="django-zenvpn-protect",  # Required

    version="0.0.1",

    description="Limits access to specific URLs to users connected via specific ZenVPN account",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zenvpnnet/django-zenvpn-protect",
    author="ZenVPN",
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Security",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["zenvpn"],
    python_requires=">=3.7, <4",
    install_requires=["Django>=4.2.0", "requests", "django-ipware"],
    project_urls={  # Optional
        "Source": "https://github.com/zenvpnnet/django-zenvpn-protect/",
        "ZenVPN Website": "https://zenvpn.net/"
    },
)