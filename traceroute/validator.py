from traceroute import config
import requests


def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


def validate_ip(ip):
    bytes = ip.split(".")
    if len(bytes) != 4:
        return False
    else:
        for byte in bytes:
            if is_number(byte) is False:
                return False

        return True


def validate_url(url):
    if config.PRE_URL not in url:
        url = config.PRE_URL + url
    try:
        request = requests.get(url)
        if request.status_code == config.STATUS_OK:
            return True
        else:
            return False
    except Exception:
        return False
