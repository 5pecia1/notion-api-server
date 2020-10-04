from flask import (
    Flask, request
)
from notion_app import add_block

app = Flask(__name__)


@app.route('/')
def health_check():
    return "good"


# {
#     "payload": {
#         "database": "",
#         "fields": {
#             "priority": "P2",
#             "status": "Automatic",
#             "type": "🏢company",
#             "url": "{{ url }}",
#             "name": "{{ name }}"
#         }
#     },
#     "headers": {
#     },
# }
@app.route('/database', methods={"POST"})
def database():
    content = request.json
    db_url = content["database"]
    fields = content["fields"]

    result = add_block(db_url, fields)

    if result:
        return "good"
    else:
        return "bad", 400

