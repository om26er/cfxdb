# automatically generated by the FlatBuffers compiler, do not modify

# namespace: xbr

# /// State of a XBR paying channel request.
class PayingChannelRequestState(object):
# /// Unset
    NONE = 0
# /// The paying channel request is newly created
    CREATED = 1
# /// The paying channel request has succeeded and a payment channel contract associated.
    ASSOCIATED = 2
# /// The paying channel request has failed (or will not be re-tried).
    FAILED = 3
