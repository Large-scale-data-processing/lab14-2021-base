from flask import Flask, request, jsonify, render_template
from ariadne import graphql_sync, make_executable_schema, gql, load_schema_from_path
from ariadne.constants import PLAYGROUND_HTML
from ariadne import QueryType

query = QueryType()

@query.field("hello")
def resolve_hello(_, info):
    return "Hi there"

# We'll create this schema soon
type_defs = gql(load_schema_from_path("./schema.graphql"))
schema = make_executable_schema(type_defs, query)

app = Flask(__name__, static_url_path='',
                  static_folder='../frontend/build',
                  template_folder='../frontend/build')

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    """Serve GraphiQL playground"""
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == '__main__':
    app.run(debug=True)