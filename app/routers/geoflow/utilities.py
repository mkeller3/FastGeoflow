"""FastGeoflow - Geoflow - Utilities"""

import uuid

def get_new_process_id() -> str:
    """
    Method to return a new process id
    """

    return str(uuid.uuid4())
