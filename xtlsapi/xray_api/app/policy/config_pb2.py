# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: app/policy/config.proto
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
    'app/policy/config.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x61pp/policy/config.proto\x12\x0fxray.app.policy\"\x17\n\x06Second\x12\r\n\x05value\x18\x01 \x01(\r\"\xc8\x03\n\x06Policy\x12\x30\n\x07timeout\x18\x01 \x01(\x0b\x32\x1f.xray.app.policy.Policy.Timeout\x12,\n\x05stats\x18\x02 \x01(\x0b\x32\x1d.xray.app.policy.Policy.Stats\x12.\n\x06\x62uffer\x18\x03 \x01(\x0b\x32\x1e.xray.app.policy.Policy.Buffer\x1a\xc5\x01\n\x07Timeout\x12*\n\thandshake\x18\x01 \x01(\x0b\x32\x17.xray.app.policy.Second\x12\x30\n\x0f\x63onnection_idle\x18\x02 \x01(\x0b\x32\x17.xray.app.policy.Second\x12,\n\x0buplink_only\x18\x03 \x01(\x0b\x32\x17.xray.app.policy.Second\x12.\n\rdownlink_only\x18\x04 \x01(\x0b\x32\x17.xray.app.policy.Second\x1aH\n\x05Stats\x12\x13\n\x0buser_uplink\x18\x01 \x01(\x08\x12\x15\n\ruser_downlink\x18\x02 \x01(\x08\x12\x13\n\x0buser_online\x18\x03 \x01(\x08\x1a\x1c\n\x06\x42uffer\x12\x12\n\nconnection\x18\x01 \x01(\x05\"\xb1\x01\n\x0cSystemPolicy\x12\x32\n\x05stats\x18\x01 \x01(\x0b\x32#.xray.app.policy.SystemPolicy.Stats\x1am\n\x05Stats\x12\x16\n\x0einbound_uplink\x18\x01 \x01(\x08\x12\x18\n\x10inbound_downlink\x18\x02 \x01(\x08\x12\x17\n\x0foutbound_uplink\x18\x03 \x01(\x08\x12\x19\n\x11outbound_downlink\x18\x04 \x01(\x08\"\xb1\x01\n\x06\x43onfig\x12\x31\n\x05level\x18\x01 \x03(\x0b\x32\".xray.app.policy.Config.LevelEntry\x12-\n\x06system\x18\x02 \x01(\x0b\x32\x1d.xray.app.policy.SystemPolicy\x1a\x45\n\nLevelEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.xray.app.policy.Policy:\x02\x38\x01\x42O\n\x13\x63om.xray.app.policyP\x01Z$github.com/xtls/xray-core/app/policy\xaa\x02\x0fXray.App.Policyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.policy.config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.xray.app.policyP\001Z$github.com/xtls/xray-core/app/policy\252\002\017Xray.App.Policy'
  _globals['_CONFIG_LEVELENTRY']._loaded_options = None
  _globals['_CONFIG_LEVELENTRY']._serialized_options = b'8\001'
  _globals['_SECOND']._serialized_start=44
  _globals['_SECOND']._serialized_end=67
  _globals['_POLICY']._serialized_start=70
  _globals['_POLICY']._serialized_end=526
  _globals['_POLICY_TIMEOUT']._serialized_start=225
  _globals['_POLICY_TIMEOUT']._serialized_end=422
  _globals['_POLICY_STATS']._serialized_start=424
  _globals['_POLICY_STATS']._serialized_end=496
  _globals['_POLICY_BUFFER']._serialized_start=498
  _globals['_POLICY_BUFFER']._serialized_end=526
  _globals['_SYSTEMPOLICY']._serialized_start=529
  _globals['_SYSTEMPOLICY']._serialized_end=706
  _globals['_SYSTEMPOLICY_STATS']._serialized_start=597
  _globals['_SYSTEMPOLICY_STATS']._serialized_end=706
  _globals['_CONFIG']._serialized_start=709
  _globals['_CONFIG']._serialized_end=886
  _globals['_CONFIG_LEVELENTRY']._serialized_start=817
  _globals['_CONFIG_LEVELENTRY']._serialized_end=886
# @@protoc_insertion_point(module_scope)
