# automatically generated by the FlatBuffers compiler, do not modify

# namespace: arealm

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# Association (N:M) between principals and authenticators, both defined independently at the management realm level.
class AuthenticatorPrincipal(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsAuthenticatorPrincipal(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AuthenticatorPrincipal()
        x.Init(buf, n + offset)
        return x

    # AuthenticatorPrincipal
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ID of the principal (which must match in type with the authenticator).
    # AuthenticatorPrincipal
    def PrincipalOid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ID of the authenticator the principal is associated with.
    # AuthenticatorPrincipal
    def AuthenticatorOid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def AuthenticatorPrincipalStart(builder): builder.StartObject(2)
def AuthenticatorPrincipalAddPrincipalOid(builder, principalOid): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(principalOid), 0)
def AuthenticatorPrincipalAddAuthenticatorOid(builder, authenticatorOid): builder.PrependStructSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(authenticatorOid), 0)
def AuthenticatorPrincipalEnd(builder): return builder.EndObject()
