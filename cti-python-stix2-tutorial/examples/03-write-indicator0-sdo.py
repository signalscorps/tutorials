from stix2 import Identity, Indicator
from stix2 import MarkingDefinition, StatementMarking, TLP_GREEN
from stix2 import FileSystemStore

## create FileSystemStore
### https://stix2.readthedocs.io/en/latest/guide/filesystem.html

fs = FileSystemStore("tmp/stix2_store")

## Create Identity SDO
### https://stix2.readthedocs.io/en/latest/api/stix2.v21.html#stix2.v21.ObservedData

SCIdentitySDO = Identity(
                        name="Signal Corps Tutorial",
                        description="Used for tutorial content")

## Create Statement Marking
### https://stix2.readthedocs.io/en/latest/api/stix2.v21.html#stix2.v21.MarkingDefinition

SCMarkingDefinitionStatement = MarkingDefinition(
    definition_type="statement",
    definition = StatementMarking(
                statement="Content from the Signals Corps tutorial"
            )
    )

## Create Indicator SDO
### https://stix2.readthedocs.io/en/latest/api/stix2.v21.html#stix2.v21.Indicator

Indicator0SDOFileHash = Indicator(
                        name="My first SDO",
                        description="Getting started with cti-python-stix2",
                        type='indicator',
                        pattern="[file:hashes.md5 = 'd41d8cd98f00b204e9800998ecf8427e']",
                        pattern_type="stix",
                        created_by_ref=SCIdentitySDO,
                        object_marking_refs=[TLP_GREEN,SCMarkingDefinitionStatement]
                    )

## Write the to filesystem

fs.add([SCIdentitySDO,SCMarkingDefinitionStatement,Indicator0SDOFileHash])

## identity--c73bd6f8-6cd0-4b39-a5ec-81c4461f97fb created in FS
## indicator--c7162dea-dbbb-42cf-be6d-fc82daeea352 created in FS
## definition marking-definition--e55ae95e-54f0-4b00-96a2-678f744c3f8a created in FS

## Print all the objects

print(SCIdentitySDO.serialize(pretty=True))
print(SCMarkingDefinitionStatement.serialize(pretty=True))
print(Indicator0SDOFileHash.serialize(pretty=True))