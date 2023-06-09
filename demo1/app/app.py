from flask import Flask, Response
import sys

from google.protobuf.json_format import MessageToJson
from client_wrapper import ServiceClient as ServiceClient

import users_pb2_grpc as users_service
import users_types_pb2 as users_messages

app = Flask(__name__)

@app.route("/healthz")
def ping():
    return "ok2", 200

@app.route('/users/')
def users_get():
    app.config['users'] = ServiceClient(users_service, 'UsersStub', 'users', 50051)
    request = users_messages.GetUsersRequest(
        user=[users_messages.User(username="alexa", user_id=1),
              users_messages.User(username="christie", user_id=1)]
    )
    def get_user():
        response = app.config['users'].GetUsers(request)
        for resp in response:
            yield MessageToJson(resp)
    return Response(get_user(), content_type='application/json')