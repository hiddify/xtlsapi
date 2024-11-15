# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proxy/freedom/config.proto
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
    'proxy/freedom/config.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xtlsapi.xray_api.common.protocol import server_spec_pb2 as common_dot_protocol_dot_server__spec__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aproxy/freedom/config.proto\x12\x12xray.proxy.freedom\x1a!common/protocol/server_spec.proto\"K\n\x13\x44\x65stinationOverride\x12\x34\n\x06server\x18\x01 \x01(\x0b\x32$.xray.common.protocol.ServerEndpoint\"\x88\x01\n\x08\x46ragment\x12\x14\n\x0cpackets_from\x18\x01 \x01(\x04\x12\x12\n\npackets_to\x18\x02 \x01(\x04\x12\x12\n\nlength_min\x18\x03 \x01(\x04\x12\x12\n\nlength_max\x18\x04 \x01(\x04\x12\x14\n\x0cinterval_min\x18\x05 \x01(\x04\x12\x14\n\x0cinterval_max\x18\x06 \x01(\x04\"h\n\x05Noise\x12\x12\n\nlength_min\x18\x01 \x01(\x04\x12\x12\n\nlength_max\x18\x02 \x01(\x04\x12\x11\n\tdelay_min\x18\x03 \x01(\x04\x12\x11\n\tdelay_max\x18\x04 \x01(\x04\x12\x11\n\tstr_noise\x18\x05 \x01(\x0c\"\xc6\x03\n\x06\x43onfig\x12\x42\n\x0f\x64omain_strategy\x18\x01 \x01(\x0e\x32).xray.proxy.freedom.Config.DomainStrategy\x12\x45\n\x14\x64\x65stination_override\x18\x03 \x01(\x0b\x32\'.xray.proxy.freedom.DestinationOverride\x12\x12\n\nuser_level\x18\x04 \x01(\r\x12.\n\x08\x66ragment\x18\x05 \x01(\x0b\x32\x1c.xray.proxy.freedom.Fragment\x12\x16\n\x0eproxy_protocol\x18\x06 \x01(\r\x12)\n\x06noises\x18\x07 \x03(\x0b\x32\x19.xray.proxy.freedom.Noise\"\xa9\x01\n\x0e\x44omainStrategy\x12\t\n\x05\x41S_IS\x10\x00\x12\n\n\x06USE_IP\x10\x01\x12\x0b\n\x07USE_IP4\x10\x02\x12\x0b\n\x07USE_IP6\x10\x03\x12\x0c\n\x08USE_IP46\x10\x04\x12\x0c\n\x08USE_IP64\x10\x05\x12\x0c\n\x08\x46ORCE_IP\x10\x06\x12\r\n\tFORCE_IP4\x10\x07\x12\r\n\tFORCE_IP6\x10\x08\x12\x0e\n\nFORCE_IP46\x10\t\x12\x0e\n\nFORCE_IP64\x10\nBX\n\x16\x63om.xray.proxy.freedomP\x01Z\'github.com/xtls/xray-core/proxy/freedom\xaa\x02\x12Xray.Proxy.Freedomb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proxy.freedom.config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.xray.proxy.freedomP\001Z\'github.com/xtls/xray-core/proxy/freedom\252\002\022Xray.Proxy.Freedom'
  _globals['_DESTINATIONOVERRIDE']._serialized_start=85
  _globals['_DESTINATIONOVERRIDE']._serialized_end=160
  _globals['_FRAGMENT']._serialized_start=163
  _globals['_FRAGMENT']._serialized_end=299
  _globals['_NOISE']._serialized_start=301
  _globals['_NOISE']._serialized_end=405
  _globals['_CONFIG']._serialized_start=408
  _globals['_CONFIG']._serialized_end=862
  _globals['_CONFIG_DOMAINSTRATEGY']._serialized_start=693
  _globals['_CONFIG_DOMAINSTRATEGY']._serialized_end=862
# @@protoc_insertion_point(module_scope)
