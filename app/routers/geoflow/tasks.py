"""FastGeoflow - Geoflow - Tasks"""

import datetime
from pygeoflow import workflow

import config
import app.routers.geoflow.models as models

geoflow_processes = {}

def run_geoflow_workflow(
    process_id: str,
    geoflow_workflow: models.WorkflowModel
):
    start = datetime.datetime.now()

    try:        

        workflow.Workflow(
            db_host=config.DB_HOST,
            db_database=config.DB_DATABASE,
            db_user=config.DB_USERNAME,
            db_password=config.DB_PASSWORD,
            workflow=geoflow_workflow.model_dump()
        ).run_workflow()

        geoflow_processes[process_id]['status'] = "SUCCESS"
        geoflow_processes[process_id]['workflow_id'] = geoflow_workflow.workflow_id
        geoflow_processes[process_id]['completion_time'] = datetime.datetime.now()
        geoflow_processes[process_id]['run_time_in_seconds'] = datetime.datetime.now()-start
    except Exception as error:
        geoflow_processes[process_id]['status'] = "FAILURE"
        geoflow_processes[process_id]['error'] = str(error)
        geoflow_processes[process_id]['completion_time'] = datetime.datetime.now()
        geoflow_processes[process_id]['run_time_in_seconds'] = datetime.datetime.now()-start