from stix2 import Indicator
from stix2 import FileSystemStore

## Get required Objects previously saved to filesystem source
### https://stix2.readthedocs.io/en/latest/guide/filesystem.html#FileSystemSource

fs = FileSystemStore("tmp/stix2_store")

Indicator0SDOFileHash = fs.get("indicator--c7162dea-dbbb-42cf-be6d-fc82daeea352")

## Update Indicator0SDOFileHash with new Property
### https://stix2.readthedocs.io/en/latest/guide/versioning.html#Versioning

Update0Indicator0SDOFileHash = Indicator0SDOFileHash.new_version(
								indicator_types = ["anomalous-activity"]
                            )

## Write the to filesystem

fs.add([Update0Indicator0SDOFileHash])

## indicator--c7162dea-dbbb-42cf-be6d-fc82daeea352 updated in FS

## Print the objects

print(Update0Indicator0SDOFileHash.serialize(pretty=True))