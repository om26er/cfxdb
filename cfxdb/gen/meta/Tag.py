# automatically generated by the FlatBuffers compiler, do not modify

# namespace: meta

import flatbuffers

# /// Generic **tags attached to objects** stored in other tables. Primary key of this table is ``(table_oid, object_oid)``.
class Tag(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTag(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Tag()
        x.Init(buf, n + offset)
        return x

    # Tag
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

# /// Table of the object with the tag attached.
    # Tag
    def TableOid(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Tag
    def TableOidAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Tag
    def TableOidLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

# /// Object (within the table) with the tag attached.
    # Tag
    def ObjectOid(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Tag
    def ObjectOidAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Tag
    def ObjectOidLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

# /// Tag definition attached to the object.
    # Tag
    def TagOid(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Tag
    def TagOidAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Tag
    def TagOidLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def TagStart(builder): builder.StartObject(3)
def TagAddTableOid(builder, tableOid): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(tableOid), 0)
def TagStartTableOidVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def TagAddObjectOid(builder, objectOid): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(objectOid), 0)
def TagStartObjectOidVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def TagAddTagOid(builder, tagOid): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(tagOid), 0)
def TagStartTagOidVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def TagEnd(builder): return builder.EndObject()
