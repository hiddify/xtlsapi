# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transport/internet/quic/config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xtlsapi.xray_api.xtlsapi.xray_api.common.serial import typed_message_pb2 as common_dot_serial_dot_typed__message__pb2
from xtlsapi.xray_api.xtlsapi.xray_api.common.protocol import headers_pb2 as common_dot_protocol_dot_headers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$transport/internet/quic/config.proto\x12\x1cxray.transport.internet.quic\x1a!common/serial/typed_message.proto\x1a\x1d\x63ommon/protocol/headers.proto\"\x7f\n\x06\x43onfig\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x36\n\x08security\x18\x02 \x01(\x0b\x32$.xray.common.protocol.SecurityConfig\x12\x30\n\x06header\x18\x03 \x01(\x0b\x32 .xray.common.serial.TypedMessageBv\n com.xray.transport.internet.quicP\x01Z1github.com/xtls/xray-core/transport/internet/quic\xaa\x02\x1cXray.Transport.Internet.Quicb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transport.internet.quic.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n com.xray.transport.internet.quicP\001Z1github.com/xtls/xray-core/transport/internet/quic\252\002\034Xray.Transport.Internet.Quic'
  _globals['_CONFIG']._serialized_start=136
  _globals['_CONFIG']._serialized_end=263
# @@protoc_insertion_point(module_scope)
