from stix2 import Bundle
from stix2 import FileSystemStore
from stix2.base import STIXJSONEncoder
import json

## Get all Objects previously saved to filesystem source
### https://stix2.readthedocs.io/en/latest/guide/filesystem.html#FileSystemSource

fs = FileSystemStore("tmp/stix2_store")

SCIdentitySDO = fs.get("identity--c73bd6f8-6cd0-4b39-a5ec-81c4461f97fb")
SCMarkingDefinitionStatement = fs.get("marking-definition--e55ae95e-54f0-4b00-96a2-678f744c3f8a")
Indicator0SDOFileHash = fs.get("indicator--c7162dea-dbbb-42cf-be6d-fc82daeea352")
Malware0SDOWithGranularMarkings = fs.get("malware--31d2559c-149d-44c1-9fe9-dd8c147031c3")
Indicator1SDOFileParent = fs.get("indicator--2b890609-c746-4bad-b3f1-2398e1e8557e")
Indicator0ToMalware0SRO = fs.get("relationship--8c26909d-88fc-45c3-bb82-ebd766c23836")
MACAddr0SCO = fs.get("mac-addr--875ad625-177b-5c2a-9101-d44b0ad55938")
MACAddr1SCO = fs.get("mac-addr--f72d7d00-86bd-5cd2-8c86-52f7a83bef62")
IPv40SCO = fs.get("ipv4-addr--dc63603e-e634-5357-b239-d4b562bc5445")
ObservedDataSROofIPv40SCO = fs.get("observed-data--220aadc8-b1d0-42b6-8695-e07fde007588")
Custom0SDO = fs.get("x-dummy-object--e996146a-7713-4dbb-bde6-c1a7c51fae74")
SightingSRO = fs.get("sighting--c62dde8c-d7bb-4be1-9075-5030a77bff7f")

## Create the STIX bundle (making sure to add allow_custom for custom Object/Properties used)
### https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.bundle.html#stix2.v21.bundle.Bundle

BundleofAllObjects = Bundle(Indicator0SDOFileHash,SCIdentitySDO,SCMarkingDefinitionStatement,
                        Malware0SDOWithGranularMarkings,Indicator1SDOFileParent,
                        Indicator0ToMalware0SRO,MACAddr0SCO,MACAddr1SCO,IPv40SCO,ObservedDataSROofIPv40SCO,
                        Custom0SDO,SightingSRO,allow_custom=True)

## Print the bundle

print(BundleofAllObjects.serialize(pretty=True))

## Save a bundle .json (cannot write to FS)

with open(BundleofAllObjects.id+'.json', 'w') as f:
    f.write(json.dumps(BundleofAllObjects,cls=STIXJSONEncoder))