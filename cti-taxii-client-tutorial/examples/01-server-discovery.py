from taxii2client.v21 import Server

server = Server('http://localhost:5000/taxii2/', user='admin', password='Password0')

print('server.title : ', server.title)
print('server.description : ', server.description)
print('server.contact : ', server.contact)
print('server.default.url :', server.default.url)
print('server.custom_properties :', server.custom_properties)

roots = []
for api in server.api_roots:
    roots.append(api.url)

print('server.api_roots : ',roots)