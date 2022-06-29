# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modelresponse.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x13modelresponse.proto\x12\rmodelresponse\"_\n\x05Value\x12\x10\n\x06svalue\x18\x01 \x01(\tH\x00\x12\x10\n\x06ivalue\x18\x02 \x01(\x03H\x00\x12\x10\n\x06\x66value\x18\x03 \x01(\x02H\x00\x12\x10\n\x06\x62value\x18\x04 \x01(\x08H\x00\x42\x0e\n\x0coneof_values\"\xbb\x01\n\x13SingleStringRequest\x12\x0f\n\x07request\x18\x01 \x01(\t\x12I\n\x0cquery_kwargs\x18\x02 \x03(\x0b\x32\x33.modelresponse.SingleStringRequest.QueryKwargsEntry\x1aH\n\x10QueryKwargsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.modelresponse.Value:\x02\x38\x01\"9\n\x11SingleStringReply\x12\x10\n\x08response\x18\x01 \x01(\t\x12\x12\n\ntime_taken\x18\x02 \x01(\x02\"\xb9\x01\n\tQARequest\x12\x10\n\x08question\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontext\x18\x02 \x01(\t\x12?\n\x0cquery_kwargs\x18\x03 \x03(\x0b\x32).modelresponse.QARequest.QueryKwargsEntry\x1aH\n\x10QueryKwargsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.modelresponse.Value:\x02\x38\x01\"\xa1\x02\n\x13\x43onversationRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x1c\n\x0f\x63onversation_id\x18\x02 \x01(\x03H\x00\x88\x01\x01\x12\x18\n\x10past_user_inputs\x18\x03 \x03(\t\x12\x1b\n\x13generated_responses\x18\x04 \x03(\t\x12I\n\x0cquery_kwargs\x18\x05 \x03(\x0b\x32\x33.modelresponse.ConversationRequest.QueryKwargsEntry\x1aH\n\x10QueryKwargsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.modelresponse.Value:\x02\x38\x01\x42\x12\n\x10_conversation_id\"w\n\x11\x43onversationReply\x12\x17\n\x0f\x63onversation_id\x18\x01 \x01(\x03\x12\x18\n\x10past_user_inputs\x18\x02 \x03(\t\x12\x1b\n\x13generated_responses\x18\x03 \x03(\t\x12\x12\n\ntime_taken\x18\x04 \x01(\x02\x32\xbc\x04\n\rModelResponse\x12X\n\x0eGeneratorReply\x12\".modelresponse.SingleStringRequest\x1a .modelresponse.SingleStringReply\"\x00\x12]\n\x13\x43lassificationReply\x12\".modelresponse.SingleStringRequest\x1a .modelresponse.SingleStringReply\"\x00\x12V\n\x16QuestionAndAnswerReply\x12\x18.modelresponse.QARequest\x1a .modelresponse.SingleStringReply\"\x00\x12W\n\rFillMaskReply\x12\".modelresponse.SingleStringRequest\x1a .modelresponse.SingleStringReply\"\x00\x12\x62\n\x18TokenClassificationReply\x12\".modelresponse.SingleStringRequest\x1a .modelresponse.SingleStringReply\"\x00\x12]\n\x13\x43onversationalReply\x12\".modelresponse.ConversationRequest\x1a .modelresponse.ConversationReply\"\x00\x62\x06proto3'
)

_VALUE = DESCRIPTOR.message_types_by_name['Value']
_SINGLESTRINGREQUEST = DESCRIPTOR.message_types_by_name['SingleStringRequest']
_SINGLESTRINGREQUEST_QUERYKWARGSENTRY = _SINGLESTRINGREQUEST.nested_types_by_name[
    'QueryKwargsEntry']
_SINGLESTRINGREPLY = DESCRIPTOR.message_types_by_name['SingleStringReply']
_QAREQUEST = DESCRIPTOR.message_types_by_name['QARequest']
_QAREQUEST_QUERYKWARGSENTRY = _QAREQUEST.nested_types_by_name['QueryKwargsEntry']
_CONVERSATIONREQUEST = DESCRIPTOR.message_types_by_name['ConversationRequest']
_CONVERSATIONREQUEST_QUERYKWARGSENTRY = _CONVERSATIONREQUEST.nested_types_by_name[
    'QueryKwargsEntry']
_CONVERSATIONREPLY = DESCRIPTOR.message_types_by_name['ConversationReply']
Value = _reflection.GeneratedProtocolMessageType(
    'Value',
    (_message.Message,
     ),
    {
        'DESCRIPTOR': _VALUE,
        '__module__': 'modelresponse_pb2'
        # @@protoc_insertion_point(class_scope:modelresponse.Value)
    })
_sym_db.RegisterMessage(Value)

SingleStringRequest = _reflection.GeneratedProtocolMessageType(
    'SingleStringRequest',
    (_message.Message,
     ),
    {
        'QueryKwargsEntry':
        _reflection.GeneratedProtocolMessageType(
            'QueryKwargsEntry',
            (_message.Message,
             ),
            {
                'DESCRIPTOR': _SINGLESTRINGREQUEST_QUERYKWARGSENTRY,
                '__module__': 'modelresponse_pb2'
                # @@protoc_insertion_point(class_scope:modelresponse.SingleStringRequest.QueryKwargsEntry)
            }),
        'DESCRIPTOR':
        _SINGLESTRINGREQUEST,
        '__module__':
        'modelresponse_pb2'
        # @@protoc_insertion_point(class_scope:modelresponse.SingleStringRequest)
    })
