import requests

r = requests.post("https://maker.ifttt.com/trigger/Movimiento/with/key/d58LS-mFzGlnl9ccgirNHa", data={"value1": "sala"})
print(r.status_code, r.reason)

