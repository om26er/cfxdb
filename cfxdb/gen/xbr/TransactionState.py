# automatically generated by the FlatBuffers compiler, do not modify

# namespace: xbr

# State of a XBR transaction.
class TransactionState(object):
    # Unset
    NONE = 0
    # The transaction is currently in-flight
    INFLIGHT = 1
    # The transaction has completed with error (it failed)
    FAILED = 2
    # The transaction has completed with success
    SUCCESS = 3

