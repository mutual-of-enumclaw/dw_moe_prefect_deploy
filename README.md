##Description: Repository for Mutual of Enumclaw's Data Warehouse Prefect Workflows. This contains resusable workflows to be used within other GitHub actions workflows in the .github\workflows folder. This repository must be public in order to use the resusable workflows in other repositories.

##Example Usage of dw-prefect-deploy.yml:

name: Deploy Dev

on:
  push:  
    branches:
      - dev

jobs:
  call-dev-deploy:
    uses: mutual-of-enumclaw/dw_moe_prefect_deploy/.github/workflows/prefect-deploy.yml@main
    with:
      region: 'us-west-2'
      environment_name: 'tst'
    secrets:
      AWS_ACCESS_KEY_ID: ${{ secrets.GENDEV_DEPLOY_USER_AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.GENDEV_DEPLOY_USER_AWS_SECRET_ACCESS_KEY }}
      MS_TEAMS_WEBHOOK_URI:  ${{ secrets.MS_TEAMS_NUCLEUS_DEPLOY_WEBHOOK_URI }}