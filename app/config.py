from os import environ

HTTP_PROVIDER_URL = environ.get("HTTP_PROVIDER_URL")
WS_PROVIDER_URL = environ.get("WS_PROVIDER_URL")

ALLOWED_ORIGIN_SUFFIXES = ('localhost', 'http://trade.oberdex.org/', 'trade.oberdex.org', 'backendoberdex.herokuapp.com')
ED_CONTRACT_ADDR = '0xb5adb233f28c86cef693451b67e1f2d41da97d21'
with open('bitox.abi.json') as f:
    import json
    ED_CONTRACT_ABI = json.load(f)
ED_WS_SERVERS = [
  "ws:https://backendoberdex.herokuapp.com//:8080/socket.io/?EIO=3&transport=websocket",
]

POSTGRES_HOST = "ec2-54-217-235-137.eu-west-1.compute.amazonaws.com"
POSTGRES_DB = environ.get("d8hb2mdogb873c")
POSTGRES_USER = environ.get("dkjqpeivffgwiz")
POSTGRES_PASSWORD = environ.get("2b2f4e065ada893d5f6fffdc0c1dbc20249a146159dbe51a491161ea191cd65b")

FRONTEND_CONFIG_FILE="trade.oberdex.org/config/main.json"
