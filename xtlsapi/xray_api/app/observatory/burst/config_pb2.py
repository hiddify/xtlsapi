# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: app/observatory/burst/config.proto
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
    'app/observatory/burst/config.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"app/observatory/burst/config.proto\x12\x1fxray.core.app.observatory.burst\"j\n\x06\x43onfig\x12\x18\n\x10subject_selector\x18\x02 \x03(\t\x12\x46\n\x0bping_config\x18\x03 \x01(\x0b\x32\x31.xray.core.app.observatory.burst.HealthPingConfig\"w\n\x10HealthPingConfig\x12\x13\n\x0b\x64\x65stination\x18\x01 \x01(\t\x12\x14\n\x0c\x63onnectivity\x18\x02 \x01(\t\x12\x10\n\x08interval\x18\x03 \x01(\x03\x12\x15\n\rsamplingCount\x18\x04 \x01(\x05\x12\x0f\n\x07timeout\x18\x05 \x01(\x03\x42p\n\x1e\x63om.xray.app.observatory.burstP\x01Z/github.com/xtls/xray-core/app/observatory/burst\xaa\x02\x1aXray.App.Observatory.Burstb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.observatory.burst.config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.xray.app.observatory.burstP\001Z/github.com/xtls/xray-core/app/observatory/burst\252\002\032Xray.App.Observatory.Burst'
  _globals['_CONFIG']._serialized_start=71
  _globals['_CONFIG']._serialized_end=177
  _globals['_HEALTHPINGCONFIG']._serialized_start=179
  _globals['_HEALTHPINGCONFIG']._serialized_end=298
# @@protoc_insertion_point(module_scope)
