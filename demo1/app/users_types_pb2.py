# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: users_types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()



_USER = None
_CREATEUSERREQUEST = None
_CREATEUSERRESULT = None
_GETUSERSREQUEST = None
_GETUSERSRESULT = None

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11users_types.proto\x12\x05users\")\n\x04User\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\r\"F\n\x11\x43reateUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"-\n\x10\x43reateUserResult\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\",\n\x0fGetUsersRequest\x12\x19\n\x04user\x18\x01 \x03(\x0b\x32\x0b.users.User\"+\n\x0eGetUsersResult\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.Userb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'users_types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USER._serialized_start=28
  _USER._serialized_end=69
  _CREATEUSERREQUEST._serialized_start=71
  _CREATEUSERREQUEST._serialized_end=141
  _CREATEUSERRESULT._serialized_start=143
  _CREATEUSERRESULT._serialized_end=188
  _GETUSERSREQUEST._serialized_start=190
  _GETUSERSREQUEST._serialized_end=234
  _GETUSERSRESULT._serialized_start=236
  _GETUSERSRESULT._serialized_end=279
# @@protoc_insertion_point(module_scope)