# automatically generated by the FlatBuffers compiler, do not modify

# namespace: arealm

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TicketPrincipal(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTicketPrincipal(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TicketPrincipal()
        x.Init(buf, n + offset)
        return x

    # TicketPrincipal
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ID of this object.
    # TicketPrincipal
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
    # TicketPrincipal
    def Authid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ID of the application realm the authenticated principal will be joined to.
    # TicketPrincipal
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
    # TicketPrincipal
    def RoleOid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # WAMP-ticket specific stuff:
    # TicketPrincipal
    def Ticket(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def TicketPrincipalStart(builder): builder.StartObject(5)
def TicketPrincipalAddOid(builder, oid): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(oid), 0)
def TicketPrincipalAddAuthid(builder, authid): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(authid), 0)
def TicketPrincipalAddArealmOid(builder, arealmOid): builder.PrependStructSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(arealmOid), 0)
def TicketPrincipalAddRoleOid(builder, roleOid): builder.PrependStructSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(roleOid), 0)
def TicketPrincipalAddTicket(builder, ticket): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(ticket), 0)
def TicketPrincipalEnd(builder): return builder.EndObject()
