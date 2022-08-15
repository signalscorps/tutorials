from stix2 import CustomObject, properties
from stix2 import FileSystemStore

## Get required Objects previously saved to filesystem source
### https://stix2.readthedocs.io/en/latest/guide/filesystem.html#FileSystemSource

fs = FileSystemStore("tmp/stix2_store")
SCIdentitySDO = fs.get("identity--c73bd6f8-6cd0-4b39-a5ec-81c4461f97fb")

## Define the properties for the Custom SDO
### https://stix2.readthedocs.io/en/latest/guide/custom.html#Custom-STIX-Object-Types

@CustomObject('x-dummy-object', [
    ('property0', properties.StringProperty(required=True)),
    ('property1', properties.StringProperty()),
])
class Dummy(object):
    def __init__(self, property1=None, **kwargs):
        if property1 and property1 not in ['value0', 'value1', 'value2']:
            raise ValueError("'%s' is not a recognized value for property." % property1)

## Create the custom SDO

Custom0SDO = Dummy(
                property0="something",
                property1="value0",
                created_by_ref=SCIdentitySDO
            )

## Write the to filesystem

fs.add([Custom0SDO])

## x-dummy-object--e996146a-7713-4dbb-bde6-c1a7c51fae74 created in FS

## Print the objects

print(Custom0SDO.serialize(pretty=True))