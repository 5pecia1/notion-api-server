import os
from typing import Dict
from .notion import client

Fields = Dict[str, any]

def add_block(db_url: str, fields: Fields) -> bool:
    cv = client.get_collection_view(db_url)
    #TODO: https://github.com/jamalex/notion-py/issues/132
    row = cv.collection.add_row()

    row.title = fields['name']
    del fields["name"]

    for k, v in fields.items():
        setattr(row, k, v)

    return True