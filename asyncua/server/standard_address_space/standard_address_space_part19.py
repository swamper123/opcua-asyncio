
# -*- coding: utf-8 -*-
"""
DO NOT EDIT THIS FILE!
It is automatically generated from opcfoundation.org schemas.
"""
import datetime
from dateutil.tz import tzutc

from asyncua import ua
from asyncua.ua import NodeId, QualifiedName, NumericNodeId, StringNodeId, GuidNodeId
from asyncua.ua import NodeClass, LocalizedText


def create_standard_address_space_Part19(server):
  
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(19077, 0)
    node.BrowseName = QualifiedName('MultiStateDictionaryEntryDiscreteBaseType', 0)
    node.NodeClass = NodeClass.VariableType
    node.ParentNodeId = NumericNodeId(11238, 0)
    node.ReferenceTypeId = NumericNodeId(45, 0)
    attrs = ua.VariableTypeAttributes()
    attrs.DisplayName = LocalizedText("MultiStateDictionaryEntryDiscreteBaseType")
    attrs.DisplayName = LocalizedText("MultiStateDictionaryEntryDiscreteBaseType")
    attrs.DataType = ua.NodeId(ua.ObjectIds.Number)
    attrs.ValueRank = -1
    node.NodeAttributes = attrs
    await server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(19077, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(19082, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(19077, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(19083, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(45, 0)
    ref.SourceNodeId = NumericNodeId(19077, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(11238, 0)
    refs.append(ref)
    await server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(19082, 0)
    node.BrowseName = QualifiedName('EnumDictionaryEntries', 0)
    node.NodeClass = NodeClass.Variable
    node.ParentNodeId = NumericNodeId(19077, 0)
    node.ReferenceTypeId = NumericNodeId(46, 0)
    node.TypeDefinition = NumericNodeId(68, 0)
    attrs = ua.VariableAttributes()
    attrs.DisplayName = LocalizedText("EnumDictionaryEntries")
    attrs.DataType = ua.NodeId(ua.ObjectIds.NodeId)
    attrs.ValueRank = 2
    attrs.ArrayDimensions = [0, 0]
    node.NodeAttributes = attrs
    await server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(19082, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(68, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(37, 0)
    ref.SourceNodeId = NumericNodeId(19082, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(78, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(19082, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(19077, 0)
    refs.append(ref)
    await server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(19083, 0)
    node.BrowseName = QualifiedName('ValueAsDictionaryEntries', 0)
    node.NodeClass = NodeClass.Variable
    node.ParentNodeId = NumericNodeId(19077, 0)
    node.ReferenceTypeId = NumericNodeId(46, 0)
    node.TypeDefinition = NumericNodeId(68, 0)
    attrs = ua.VariableAttributes()
    attrs.DisplayName = LocalizedText("ValueAsDictionaryEntries")
    attrs.DataType = ua.NodeId(ua.ObjectIds.NodeId)
    attrs.ValueRank = 1
    attrs.ArrayDimensions = [0]
    node.NodeAttributes = attrs
    await server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(19083, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(68, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(37, 0)
    ref.SourceNodeId = NumericNodeId(19083, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(80, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(19083, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(19077, 0)
    refs.append(ref)
    await server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(19084, 0)
    node.BrowseName = QualifiedName('MultiStateDictionaryEntryDiscreteType', 0)
    node.NodeClass = NodeClass.VariableType
    node.ParentNodeId = NumericNodeId(19077, 0)
    node.ReferenceTypeId = NumericNodeId(45, 0)
    attrs = ua.VariableTypeAttributes()
    attrs.DisplayName = LocalizedText("MultiStateDictionaryEntryDiscreteType")
    attrs.DisplayName = LocalizedText("MultiStateDictionaryEntryDiscreteType")
    attrs.DataType = ua.NodeId(ua.ObjectIds.Number)
    attrs.ValueRank = -1
    node.NodeAttributes = attrs
    await server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(19084, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(19090, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(45, 0)
    ref.SourceNodeId = NumericNodeId(19084, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(19077, 0)
    refs.append(ref)
    await server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = NumericNodeId(19090, 0)
    node.BrowseName = QualifiedName('ValueAsDictionaryEntries', 0)
    node.NodeClass = NodeClass.Variable
    node.ParentNodeId = NumericNodeId(19084, 0)
    node.ReferenceTypeId = NumericNodeId(46, 0)
    node.TypeDefinition = NumericNodeId(68, 0)
    attrs = ua.VariableAttributes()
    attrs.DisplayName = LocalizedText("ValueAsDictionaryEntries")
    attrs.DataType = ua.NodeId(ua.ObjectIds.NodeId)
    attrs.ValueRank = 1
    attrs.ArrayDimensions = [0]
    node.NodeAttributes = attrs
    await server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(40, 0)
    ref.SourceNodeId = NumericNodeId(19090, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(68, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = NumericNodeId(37, 0)
    ref.SourceNodeId = NumericNodeId(19090, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(78, 0)
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = False
    ref.ReferenceTypeId = NumericNodeId(46, 0)
    ref.SourceNodeId = NumericNodeId(19090, 0)
    ref.TargetNodeClass = NodeClass.DataType
    ref.TargetNodeId = NumericNodeId(19084, 0)
    refs.append(ref)
    await server.add_references(refs)
