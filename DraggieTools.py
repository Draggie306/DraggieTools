from requests import get
build = 0
version = "0.0.1"

def check_for_update():
    x = get("")