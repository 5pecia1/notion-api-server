from flask import (
    Flask, request
)

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
    db_url = request.values.get("database", type=str)
    fields = request.values.get("fields", default={}, type=dict)

    return "good"
