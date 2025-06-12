import requests
from stem import Signal
from stem.control import Controller
import time

TOR_SOCKS_PORT = 9050  # ou 9150 selon ta config
TOR_CONTROL_PORT = 9051
TEST_URL = "https://httpbin.org/ip"

def get_my_ip():
    proxies = {
        'http': f'socks5h://127.0.0.1:{TOR_SOCKS_PORT}',
        'https': f'socks5h://127.0.0.1:{TOR_SOCKS_PORT}',
    }
    r = requests.get(TEST_URL, proxies=proxies, timeout=10)
    return r.json()["origin"]

def new_tor_identity():
    with Controller.from_port(port=TOR_CONTROL_PORT) as controller:
        controller.authenticate()  # Si tu as mis un mot de passe, ajoute-le ici
        controller.signal(Signal.NEWNYM)

if __name__ == "__main__":
    print("IP actuelle via Tor :", get_my_ip())
    print("Changement d'identité Tor...")
    new_tor_identity()
    print("Attente création d'un nouveau circuit Tor...")
    time.sleep(10)  # Attends 8-10 secondes, c'est important !
    print("Nouvelle IP via Tor :", get_my_ip())
