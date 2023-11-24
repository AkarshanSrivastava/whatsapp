import http.client
import ssl

conn = http.client.HTTPSConnection("api.ultramsg.com",context = ssl._create_unverified_context())

payload = "token=k29irlpc49wq5r4q&to=+917007958615&body=Welcome to Dimension Zero, A platform that provide everythingf related to IML"
payload = payload.encode('utf8').decode('iso-8859-1')

headers = { 'content-type': "application/x-www-form-urlencoded" }

conn.request("POST", "/instance69299/messages/chat", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))