# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: transport/internet/http/config.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'transport/internet/http/config.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xtlsapi.xray_api.transport.internet.headers.http import config_pb2 as transport_dot_internet_dot_headers_dot_http_dot_config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$transport/internet/http/config.proto\x12\x1cxray.transport.internet.http\x1a,transport/internet/headers/http/config.proto\"\xa6\x01\n\x06\x43onfig\x12\x0c\n\x04host\x18\x01 \x03(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x14\n\x0cidle_timeout\x18\x03 \x01(\x05\x12\x1c\n\x14health_check_timeout\x18\x04 \x01(\x05\x12\x0e\n\x06method\x18\x05 \x01(\t\x12<\n\x06header\x18\x06 \x03(\x0b\x32,.xray.transport.internet.headers.http.HeaderBv\n com.xray.transport.internet.httpP\x01Z1github.com/xtls/xray-core/transport/internet/http\xaa\x02\x1cXray.Transport.Internet.Httpb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transport.internet.http.config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.xray.transport.internet.httpP\001Z1github.com/xtls/xray-core/transport/internet/http\252\002\034Xray.Transport.Internet.Http'
  _globals['_CONFIG']._serialized_start=117
  _globals['_CONFIG']._serialized_end=283
# @@protoc_insertion_point(module_scope)
