## Description: Repository for Mutual of Enumclaw's Data Warehouse Prefect Workflows. This contains resusable workflows to be used within other GitHub actions workflows in the .github\workflows folder. This repository must be public in order to use the resusable workflows in other repositories.

## Example Usage of dw-prefect-deploy.yml:

```
name: Deploy Dev

on:
  push:  
    branches:
      - dev

jobs:
  call-dev-deploy:
    uses: mutual-of-enumclaw/dw_moe_prefect_deploy/.github/workflows/prefect-deploy.yml@main
    with:
      prefect-workspace: upsilon36-lesath/test-workspace
    secrets:
      prefect-api-key: ${{ secrets.PREFECT_API_KEY }}
      prefect-api-url: ${{ secrets.PREFECT_API_URL }}
```