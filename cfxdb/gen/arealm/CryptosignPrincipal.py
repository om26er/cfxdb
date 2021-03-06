# automatically generated by the FlatBuffers compiler, do not modify

# namespace: arealm

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CryptosignPrincipal(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsCryptosignPrincipal(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CryptosignPrincipal()
        x.Init(buf, n + offset)
        return x

    # CryptosignPrincipal
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ID of this object.
    # CryptosignPrincipal
    def Oid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # WAMP authid of the principal, must be unique within the application realm at any moment in time.
    # CryptosignPrincipal
    def Authid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ID of the application realm the authenticated principal will be joined to.
    # CryptosignPrincipal
    def ArealmOid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ID of the role the authenticated principal will be joined to the application realm.
    # CryptosignPrincipal
    def RoleOid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # WAMP-cryptosign specific stuff:
    # Authorized public keys, eg 64 character hex strings of the 32 bytes Ed25519 public keys.
    # CryptosignPrincipal
    def AuthorizedKeys(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CryptosignPrincipal
    def AuthorizedKeysLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CryptosignPrincipal
    def AuthorizedKeysIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

def CryptosignPrincipalStart(builder): builder.StartObject(5)
def CryptosignPrincipalAddOid(builder, oid): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(oid), 0)
def CryptosignPrincipalAddAuthid(builder, authid): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(authid), 0)
def CryptosignPrincipalAddArealmOid(builder, arealmOid): builder.PrependStructSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(arealmOid), 0)
def CryptosignPrincipalAddRoleOid(builder, roleOid): builder.PrependStructSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(roleOid), 0)
def CryptosignPrincipalAddAuthorizedKeys(builder, authorizedKeys): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(authorizedKeys), 0)
def CryptosignPrincipalStartAuthorizedKeysVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CryptosignPrincipalEnd(builder): return builder.EndObject()
