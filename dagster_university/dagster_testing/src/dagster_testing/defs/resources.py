import dagster as dg
from dagster_snowflake import SnowflakeResource


class StatePopulation(dg.ConfigurableResource):
    def get_cities(self, state: str) -> list[dict]:
        return [
            {
                "City": "Milwaukee",
                "Population": 577222,
            },
            {
                "City": "Madison",
                "Population": 269840,
            },
        ]


@dg.definitions
def resources():
    """Returns Dagster resource definitions.

    Returns:
        dagster.Definitions: The resource definitions for Dagster.
    """
    return dg.Definitions(
        resources={
            "database": SnowflakeResource,
        },
    )

