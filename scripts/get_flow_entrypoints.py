# Script to get the entrypoints of all flows
# for use in the .github/workflows/deploy-flows.yml file.

# Usage: python scripts/get_flow_entrypoints.py
# prints comma-separated entrypoints to stdout

import pathlib

from prefect.deployments.base import _search_for_flow_functions


async def main():
    # Establish base path to search for flows
    base_dir = pathlib.Path(__file__).resolve().parent.parent

    # Find and collect flows within files in the root of the project
    entrypoints = [
        f"{flow['filepath'].replace(str(base_dir) + '/', '')}:{flow['function_name']}" # noqa: E501
        
        for flow in await _search_for_flow_functions(directory=str(base_dir))
        if str(base_dir) in flow['filepath']
    ]

    # Print comma delimited list of flows
    print(','.join(entrypoints))


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())