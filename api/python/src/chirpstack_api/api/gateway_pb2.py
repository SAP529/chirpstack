# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/api/gateway.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from chirpstack_api.common import common_pb2 as chirpstack__api_dot_common_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n chirpstack-api/api/gateway.proto\x12\x03\x61pi\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\"chirpstack-api/common/common.proto\"\xa9\x02\n\x07Gateway\x12\x12\n\ngateway_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\"\n\x08location\x18\x04 \x01(\x0b\x32\x10.common.Location\x12\x11\n\ttenant_id\x18\x05 \x01(\t\x12$\n\x04tags\x18\x06 \x03(\x0b\x32\x16.api.Gateway.TagsEntry\x12,\n\x08metadata\x18\x07 \x03(\x0b\x32\x1a.api.Gateway.MetadataEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xfe\x02\n\x0fGatewayListItem\x12\x11\n\ttenant_id\x18\x01 \x01(\t\x12\x12\n\ngateway_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\"\n\x08location\x18\x05 \x01(\x0b\x32\x10.common.Location\x12\x38\n\nproperties\x18\x06 \x03(\x0b\x32$.api.GatewayListItem.PropertiesEntry\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0clast_seen_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"5\n\x14\x43reateGatewayRequest\x12\x1d\n\x07gateway\x18\x01 \x01(\x0b\x32\x0c.api.Gateway\"\'\n\x11GetGatewayRequest\x12\x12\n\ngateway_id\x18\x01 \x01(\t\"\xc5\x01\n\x12GetGatewayResponse\x12\x1d\n\x07gateway\x18\x01 \x01(\x0b\x32\x0c.api.Gateway\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0clast_seen_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"5\n\x14UpdateGatewayRequest\x12\x1d\n\x07gateway\x18\x01 \x01(\x0b\x32\x0c.api.Gateway\"*\n\x14\x44\x65leteGatewayRequest\x12\x12\n\ngateway_id\x18\x01 \x01(\t\"W\n\x13ListGatewaysRequest\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\r\x12\x0e\n\x06search\x18\x03 \x01(\t\x12\x11\n\ttenant_id\x18\x04 \x01(\t\"Q\n\x14ListGatewaysResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\r\x12$\n\x06result\x18\x02 \x03(\x0b\x32\x14.api.GatewayListItem\"=\n\'GenerateGatewayClientCertificateRequest\x12\x12\n\ngateway_id\x18\x01 \x01(\t\"\x8e\x01\n(GenerateGatewayClientCertificateResponse\x12\x10\n\x08tls_cert\x18\x01 \x01(\t\x12\x0f\n\x07tls_key\x18\x02 \x01(\t\x12\x0f\n\x07\x63\x61_cert\x18\x03 \x01(\t\x12.\n\nexpires_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xac\x01\n\x18GetGatewayMetricsRequest\x12\x12\n\ngateway_id\x18\x01 \x01(\t\x12)\n\x05start\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03\x65nd\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x0b\x61ggregation\x18\x04 \x01(\x0e\x32\x13.common.Aggregation\"\xc2\x02\n\x19GetGatewayMetricsResponse\x12\"\n\nrx_packets\x18\x01 \x01(\x0b\x32\x0e.common.Metric\x12\"\n\ntx_packets\x18\x02 \x01(\x0b\x32\x0e.common.Metric\x12+\n\x13tx_packets_per_freq\x18\x03 \x01(\x0b\x32\x0e.common.Metric\x12+\n\x13rx_packets_per_freq\x18\x04 \x01(\x0b\x32\x0e.common.Metric\x12)\n\x11tx_packets_per_dr\x18\x05 \x01(\x0b\x32\x0e.common.Metric\x12)\n\x11rx_packets_per_dr\x18\x06 \x01(\x0b\x32\x0e.common.Metric\x12-\n\x15tx_packets_per_status\x18\x07 \x01(\x0b\x32\x0e.common.Metric2\x91\x06\n\x0eGatewayService\x12U\n\x06\x43reate\x12\x19.api.CreateGatewayRequest\x1a\x16.google.protobuf.Empty\"\x18\x82\xd3\xe4\x93\x02\x12\"\r/api/gateways:\x01*\x12Z\n\x03Get\x12\x16.api.GetGatewayRequest\x1a\x17.api.GetGatewayResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/api/gateways/{gateway_id}\x12j\n\x06Update\x12\x19.api.UpdateGatewayRequest\x1a\x16.google.protobuf.Empty\"-\x82\xd3\xe4\x93\x02\'\x1a\"/api/gateways/{gateway.gateway_id}:\x01*\x12_\n\x06\x44\x65lete\x12\x19.api.DeleteGatewayRequest\x1a\x16.google.protobuf.Empty\"\"\x82\xd3\xe4\x93\x02\x1c*\x1a/api/gateways/{gateway_id}\x12R\n\x04List\x12\x18.api.ListGatewaysRequest\x1a\x19.api.ListGatewaysResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/api/gateways\x12\xb1\x01\n\x19GenerateClientCertificate\x12,.api.GenerateGatewayClientCertificateRequest\x1a-.api.GenerateGatewayClientCertificateResponse\"7\x82\xd3\xe4\x93\x02\x31\"//api/gateways/{gateway_id}/generate-certificate\x12w\n\nGetMetrics\x12\x1d.api.GetGatewayMetricsRequest\x1a\x1e.api.GetGatewayMetricsResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/api/gateways/{gateway_id}/metricsBS\n\x11io.chirpstack.apiB\x0cGatewayProtoP\x01Z.github.com/chirpstack/chirpstack/api/go/v4/apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.api.gateway_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021io.chirpstack.apiB\014GatewayProtoP\001Z.github.com/chirpstack/chirpstack/api/go/v4/api'
  _GATEWAY_TAGSENTRY._options = None
  _GATEWAY_TAGSENTRY._serialized_options = b'8\001'
  _GATEWAY_METADATAENTRY._options = None
  _GATEWAY_METADATAENTRY._serialized_options = b'8\001'
  _GATEWAYLISTITEM_PROPERTIESENTRY._options = None
  _GATEWAYLISTITEM_PROPERTIESENTRY._serialized_options = b'8\001'
  _GATEWAYSERVICE.methods_by_name['Create']._options = None
  _GATEWAYSERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\022\"\r/api/gateways:\001*'
  _GATEWAYSERVICE.methods_by_name['Get']._options = None
  _GATEWAYSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\034\022\032/api/gateways/{gateway_id}'
  _GATEWAYSERVICE.methods_by_name['Update']._options = None
  _GATEWAYSERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002\'\032\"/api/gateways/{gateway.gateway_id}:\001*'
  _GATEWAYSERVICE.methods_by_name['Delete']._options = None
  _GATEWAYSERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002\034*\032/api/gateways/{gateway_id}'
  _GATEWAYSERVICE.methods_by_name['List']._options = None
  _GATEWAYSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\017\022\r/api/gateways'
  _GATEWAYSERVICE.methods_by_name['GenerateClientCertificate']._options = None
  _GATEWAYSERVICE.methods_by_name['GenerateClientCertificate']._serialized_options = b'\202\323\344\223\0021\"//api/gateways/{gateway_id}/generate-certificate'
  _GATEWAYSERVICE.methods_by_name['GetMetrics']._options = None
  _GATEWAYSERVICE.methods_by_name['GetMetrics']._serialized_options = b'\202\323\344\223\002$\022\"/api/gateways/{gateway_id}/metrics'
  _GATEWAY._serialized_start=170
  _GATEWAY._serialized_end=467
  _GATEWAY_TAGSENTRY._serialized_start=375
  _GATEWAY_TAGSENTRY._serialized_end=418
  _GATEWAY_METADATAENTRY._serialized_start=420
  _GATEWAY_METADATAENTRY._serialized_end=467
  _GATEWAYLISTITEM._serialized_start=470
  _GATEWAYLISTITEM._serialized_end=852
  _GATEWAYLISTITEM_PROPERTIESENTRY._serialized_start=803
  _GATEWAYLISTITEM_PROPERTIESENTRY._serialized_end=852
  _CREATEGATEWAYREQUEST._serialized_start=854
  _CREATEGATEWAYREQUEST._serialized_end=907
  _GETGATEWAYREQUEST._serialized_start=909
  _GETGATEWAYREQUEST._serialized_end=948
  _GETGATEWAYRESPONSE._serialized_start=951
  _GETGATEWAYRESPONSE._serialized_end=1148
  _UPDATEGATEWAYREQUEST._serialized_start=1150
  _UPDATEGATEWAYREQUEST._serialized_end=1203
  _DELETEGATEWAYREQUEST._serialized_start=1205
  _DELETEGATEWAYREQUEST._serialized_end=1247
  _LISTGATEWAYSREQUEST._serialized_start=1249
  _LISTGATEWAYSREQUEST._serialized_end=1336
  _LISTGATEWAYSRESPONSE._serialized_start=1338
  _LISTGATEWAYSRESPONSE._serialized_end=1419
  _GENERATEGATEWAYCLIENTCERTIFICATEREQUEST._serialized_start=1421
  _GENERATEGATEWAYCLIENTCERTIFICATEREQUEST._serialized_end=1482
  _GENERATEGATEWAYCLIENTCERTIFICATERESPONSE._serialized_start=1485
  _GENERATEGATEWAYCLIENTCERTIFICATERESPONSE._serialized_end=1627
  _GETGATEWAYMETRICSREQUEST._serialized_start=1630
  _GETGATEWAYMETRICSREQUEST._serialized_end=1802
  _GETGATEWAYMETRICSRESPONSE._serialized_start=1805
  _GETGATEWAYMETRICSRESPONSE._serialized_end=2127
  _GATEWAYSERVICE._serialized_start=2130
  _GATEWAYSERVICE._serialized_end=2915
# @@protoc_insertion_point(module_scope)
