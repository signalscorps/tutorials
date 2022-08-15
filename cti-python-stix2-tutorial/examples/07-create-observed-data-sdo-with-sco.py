from stix2 import ObservedData
from stix2 import MACAddress, IPv4Address
from stix2 import FileSystemStore

## Get required Objects previously saved to filesystem source
### https://stix2.readthedocs.io/en/latest/guide/filesystem.html#FileSystemSource

fs = FileSystemStore("tmp/stix2_store")
SCIdentitySDO = fs.get("identity--c73bd6f8-6cd0-4b39-a5ec-81c4461f97fb")

## Set MAC Address SCOs
### https://stix2.readthedocs.io/en/latest/api/stix2.v21.html#stix2.v21.MACAddress

MACAddr0SCO = MACAddress(
                value="a1:b2:c3:d4:e5:f6"
            )
MACAddr1SCO = MACAddress(
                value="a7:b8:c9:d0:e1:f2"
            )

## Create IPv4 SCO referencing MAC Address values
### https://stix2.readthedocs.io/en/latest/api/stix2.v21.html#stix2.v21.IPv4Address

IPv40SCO = IPv4Address(
            value="177.60.40.7",
            resolves_to_refs=[MACAddr0SCO.id, MACAddr1SCO.id]
        )

## Create Observed Data SRO
### https://stix2.readthedocs.io/en/latest/api/stix2.v21.html#stix2.v21.ObservedData

ObservedDataSROofIPv40SCO = ObservedData(
                        object_refs=IPv40SCO,
                        first_observed="2021-06-25T12:01:23.868289Z",
                        last_observed="2021-06-25T12:01:23.868289Z",
                        number_observed="1",
                        created_by_ref=SCIdentitySDO
                        )

## Write the to filesystem

fs.add([MACAddr0SCO,MACAddr1SCO,IPv40SCO,ObservedDataSROofIPv40SCO])

## observed-data--220aadc8-b1d0-42b6-8695-e07fde007588 created in FS
## mac-addr--875ad625-177b-5c2a-9101-d44b0ad55938 created in FS
## mac-addr--f72d7d00-86bd-5cd2-8c86-52f7a83bef62 created in FS
## ipv4-addr--dc63603e-e634-5357-b239-d4b562bc5445 created in FS

## Print all the objects

print(MACAddr0SCO.serialize(pretty=True))
print(MACAddr1SCO.serialize(pretty=True))
print(IPv40SCO.serialize(pretty=True))
print(ObservedDataSROofIPv40SCO.serialize(pretty=True))