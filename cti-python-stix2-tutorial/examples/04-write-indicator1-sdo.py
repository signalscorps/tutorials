from stix2 import Indicator
from stix2 import ObjectPath, EqualityComparisonExpression, ObservationExpression
from stix2 import FileSystemStore

## Get required Objects previously saved to filesystem source
### https://stix2.readthedocs.io/en/latest/guide/filesystem.html#FileSystemSource

fs = FileSystemStore("tmp/stix2_store")
SCIdentitySDO = fs.get("identity--c73bd6f8-6cd0-4b39-a5ec-81c4461f97fb")

## Create pattern
### https://stix2.readthedocs.io/en/latest/api/stix2.patterns.html?stix2.patterns.ObservationExpression

setSCOandContributingProperty = ObjectPath("file", ["parent_directory_ref","path"])
fileParentDirectoryPattern = ObservationExpression(EqualityComparisonExpression(setSCOandContributingProperty, "C:\\Windows\\System32"))

## Create Indicator SDO
### https://stix2.readthedocs.io/en/latest/api/stix2.v21.html#stix2.v21.Indicator

## Create Indicator SDO with pattern fileParentDirectoryPattern

Indicator1SDOFileParent = Indicator(
                        name="My Indicator SDO with created pattern",
                        description="Pattern created using stix2",
                        type='indicator',
                        pattern=fileParentDirectoryPattern,
                        pattern_type="stix",
                        created_by_ref=SCIdentitySDO
                        )

## Write the to filesystem

fs.add([Indicator1SDOFileParent])

## indicator--2b890609-c746-4bad-b3f1-2398e1e8557e created in FS

## Print the object

print(Indicator1SDOFileParent.serialize(pretty=True))