import os
from typing import Dict
from .notion import client
from .block import TextBlock

Fields = Dict[str, any]

def add_block(db_url: str, fields: Fields, content: any = None) -> bool:
    cv = client.get_collection_view(db_url)
    row = cv.collection.add_row()

    row.title = fields['name']
    del fields["name"]

    for k, v in fields.items():
        setattr(row, k, v)

    if content != None: 
        # TODO: parse description
        newchild = row.children.add_new(TextBlock, title=content)
        # newchild = row.children.add_new(TextBlock, title=description)
        newchild.checked = True

    return True