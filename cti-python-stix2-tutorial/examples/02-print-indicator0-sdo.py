from stix2 import Identity, Indicator
from stix2 import MarkingDefinition, StatementMarking, TLP_GREEN

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

## Print all the objects

print(SCIdentitySDO.serialize(pretty=True))
print(SCMarkingDefinitionStatement.serialize(pretty=True))
print(Indicator0SDOFileHash.serialize(pretty=True))