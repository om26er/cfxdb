# automatically generated by the FlatBuffers compiler, do not modify

# namespace: meta

import flatbuffers

class Reaction(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsReaction(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Reaction()
        x.Init(buf, n + offset)
        return x

    # Reaction
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def ReactionStart(builder): builder.StartObject(0)
def ReactionEnd(builder): return builder.EndObject()