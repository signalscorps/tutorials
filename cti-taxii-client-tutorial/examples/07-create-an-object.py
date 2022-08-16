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

x = collection3.add_objects("{\"objects\":[{\"type\":\"indicator\",\"spec_version\":\"2.1\",\"id\":\"indicator--9ef5baeb-ad55-4c2c-aa89-ea5515dacf62\",\"created\":\"2022-01-01T01:00:00.000Z\",\"modified\":\"2022-01-01T01:00:00.000Z\",\"name\":\"Malicious site hosting downloader\",\"description\":\"This organized threat actor group operates to create profit from all types of crime.\",\"indicator_types\":[\"malicious-activity\"],\"pattern\":\"[url:value = 'http:\/\/x4z9arb.cn\/4712\/']\",\"pattern_type\":\"stix\",\"valid_from\":\"2022-01-01T01:00:00.000Z\"}]}")
print('status: ', x.status)
print('id: ', x.id)
print('failure_count: ', x.failure_count)
print('pending_count: ', x.pending_count)
print('success_count: ', x.success_count)