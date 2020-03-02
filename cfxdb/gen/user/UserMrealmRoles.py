# automatically generated by the FlatBuffers compiler, do not modify

# namespace: user

import flatbuffers

# /// CFC user roles on a management realm
class UserMrealmRoles(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsUserMrealmRoles(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserMrealmRoles()
        x.Init(buf, n + offset)
        return x

    # UserMrealmRoles
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

# /// List of roles the user has on the respective mrealm.
    # UserMrealmRoles
    def Roles(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # UserMrealmRoles
    def RolesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int8Flags, o)
        return 0

    # UserMrealmRoles
    def RolesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def UserMrealmRolesStart(builder): builder.StartObject(1)
def UserMrealmRolesAddRoles(builder, roles): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(roles), 0)
def UserMrealmRolesStartRolesVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def UserMrealmRolesEnd(builder): return builder.EndObject()