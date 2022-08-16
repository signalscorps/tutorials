from taxii2client.v21 import ApiRoot

default = ApiRoot(url='http://localhost:5000/trustgroup1', user='admin', password='Password0')

collection_no = 1

for collections in default.collections:

    print()
    print('Collection {}'.format(collection_no))
    print()
    print("collection.title: ", collections.title)
    print("collection.description: ", collections.description)
    print("collection.id: ", collections.id)
    print('collection.custom_properties: ',collections.custom_properties)
    print('collection.can_read: ',collections.can_read)
    print('collection.can_write: ',collections.can_write)
    print('collection.media_types: ',collections.media_types)
    print()

    collection_no += 1