_sym_db.RegisterMessage(SingleStringRequest)
_sym_db.RegisterMessage(SingleStringRequest.QueryKwargsEntry)

SingleStringReply = _reflection.GeneratedProtocolMessageType(
    'SingleStringReply',
    (_message.Message,
     ),
    {
        'DESCRIPTOR': _SINGLESTRINGREPLY,
        '__module__': 'modelresponse_pb2'
        # @@protoc_insertion_point(class_scope:modelresponse.SingleStringReply)
    })
_sym_db.RegisterMessage(SingleStringReply)

QARequest = _reflection.GeneratedProtocolMessageType(
    'QARequest',
    (_message.Message,
     ),
    {
        'QueryKwargsEntry':
        _reflection.GeneratedProtocolMessageType(
            'QueryKwargsEntry',
            (_message.Message,
             ),
            {
                'DESCRIPTOR': _QAREQUEST_QUERYKWARGSENTRY,
                '__module__': 'modelresponse_pb2'
                # @@protoc_insertion_point(class_scope:modelresponse.QARequest.QueryKwargsEntry)
            }),
        'DESCRIPTOR':
        _QAREQUEST,
        '__module__':
        'modelresponse_pb2'
        # @@protoc_insertion_point(class_scope:modelresponse.QARequest)
    })
_sym_db.RegisterMessage(QARequest)
_sym_db.RegisterMessage(QARequest.QueryKwargsEntry)

ConversationRequest = _reflection.GeneratedProtocolMessageType(
    'ConversationRequest',
    (_message.Message,
     ),
    {
        'QueryKwargsEntry':
        _reflection.GeneratedProtocolMessageType(
            'QueryKwargsEntry',
            (_message.Message,
             ),
            {
                'DESCRIPTOR': _CONVERSATIONREQUEST_QUERYKWARGSENTRY,
                '__module__': 'modelresponse_pb2'
                # @@protoc_insertion_point(class_scope:modelresponse.ConversationRequest.QueryKwargsEntry)
            }),
        'DESCRIPTOR':
        _CONVERSATIONREQUEST,
        '__module__':
        'modelresponse_pb2'
        # @@protoc_insertion_point(class_scope:modelresponse.ConversationRequest)
    })
_sym_db.RegisterMessage(ConversationRequest)
_sym_db.RegisterMessage(ConversationRequest.QueryKwargsEntry)

ConversationReply = _reflection.GeneratedProtocolMessageType(
    'ConversationReply',
    (_message.Message,
     ),
    {
        'DESCRIPTOR': _CONVERSATIONREPLY,
        '__module__': 'modelresponse_pb2'
        # @@protoc_insertion_point(class_scope:modelresponse.ConversationReply)
    })
_sym_db.RegisterMessage(ConversationReply)

_MODELRESPONSE = DESCRIPTOR.services_by_name['ModelResponse']
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _SINGLESTRINGREQUEST_QUERYKWARGSENTRY._options = None
    _SINGLESTRINGREQUEST_QUERYKWARGSENTRY._serialized_options = b'8\001'
    _QAREQUEST_QUERYKWARGSENTRY._options = None
    _QAREQUEST_QUERYKWARGSENTRY._serialized_options = b'8\001'
    _CONVERSATIONREQUEST_QUERYKWARGSENTRY._options = None
    _CONVERSATIONREQUEST_QUERYKWARGSENTRY._serialized_options = b'8\001'
    _VALUE._serialized_start = 38
    _VALUE._serialized_end = 133
    _SINGLESTRINGREQUEST._serialized_start = 136
    _SINGLESTRINGREQUEST._serialized_end = 323
    _SINGLESTRINGREQUEST_QUERYKWARGSENTRY._serialized_start = 251
    _SINGLESTRINGREQUEST_QUERYKWARGSENTRY._serialized_end = 323
    _SINGLESTRINGREPLY._serialized_start = 325
    _SINGLESTRINGREPLY._serialized_end = 382
    _QAREQUEST._serialized_start = 385
    _QAREQUEST._serialized_end = 570
    _QAREQUEST_QUERYKWARGSENTRY._serialized_start = 251
    _QAREQUEST_QUERYKWARGSENTRY._serialized_end = 323
    _CONVERSATIONREQUEST._serialized_start = 573
    _CONVERSATIONREQUEST._serialized_end = 862
    _CONVERSATIONREQUEST_QUERYKWARGSENTRY._serialized_start = 251
    _CONVERSATIONREQUEST_QUERYKWARGSENTRY._serialized_end = 323
    _CONVERSATIONREPLY._serialized_start = 864
    _CONVERSATIONREPLY._serialized_end = 983
    _MODELRESPONSE._serialized_start = 986
    _MODELRESPONSE._serialized_end = 1558
# @@protoc_insertion_point(module_scope)