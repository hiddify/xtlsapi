# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proxy/http/config.proto
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
    'proxy/http/config.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xtlsapi.xray_api.common.protocol import server_spec_pb2 as common_dot_protocol_dot_server__spec__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17proxy/http/config.proto\x12\x0fxray.proxy.http\x1a!common/protocol/server_spec.proto\"-\n\x07\x41\x63\x63ount\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\xad\x01\n\x0cServerConfig\x12=\n\x08\x61\x63\x63ounts\x18\x02 \x03(\x0b\x32+.xray.proxy.http.ServerConfig.AccountsEntry\x12\x19\n\x11\x61llow_transparent\x18\x03 \x01(\x08\x12\x12\n\nuser_level\x18\x04 \x01(\r\x1a/\n\rAccountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"$\n\x06Header\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"m\n\x0c\x43lientConfig\x12\x34\n\x06server\x18\x01 \x03(\x0b\x32$.xray.common.protocol.ServerEndpoint\x12\'\n\x06header\x18\x02 \x03(\x0b\x32\x17.xray.proxy.http.HeaderBO\n\x13\x63om.xray.proxy.httpP\x01Z$github.com/xtls/xray-core/proxy/http\xaa\x02\x0fXray.Proxy.Httpb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proxy.http.config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.xray.proxy.httpP\001Z$github.com/xtls/xray-core/proxy/http\252\002\017Xray.Proxy.Http'
  _globals['_SERVERCONFIG_ACCOUNTSENTRY']._loaded_options = None
  _globals['_SERVERCONFIG_ACCOUNTSENTRY']._serialized_options = b'8\001'
  _globals['_ACCOUNT']._serialized_start=79
  _globals['_ACCOUNT']._serialized_end=124
  _globals['_SERVERCONFIG']._serialized_start=127
  _globals['_SERVERCONFIG']._serialized_end=300
  _globals['_SERVERCONFIG_ACCOUNTSENTRY']._serialized_start=253
  _globals['_SERVERCONFIG_ACCOUNTSENTRY']._serialized_end=300
  _globals['_HEADER']._serialized_start=302
  _globals['_HEADER']._serialized_end=338
  _globals['_CLIENTCONFIG']._serialized_start=340
  _globals['_CLIENTCONFIG']._serialized_end=449
# @@protoc_insertion_point(module_scope)
