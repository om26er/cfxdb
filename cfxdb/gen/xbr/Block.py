# automatically generated by the FlatBuffers compiler, do not modify

# namespace: xbr

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# This table stores information about the series of Ethereum blocks that make up the blockchain.
class Block(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsBlock(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Block()
        x.Init(buf, n + offset)
        return x

    # Block
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Timestamp when record was inserted (Unix epoch time in ns)
    # Block
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Primary key: block number.
    # Block
    def BlockNumber(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Block
    def BlockNumberAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Block
    def BlockNumberLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Block
    def BlockNumberIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # Block hash.
    # Block
    def BlockHash(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Block
    def BlockHashAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Block
    def BlockHashLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Block
    def BlockHashIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # Number of XBR blockchain log events found in the block.
    # Block
    def CntEvents(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def BlockStart(builder): builder.StartObject(4)
def BlockAddTimestamp(builder, timestamp): builder.PrependUint64Slot(0, timestamp, 0)
def BlockAddBlockNumber(builder, blockNumber): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(blockNumber), 0)
def BlockStartBlockNumberVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def BlockAddBlockHash(builder, blockHash): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(blockHash), 0)
def BlockStartBlockHashVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def BlockAddCntEvents(builder, cntEvents): builder.PrependUint32Slot(3, cntEvents, 0)
def BlockEnd(builder): return builder.EndObject()
