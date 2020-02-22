# automatically generated by the FlatBuffers compiler, do not modify

# namespace: xbr

import flatbuffers

# /// XBR payment channel current (off-chain) balance. The sum of ``Balance.remaining`` and ``Balance.inflight`` equals ``PaymentChannel.amount``.
class PaymentChannelBalance(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPaymentChannelBalance(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PaymentChannelBalance()
        x.Init(buf, n + offset)
        return x

    # PaymentChannelBalance
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

# /// Amount of XBR tokens currently remaining in the payment channel.
    # PaymentChannelBalance
    def Remaining(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # PaymentChannelBalance
    def RemainingAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # PaymentChannelBalance
    def RemainingLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

# /// Amount of XBR tokens reserved to in-flight purchase transactions.
    # PaymentChannelBalance
    def Inflight(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # PaymentChannelBalance
    def InflightAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # PaymentChannelBalance
    def InflightLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

# /// Sequence number of transactions on this balance starting from 0 when the payment channel is created.
    # PaymentChannelBalance
    def Seq(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def PaymentChannelBalanceStart(builder): builder.StartObject(3)
def PaymentChannelBalanceAddRemaining(builder, remaining): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(remaining), 0)
def PaymentChannelBalanceStartRemainingVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def PaymentChannelBalanceAddInflight(builder, inflight): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(inflight), 0)
def PaymentChannelBalanceStartInflightVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def PaymentChannelBalanceAddSeq(builder, seq): builder.PrependUint32Slot(2, seq, 0)
def PaymentChannelBalanceEnd(builder): return builder.EndObject()