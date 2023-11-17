from prefect import flow
from prefect_fivetran import FivetranCredentials
from prefect_fivetran.connectors import (
    trigger_fivetran_connector_sync_and_wait_for_completion,
)

from prefect_dbt.cloud import DbtCloudCredentials
from prefect_dbt.cloud.jobs import trigger_dbt_cloud_job_run_and_wait_for_completion
from prefect_dbt.cloud.models import TriggerJobRunOptions


# -------------------- Begin: Tasks and Flows for this pipeline -------------------------
@flow(
    flow_run_name="Load and model Hubspot data",
    description="This flow loads Hubspot data via Fivetran and models it using Dbt Cloud",
    log_prints=True,
)
def fivetran_hubspot_load():
    print("Begin Fivetran Hubspot Load")

    # Execute Fivetran Load/Sync.
    trigger_fivetran_connector_sync_and_wait_for_completion(
        fivetran_credentials=FivetranCredentials.load("fivetran-creds"),
        connector_id="pamperer_collaboration",
        schedule_type="auto",
        poll_status_every_n_seconds=30,
    )
    print("Finished Fivetran Hubspot Load")

    print("Begin Dbt Job Run")
    # Execute Dbt Cloud Job for Hubspot model
    trigger_dbt_cloud_job_run_and_wait_for_completion(
        dbt_cloud_credentials=DbtCloudCredentials.load("dbt-cloud-creds"),
        poll_frequency_seconds=15,
        job_id=72790,
        trigger_job_run_options=TriggerJobRunOptions(
            steps_override=["dbt run --select +master.hubspot_email_event+"]
        ),
    )
    print("Finished Dbt Job Run!")


# --------------------- End: Tasks and Flows for this pipeline --------------------------


# ----------------------------- Begin: Main Entrypoint ----------------------------------
if __name__ == "__main__":
    hubspot_load = fivetran_hubspot_load()
# ----------------------------- End: Main Entrypoint ----------------------------------
