# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: common/protocol/headers.proto
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
    'common/protocol/headers.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63ommon/protocol/headers.proto\x12\x14xray.common.protocol\"B\n\x0eSecurityConfig\x12\x30\n\x04type\x18\x01 \x01(\x0e\x32\".xray.common.protocol.SecurityType*`\n\x0cSecurityType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04\x41UTO\x10\x02\x12\x0e\n\nAES128_GCM\x10\x03\x12\x15\n\x11\x43HACHA20_POLY1305\x10\x04\x12\x08\n\x04NONE\x10\x05\x12\x08\n\x04ZERO\x10\x06\x42^\n\x18\x63om.xray.common.protocolP\x01Z)github.com/xtls/xray-core/common/protocol\xaa\x02\x14Xray.Common.Protocolb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.protocol.headers_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.xray.common.protocolP\001Z)github.com/xtls/xray-core/common/protocol\252\002\024Xray.Common.Protocol'
  _globals['_SECURITYTYPE']._serialized_start=123
  _globals['_SECURITYTYPE']._serialized_end=219
  _globals['_SECURITYCONFIG']._serialized_start=55
  _globals['_SECURITYCONFIG']._serialized_end=121
# @@protoc_insertion_point(module_scope)
