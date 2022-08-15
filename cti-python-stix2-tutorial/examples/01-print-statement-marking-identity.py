from stix2 import Identity
from stix2 import MarkingDefinition, StatementMarking

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

## Print all the objects

print(SCIdentitySDO.serialize(pretty=True))
print(SCMarkingDefinitionStatement.serialize(pretty=True))