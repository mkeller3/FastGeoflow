"""FastGeoflow - Geoflow"""

from fastapi import APIRouter, BackgroundTasks, Request

import app.routers.geoflow.utilities as utilities
import app.routers.geoflow.models as models
import app.routers.geoflow.tasks as tasks

router = APIRouter()

@router.get("/status/{process_id}", tags=["geoflow"])
def status(process_id: str):
    if process_id not in tasks.geoflow_processes:
        return {"status": "UNKNOWN", "error": "This process_id does not exist."}
    return tasks.geoflow_processes[process_id]

@router.post("/run_workflow", tags=["geoflow"], response_model=models.BaseResponseModel)
async def run_workflow(info: models.WorkflowModel, request: Request, background_tasks: BackgroundTasks):

    process_id = utilities.get_new_process_id()

    process_url = str(request.base_url)

    process_url += f"api/v1/geoflow/status/{process_id}"

    tasks.geoflow_processes[process_id] = {
        "status": "PENDING"
    }

    background_tasks.add_task(
        tasks.run_geoflow_workflow,
        geoflow_workflow=info,
        process_id=process_id
    )

    return {
        "process_id": process_id,
        "url": process_url
    }