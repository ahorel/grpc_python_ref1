# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import users_types_pb2 as users__types__pb2


class UsersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
                '/Users/CreateUser',
                request_serializer=users__types__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=users__types__pb2.CreateUserResult.FromString,
                )
        self.GetUsers = channel.unary_stream(
                '/Users/GetUsers',
                request_serializer=users__types__pb2.GetUsersRequest.SerializeToString,
                response_deserializer=users__types__pb2.GetUsersResult.FromString,
                )


class UsersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=users__types__pb2.CreateUserRequest.FromString,
                    response_serializer=users__types__pb2.CreateUserResult.SerializeToString,
            ),
            'GetUsers': grpc.unary_stream_rpc_method_handler(
                    servicer.GetUsers,
                    request_deserializer=users__types__pb2.GetUsersRequest.FromString,
                    response_serializer=users__types__pb2.GetUsersResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Users', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Users(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Users/CreateUser',
            users__types__pb2.CreateUserRequest.SerializeToString,
            users__types__pb2.CreateUserResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Users/GetUsers',
            users__types__pb2.GetUsersRequest.SerializeToString,
            users__types__pb2.GetUsersResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
