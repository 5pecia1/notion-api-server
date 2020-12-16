import os
from typing import Dict
from .notion import client
from .block import TextBlock

Fields = Dict[str, any]

def add_block(db_url: str, fields: Fields, content: any = None, query: any = None, update: any = None) -> bool:
    cv = client.get_collection_view(db_url)
    if query is not None:
        dbs = cv.default_query().execute()
        queried = []
        for r in dbs:
            if is_contain(query, r):
                queried.append(r)
        if update is not None:
            for q in queried:
                for u in update:
                    setattr(q, u, update[u])
        else:
            print(queried)
        
    else:
        row = cv.collection.add_row()

        for k, v in fields.items():
            setattr(row, k, v)

        if content != None: 
            # TODO: parse description
            newchild = row.children.add_new(TextBlock, title=content)
            # newchild = row.children.add_new(TextBlock, title=description)
            newchild.checked = True

    return True

def is_contain(query: any, row: any) -> bool:
    for a1 in query.keys():
        if query[a1] != getattr(row, a1):
                return False
    return True