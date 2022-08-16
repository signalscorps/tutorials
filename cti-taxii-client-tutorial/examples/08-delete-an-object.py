from taxii2client.v21 import Server 

server = Server('http://localhost:5000/taxii2/', user='admin', password='Password0')

col = {}

for api_roots in server.api_roots:
    api_root = api_roots.collections
    try:
        for collections in api_roots.collections:
            col[collections.id] = collections 

    except:
        print('')
        continue

collection3 =  col['91a7b528-80eb-42ed-a74d-c6fbd5a26116']

collection3.delete_object(obj_id='indicator--9ef5baeb-ad55-4c2c-aa89-ea5515dacf62')
print('Successfully deleted')