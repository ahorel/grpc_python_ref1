# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import identity_pb2 as identity__pb2


class IdentityStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ValidateToken = channel.unary_unary(
                '/Identity/ValidateToken',
                request_serializer=identity__pb2.ValidateTokenRequest.SerializeToString,
                response_deserializer=identity__pb2.ValidateTokenReply.FromString,
                )
        self.ValidateFileDownload = channel.unary_unary(
                '/Identity/ValidateFileDownload',
                request_serializer=identity__pb2.ValidateFileDownloadRequest.SerializeToString,
                response_deserializer=identity__pb2.ValidateFileDownloadReply.FromString,
                )
        self.ValidateFileDelete = channel.unary_unary(
                '/Identity/ValidateFileDelete',
                request_serializer=identity__pb2.ValidateFileDeleteRequest.SerializeToString,
                response_deserializer=identity__pb2.ValidateFileDeleteReply.FromString,
                )
        self.ExpireToken = channel.stream_stream(
                '/Identity/ExpireToken',
                request_serializer=identity__pb2.ExpireTokenRequest.SerializeToString,
                response_deserializer=identity__pb2.ExpireTokenReply.FromString,
                )


class IdentityServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ValidateToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidateFileDownload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidateFileDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExpireToken(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IdentityServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ValidateToken': grpc.unary_unary_rpc_method_handler(
                    servicer.ValidateToken,
                    request_deserializer=identity__pb2.ValidateTokenRequest.FromString,
                    response_serializer=identity__pb2.ValidateTokenReply.SerializeToString,
            ),
            'ValidateFileDownload': grpc.unary_unary_rpc_method_handler(
                    servicer.ValidateFileDownload,
                    request_deserializer=identity__pb2.ValidateFileDownloadRequest.FromString,
                    response_serializer=identity__pb2.ValidateFileDownloadReply.SerializeToString,
            ),
            'ValidateFileDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.ValidateFileDelete,
                    request_deserializer=identity__pb2.ValidateFileDeleteRequest.FromString,
                    response_serializer=identity__pb2.ValidateFileDeleteReply.SerializeToString,
            ),
            'ExpireToken': grpc.stream_stream_rpc_method_handler(
                    servicer.ExpireToken,
                    request_deserializer=identity__pb2.ExpireTokenRequest.FromString,
                    response_serializer=identity__pb2.ExpireTokenReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Identity', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Identity(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ValidateToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Identity/ValidateToken',
            identity__pb2.ValidateTokenRequest.SerializeToString,
            identity__pb2.ValidateTokenReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValidateFileDownload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Identity/ValidateFileDownload',
            identity__pb2.ValidateFileDownloadRequest.SerializeToString,
            identity__pb2.ValidateFileDownloadReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValidateFileDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Identity/ValidateFileDelete',
            identity__pb2.ValidateFileDeleteRequest.SerializeToString,
            identity__pb2.ValidateFileDeleteReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExpireToken(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/Identity/ExpireToken',
            identity__pb2.ExpireTokenRequest.SerializeToString,
            identity__pb2.ExpireTokenReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
