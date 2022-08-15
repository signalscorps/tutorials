from stix2 import Relationship
from stix2 import TLP_AMBER
from stix2 import FileSystemStore

## Get required Objects previously saved to filesystem source
### https://stix2.readthedocs.io/en/latest/guide/filesystem.html#FileSystemSource

fs = FileSystemStore("tmp/stix2_store")
SCIdentitySDO = fs.get("identity--c73bd6f8-6cd0-4b39-a5ec-81c4461f97fb")
Indicator0SDOFileHash = fs.get("indicator--c7162dea-dbbb-42cf-be6d-fc82daeea352")
Malware0SDOWithGranularMarkings = fs.get("malware--31d2559c-149d-44c1-9fe9-dd8c147031c3")

## Link Indicator SDO and Malware SDO using SRO
### https://stix2.readthedocs.io/en/latest/api/stix2.v21.html#stix2.v21.Relationship

Indicator0ToMalware0SRO = Relationship(
                        relationship_type='indicates',
                        source_ref=Indicator0SDOFileHash.id,
                        target_ref=Malware0SDOWithGranularMarkings.id,
                        created_by_ref=SCIdentitySDO,
                        object_marking_refs=TLP_AMBER
                    )


## Write the to filesystem

fs.add([Indicator0ToMalware0SRO])

## relationship--8c26909d-88fc-45c3-bb82-ebd766c23836 created in FS

## Print the object

print(Indicator0ToMalware0SRO.serialize(pretty=True))