from taxii2client.v21 import as_pages
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

page_no = 1
for envelope in as_pages(collection3.get_objects, per_request=1):
    print()
    print('Page # {}'.format(page_no))
    print()
    print(envelope)
    page_no += 1