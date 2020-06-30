# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import seabird_pb2 as seabird__pb2


class SeabirdStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamEvents = channel.unary_stream(
                '/seabird.Seabird/StreamEvents',
                request_serializer=seabird__pb2.StreamEventsRequest.SerializeToString,
                response_deserializer=seabird__pb2.Event.FromString,
                )
        self.PerformAction = channel.unary_unary(
                '/seabird.Seabird/PerformAction',
                request_serializer=seabird__pb2.PerformActionRequest.SerializeToString,
                response_deserializer=seabird__pb2.PerformActionResponse.FromString,
                )
        self.PerformPrivateAction = channel.unary_unary(
                '/seabird.Seabird/PerformPrivateAction',
                request_serializer=seabird__pb2.PerformPrivateActionRequest.SerializeToString,
                response_deserializer=seabird__pb2.PerformPrivateActionResponse.FromString,
                )
        self.SendMessage = channel.unary_unary(
                '/seabird.Seabird/SendMessage',
                request_serializer=seabird__pb2.SendMessageRequest.SerializeToString,
                response_deserializer=seabird__pb2.SendMessageResponse.FromString,
                )
        self.SendPrivateMessage = channel.unary_unary(
                '/seabird.Seabird/SendPrivateMessage',
                request_serializer=seabird__pb2.SendPrivateMessageRequest.SerializeToString,
                response_deserializer=seabird__pb2.SendPrivateMessageResponse.FromString,
                )
        self.JoinChannel = channel.unary_unary(
                '/seabird.Seabird/JoinChannel',
                request_serializer=seabird__pb2.JoinChannelRequest.SerializeToString,
                response_deserializer=seabird__pb2.JoinChannelResponse.FromString,
                )
        self.LeaveChannel = channel.unary_unary(
                '/seabird.Seabird/LeaveChannel',
                request_serializer=seabird__pb2.LeaveChannelRequest.SerializeToString,
                response_deserializer=seabird__pb2.LeaveChannelResponse.FromString,
                )
        self.UpdateChannelInfo = channel.unary_unary(
                '/seabird.Seabird/UpdateChannelInfo',
                request_serializer=seabird__pb2.UpdateChannelInfoRequest.SerializeToString,
                response_deserializer=seabird__pb2.UpdateChannelInfoResponse.FromString,
                )
        self.ListBackends = channel.unary_unary(
                '/seabird.Seabird/ListBackends',
                request_serializer=seabird__pb2.ListBackendsRequest.SerializeToString,
                response_deserializer=seabird__pb2.ListBackendsResponse.FromString,
                )
        self.GetBackendInfo = channel.unary_unary(
                '/seabird.Seabird/GetBackendInfo',
                request_serializer=seabird__pb2.BackendInfoRequest.SerializeToString,
                response_deserializer=seabird__pb2.BackendInfoResponse.FromString,
                )
        self.ListChannels = channel.unary_unary(
                '/seabird.Seabird/ListChannels',
                request_serializer=seabird__pb2.ListChannelsRequest.SerializeToString,
                response_deserializer=seabird__pb2.ListChannelsResponse.FromString,
                )
        self.GetChannelInfo = channel.unary_unary(
                '/seabird.Seabird/GetChannelInfo',
                request_serializer=seabird__pb2.ChannelInfoRequest.SerializeToString,
                response_deserializer=seabird__pb2.ChannelInfoResponse.FromString,
                )
        self.GetCoreInfo = channel.unary_unary(
                '/seabird.Seabird/GetCoreInfo',
                request_serializer=seabird__pb2.CoreInfoRequest.SerializeToString,
                response_deserializer=seabird__pb2.CoreInfoResponse.FromString,
                )


class SeabirdServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StreamEvents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PerformAction(self, request, context):
        """Chat actions
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PerformPrivateAction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendPrivateMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def JoinChannel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LeaveChannel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateChannelInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBackends(self, request, context):
        """Chat backend introspection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBackendInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListChannels(self, request, context):
        """Chat connection introspection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChannelInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCoreInfo(self, request, context):
        """Seabird introspection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SeabirdServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamEvents': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamEvents,
                    request_deserializer=seabird__pb2.StreamEventsRequest.FromString,
                    response_serializer=seabird__pb2.Event.SerializeToString,
            ),
            'PerformAction': grpc.unary_unary_rpc_method_handler(
                    servicer.PerformAction,
                    request_deserializer=seabird__pb2.PerformActionRequest.FromString,
                    response_serializer=seabird__pb2.PerformActionResponse.SerializeToString,
            ),
            'PerformPrivateAction': grpc.unary_unary_rpc_method_handler(
                    servicer.PerformPrivateAction,
                    request_deserializer=seabird__pb2.PerformPrivateActionRequest.FromString,
                    response_serializer=seabird__pb2.PerformPrivateActionResponse.SerializeToString,
            ),
            'SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=seabird__pb2.SendMessageRequest.FromString,
                    response_serializer=seabird__pb2.SendMessageResponse.SerializeToString,
            ),
            'SendPrivateMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendPrivateMessage,
                    request_deserializer=seabird__pb2.SendPrivateMessageRequest.FromString,
                    response_serializer=seabird__pb2.SendPrivateMessageResponse.SerializeToString,
            ),
            'JoinChannel': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinChannel,
                    request_deserializer=seabird__pb2.JoinChannelRequest.FromString,
                    response_serializer=seabird__pb2.JoinChannelResponse.SerializeToString,
            ),
            'LeaveChannel': grpc.unary_unary_rpc_method_handler(
                    servicer.LeaveChannel,
                    request_deserializer=seabird__pb2.LeaveChannelRequest.FromString,
                    response_serializer=seabird__pb2.LeaveChannelResponse.SerializeToString,
            ),
            'UpdateChannelInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateChannelInfo,
                    request_deserializer=seabird__pb2.UpdateChannelInfoRequest.FromString,
                    response_serializer=seabird__pb2.UpdateChannelInfoResponse.SerializeToString,
            ),
            'ListBackends': grpc.unary_unary_rpc_method_handler(
                    servicer.ListBackends,
                    request_deserializer=seabird__pb2.ListBackendsRequest.FromString,
                    response_serializer=seabird__pb2.ListBackendsResponse.SerializeToString,
            ),
            'GetBackendInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBackendInfo,
                    request_deserializer=seabird__pb2.BackendInfoRequest.FromString,
                    response_serializer=seabird__pb2.BackendInfoResponse.SerializeToString,
            ),
            'ListChannels': grpc.unary_unary_rpc_method_handler(
                    servicer.ListChannels,
                    request_deserializer=seabird__pb2.ListChannelsRequest.FromString,
                    response_serializer=seabird__pb2.ListChannelsResponse.SerializeToString,
            ),
            'GetChannelInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetChannelInfo,
                    request_deserializer=seabird__pb2.ChannelInfoRequest.FromString,
                    response_serializer=seabird__pb2.ChannelInfoResponse.SerializeToString,
            ),
            'GetCoreInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCoreInfo,
                    request_deserializer=seabird__pb2.CoreInfoRequest.FromString,
                    response_serializer=seabird__pb2.CoreInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'seabird.Seabird', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Seabird(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StreamEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/seabird.Seabird/StreamEvents',
            seabird__pb2.StreamEventsRequest.SerializeToString,
            seabird__pb2.Event.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PerformAction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/PerformAction',
            seabird__pb2.PerformActionRequest.SerializeToString,
            seabird__pb2.PerformActionResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PerformPrivateAction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/PerformPrivateAction',
            seabird__pb2.PerformPrivateActionRequest.SerializeToString,
            seabird__pb2.PerformPrivateActionResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/SendMessage',
            seabird__pb2.SendMessageRequest.SerializeToString,
            seabird__pb2.SendMessageResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendPrivateMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/SendPrivateMessage',
            seabird__pb2.SendPrivateMessageRequest.SerializeToString,
            seabird__pb2.SendPrivateMessageResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def JoinChannel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/JoinChannel',
            seabird__pb2.JoinChannelRequest.SerializeToString,
            seabird__pb2.JoinChannelResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LeaveChannel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/LeaveChannel',
            seabird__pb2.LeaveChannelRequest.SerializeToString,
            seabird__pb2.LeaveChannelResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateChannelInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/UpdateChannelInfo',
            seabird__pb2.UpdateChannelInfoRequest.SerializeToString,
            seabird__pb2.UpdateChannelInfoResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListBackends(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/ListBackends',
            seabird__pb2.ListBackendsRequest.SerializeToString,
            seabird__pb2.ListBackendsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBackendInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/GetBackendInfo',
            seabird__pb2.BackendInfoRequest.SerializeToString,
            seabird__pb2.BackendInfoResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListChannels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/ListChannels',
            seabird__pb2.ListChannelsRequest.SerializeToString,
            seabird__pb2.ListChannelsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetChannelInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/GetChannelInfo',
            seabird__pb2.ChannelInfoRequest.SerializeToString,
            seabird__pb2.ChannelInfoResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCoreInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/GetCoreInfo',
            seabird__pb2.CoreInfoRequest.SerializeToString,
            seabird__pb2.CoreInfoResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
