# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: transport/internet/grpc/encoding/stream.proto
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
    'transport/internet/grpc/encoding/stream.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-transport/internet/grpc/encoding/stream.proto\x12%xray.transport.internet.grpc.encoding\"\x14\n\x04Hunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x19\n\tMultiHunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x0c\x32\xe6\x01\n\x0bGRPCService\x12\x63\n\x03Tun\x12+.xray.transport.internet.grpc.encoding.Hunk\x1a+.xray.transport.internet.grpc.encoding.Hunk(\x01\x30\x01\x12r\n\x08TunMulti\x12\x30.xray.transport.internet.grpc.encoding.MultiHunk\x1a\x30.xray.transport.internet.grpc.encoding.MultiHunk(\x01\x30\x01\x42<Z:github.com/xtls/xray-core/transport/internet/grpc/encodingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transport.internet.grpc.encoding.stream_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z:github.com/xtls/xray-core/transport/internet/grpc/encoding'
  _globals['_HUNK']._serialized_start=88
  _globals['_HUNK']._serialized_end=108
  _globals['_MULTIHUNK']._serialized_start=110
  _globals['_MULTIHUNK']._serialized_end=135
  _globals['_GRPCSERVICE']._serialized_start=138
  _globals['_GRPCSERVICE']._serialized_end=368
# @@protoc_insertion_point(module_scope)
