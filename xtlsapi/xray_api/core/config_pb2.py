# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: core/config.proto
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
    'core/config.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xtlsapi.xray_api.common.serial import typed_message_pb2 as common_dot_serial_dot_typed__message__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x63ore/config.proto\x12\txray.core\x1a!common/serial/typed_message.proto\"\xd8\x01\n\x06\x43onfig\x12\x30\n\x07inbound\x18\x01 \x03(\x0b\x32\x1f.xray.core.InboundHandlerConfig\x12\x32\n\x08outbound\x18\x02 \x03(\x0b\x32 .xray.core.OutboundHandlerConfig\x12-\n\x03\x61pp\x18\x04 \x03(\x0b\x32 .xray.common.serial.TypedMessage\x12\x33\n\textension\x18\x06 \x03(\x0b\x32 .xray.common.serial.TypedMessageJ\x04\x08\x03\x10\x04\"\x9a\x01\n\x14InboundHandlerConfig\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12;\n\x11receiver_settings\x18\x02 \x01(\x0b\x32 .xray.common.serial.TypedMessage\x12\x38\n\x0eproxy_settings\x18\x03 \x01(\x0b\x32 .xray.common.serial.TypedMessage\"\xba\x01\n\x15OutboundHandlerConfig\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x39\n\x0fsender_settings\x18\x02 \x01(\x0b\x32 .xray.common.serial.TypedMessage\x12\x38\n\x0eproxy_settings\x18\x03 \x01(\x0b\x32 .xray.common.serial.TypedMessage\x12\x0e\n\x06\x65xpire\x18\x04 \x01(\x03\x12\x0f\n\x07\x63omment\x18\x05 \x01(\tB=\n\rcom.xray.coreP\x01Z\x1egithub.com/xtls/xray-core/core\xaa\x02\tXray.Coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'core.config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\rcom.xray.coreP\001Z\036github.com/xtls/xray-core/core\252\002\tXray.Core'
  _globals['_CONFIG']._serialized_start=68
  _globals['_CONFIG']._serialized_end=284
  _globals['_INBOUNDHANDLERCONFIG']._serialized_start=287
  _globals['_INBOUNDHANDLERCONFIG']._serialized_end=441
  _globals['_OUTBOUNDHANDLERCONFIG']._serialized_start=444
  _globals['_OUTBOUNDHANDLERCONFIG']._serialized_end=630
# @@protoc_insertion_point(module_scope)
