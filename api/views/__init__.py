from flask import Blueprint
from flask_graphql import GraphQLView

graph_bp = Blueprint('graph', __name__)

from api.models.graphql_models import schema_query, schema_mutation

graph_bp.add_url_rule(
    '/query',
    view_func=GraphQLView.as_view(
        'graphql-query',
        schema=schema_query,
        graphiql=True),
)

graph_bp.add_url_rule(
    '/mutate',
    view_func=GraphQLView.as_view(
        'graphql-mutation',
        schema=schema_mutation,
        graphiql=True),
)