# automatically generated by the FlatBuffers compiler, do not modify

# namespace: arealm

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class WampCraPrincipal(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsWampCraPrincipal(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = WampCraPrincipal()
        x.Init(buf, n + offset)
        return x

    # WampCraPrincipal
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ID of this object.
    # WampCraPrincipal
    def Oid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # WAMP authid of the principal, must be unique within the application realm at any moment in time.
    # WampCraPrincipal
    def Authid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ID of the application realm the authenticated principal will be joined to.
    # WampCraPrincipal
    def ArealmOid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ID of the role the authenticated principal will be joined to the application realm.
    # WampCraPrincipal
    def RoleOid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = o + self._tab.Pos
            from oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # WAMP-CRA specific stuff:
    # WampCraPrincipal
    def Secret(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # WampCraPrincipal
    def Salt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # WampCraPrincipal
    def Iterations(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # WampCraPrincipal
    def Keylen(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

def WampCraPrincipalStart(builder): builder.StartObject(8)
def WampCraPrincipalAddOid(builder, oid): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(oid), 0)
def WampCraPrincipalAddAuthid(builder, authid): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(authid), 0)
def WampCraPrincipalAddArealmOid(builder, arealmOid): builder.PrependStructSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(arealmOid), 0)
def WampCraPrincipalAddRoleOid(builder, roleOid): builder.PrependStructSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(roleOid), 0)
def WampCraPrincipalAddSecret(builder, secret): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(secret), 0)
def WampCraPrincipalAddSalt(builder, salt): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(salt), 0)
def WampCraPrincipalAddIterations(builder, iterations): builder.PrependUint32Slot(6, iterations, 0)
def WampCraPrincipalAddKeylen(builder, keylen): builder.PrependUint16Slot(7, keylen, 0)
def WampCraPrincipalEnd(builder): return builder.EndObject()
