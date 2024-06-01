"""FastGeoflow - Geoflow - Models"""

from typing import List

from pydantic import BaseModel, Field

class BaseResponseModel(BaseModel):
    process_id: str = Field(
        default="472e29dc-91a8-41d3-b05f-cee34006e3f7"
    )
    url: str = Field(
        default="http://127.0.0.1:8000/api/v1/analysis/status/472e29dc-91a8-41d3-b05f-cee34006e3f7"
    )

class NodeModel(BaseModel):
    """
    Model used for validation of a node in the workflow
    """

    type: str
    data: object
    id: str

    class Config:
        """config"""
        populate_by_name = True
        extra = 'allow'

class EdgeModel(BaseModel):
    """
    Model used for validation of a edge in the workflow
    """

    source: str
    target: str

    class Config:
        """config"""
        populate_by_name = True
        extra = 'allow'

class WorkflowModel(BaseModel):
    """
    Model used for validation of workflow
    """

    nodes: List[NodeModel]
    edges: List[EdgeModel]
    workflow_id: str
    clear_temporary_tables: bool