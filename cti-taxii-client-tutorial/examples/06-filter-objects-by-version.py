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

def filter(object_id, object_version, collection=collection3):
    x =  collection.get_object(obj_id=object_id, modified=object_version)
    return x

get_version = filter('indicator--cd981c25-8042-4166-8945-51178443bdac','2014-05-08T09:00:00.000Z' )

print(get_version)