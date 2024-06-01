# FastGeoflow

FastGeoflow is a ...... .FastGeoflow is written in [Python](https://www.python.org/) using the [FastAPI](https://fastapi.tiangolo.com/) web framework. 

---

**Source Code**: <a href="https://github.com/mkeller3/FastGeoflow" target="_blank">https://github.com/mkeller3/FastGeoflow</a>

---

## Configuration

In order for the api to work you will need to edit the `config.py` file with your database connections.

Example
```python
DB_HOST = "localhost"
DB_DATABASE = "data"
DB_USERNAME = "postgres"
DB_PASSWORD = "postgres"
```

## Usage

### Running Locally

To run the app locally `uvicorn app.main:app --reload`

### Production
Build Dockerfile into a docker image to deploy to the cloud.

## API

| Method | URL | Description |
| ------ | --- | ----------- |
| `GET` | `/api/v1/geoflow/status/{process_id}` | [Geoflow Status](#Geoflow-Status)  |
| `POST` | `/api/v1/geoflow/run_workflow` | [Run Workflow](#Run-Workflow)  |


## Endpoint Description's

## Geoflow Status
Any time an geoflow is submitted it given a process_id to have the geoflow run in the background using [FastAPI's Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/). To check the
status of an geoflow, you can call this endpoint with the process_id.

## Example Call
```shell
/api/v1/geoflow/status/472e29dc-91a8-41d3-b05f-cee34006e3f7
```

## Example Output - Still Running
```json
{
    "status": "PENDING"
}
```

## Example Output - Complete
```json
{
    "status": "SUCCESS",
    "completion_time": "2022-07-06T19:33:17.950059",
    "run_time_in_seconds": 1.78599
}
```

## Example Output - Error
```json
{
    "status": "FAILURE",
    "error": "ERROR HERE",
    "completion_time": "2022-07-08T13:39:47.961389",
    "run_time_in_seconds": 0.040892
}
```

## Run Workflow

### Description
I

### Example Input
```json
{
    "workflow_id": "123",
    "clear_temporary_tables": true,
    "nodes": [
        {
            "type": "input",
            "data": {
                "type": "source",
                "output_table_name": "2023_wildfires",
                "output_table_schema": "public"
            },
            "events": {},
            "id": "dndnode_2",
            "position": {
                "x": 547,
                "y": -4.000000000000028
            },
            "label": "2023 Wildfires"
        },
        {
            "type": "default",
            "data": {
                "type": "analysis",
                "analysis": "filter",
                "output_table_name": "ujkbtfgpobtxlekphgvvtycvbqjdduhutltghfurrpxhumgkyn",
                "output_table_schema": "geoflow",
                "sql_filter": "attr_state = 'US-CA'"
            },
            "events": {},
            "id": "dndnode_3",
            "position": {
                "x": 538,
                "y": 94.99999999999997
            },
            "label": "Simple Filter"
        },
        {
            "type": "default",
            "data": {
                "type": "analysis",
                "analysis": "intersects",
                "output_table_name": "ujkbtfgpobtxlekphgvvtycvbqjdduhutltghfurrpxhumgkym",
                "output_table_schema": "geoflow"
            },
            "events": {},
            "id": "dndnode_4",
            "position": {
                "x": 473,
                "y": 260
            },
            "label": "Spatial Filter"
        },
        {
            "type": "default",
            "data": {
                "type": "analysis",
                "analysis": "filter",
                "output_table_name": "ujkbtfgpobtxlekphgvvtycvbqjdduhutltghfurrpxhumgkyr",
                "output_table_schema": "geoflow",
                "sql_filter": "state = 'CA'"
            },
            "events": {},
            "id": "dndnode_5",
            "position": {
                "x": 319.725626988259,
                "y": 91.62722729446045
            },
            "label": "Simple Filter"
        },
        {
            "type": "input",
            "data": {
                "type": "source",
                "output_table_name": "zip_code_population",
                "output_table_schema": "public"
            },
            "events": {},
            "id": "dndnode_6",
            "position": {
                "x": 369.31135720270663,
                "y": 0.16910267670175244
            },
            "label": "Zip Code Population"
        }
    ],
    "edges": [
        {
            "sourceHandle": "dndnode_2__handle-bottom",
            "targetHandle": "dndnode_3__handle-top",
            "type": "default",
            "source": "dndnode_2",
            "target": "dndnode_3",
            "data": {},
            "events": {},
            "id": "vueflow__edge-dndnode_2dndnode_2__handle-bottom-dndnode_3dndnode_3__handle-top",
            "sourceX": 622,
            "sourceY": 38.99999999999997,
            "targetX": 613,
            "targetY": 91.99999999999997
        },
        {
            "sourceHandle": "dndnode_3__handle-bottom",
            "targetHandle": "dndnode_4__handle-top",
            "type": "default",
            "source": "dndnode_3",
            "target": "dndnode_4",
            "data": {},
            "events": {},
            "id": "vueflow__edge-dndnode_3dndnode_3__handle-bottom-dndnode_4dndnode_4__handle-top",
            "sourceX": 613,
            "sourceY": 137.99999999999997,
            "targetX": 548,
            "targetY": 257
        },
        {
            "sourceHandle": "dndnode_6__handle-bottom",
            "targetHandle": "dndnode_5__handle-top",
            "type": "default",
            "source": "dndnode_6",
            "target": "dndnode_5",
            "data": {},
            "events": {},
            "id": "vueflow__edge-dndnode_6dndnode_6__handle-bottom-dndnode_5dndnode_5__handle-top",
            "sourceX": 444.30248270007485,
            "sourceY": 43.174734097695364,
            "targetX": 394.71675248562724,
            "targetY": 88.63370886022958
        },
        {
            "sourceHandle": "dndnode_5__handle-bottom",
            "targetHandle": "dndnode_4__handle-top",
            "type": "default",
            "source": "dndnode_5",
            "target": "dndnode_4",
            "data": {},
            "events": {},
            "id": "vueflow__edge-dndnode_5dndnode_5__handle-bottom-dndnode_4dndnode_4__handle-top",
            "sourceX": 394.71675248562724,
            "sourceY": 134.63285871545406,
            "targetX": 548,
            "targetY": 257
        }
    ],
    "position": [
        -81.15713093763446,
        305.84653608167775
    ],
    "zoom": 0.9075191553171605,
    "viewport": {
        "x": -81.15713093763446,
        "y": 305.84653608167775,
        "zoom": 0.9075191553171605
    }
}
```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/geoflow/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```
