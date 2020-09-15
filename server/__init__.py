from flask import Flask

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
@app.route('/database')
def health_check():
    return "good"
