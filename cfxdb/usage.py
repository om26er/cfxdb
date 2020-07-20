##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import pprint
import uuid

import flatbuffers
import numpy as np

from txaio import time_ns

from .gen.log import MasterNodeUsage as MasterNodeUsageGen


class _MasterNodeUsage(MasterNodeUsageGen.MasterNodeUsage):
    """
    Expand methods on the class code generated by flatc.

    FIXME: comes up with a PR for flatc to generated this stuff automatically.
    """
    @classmethod
    def GetRootAsMasterNodeUsage(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = _MasterNodeUsage()
        x.Init(buf, n + offset)
        return x

    def MrealmIdAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def PubkeyAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def ClientIpAddressAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def MeteringIdAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None


class MasterNodeUsage(object):
    """
    Persisted master node metering record database object.
    """
    def __init__(self, from_fbs=None):
        self._from_fbs = from_fbs

        self._timestamp = None
        self._mrealm_id = None
        self._timestamp_from = None
        self._pubkey = None
        self._client_ip_address = None
        self._client_ip_version = None
        self._client_ip_port = None
        self._seq = None
        self._sent = None
        self._processed = None
        self._status = None
        self._status_message = None
        self._metering_id = None

        self._count = None
        self._total = None
        self._nodes = None

        self._controllers = None
        self._hostmonitors = None
        self._routers = None
        self._containers = None
        self._guests = None
        self._proxies = None
        self._marketmakers = None

        self._sessions = None

        self._msgs_call = None
        self._msgs_yield = None
        self._msgs_invocation = None
        self._msgs_result = None
        self._msgs_error = None
        self._msgs_publish = None
        self._msgs_published = None
        self._msgs_event = None
        self._msgs_register = None
        self._msgs_registered = None
        self._msgs_subscribe = None
        self._msgs_subscribed = None

    def marshal(self):
        obj = {
            'timestamp': int(self.timestamp) if self.timestamp else None,
            'mrealm_id': str(self.mrealm_id) if self.mrealm_id else None,
            'timestamp_from': int(self.timestamp_from) if self.timestamp_from else None,
            'pubkey': bytes(self.pubkey) if self.pubkey else None,
            'client_ip_address': bytes(self.client_ip_address) if self.client_ip_address else None,
            'client_ip_version': self.client_ip_version,
            'client_ip_port': self.client_ip_port,
            'seq': self.seq,
            'sent': int(self.sent) if self.sent else None,
            'processed': int(self.processed) if self.processed else None,
            'status': self.status,
            'status_message': self.status_message,
            'metering_id': str(self.metering_id) if self.metering_id else None,
            'count': self.count,
            'total': self.total,
            'nodes': self.nodes,
            'controllers': self.controllers,
            'hostmonitors': self.hostmonitors,
            'routers': self.routers,
            'containers': self.containers,
            'guests': self.guests,
            'proxies': self.proxies,
            'marketmakers': self.marketmakers,
            'sessions': self.sessions,
            'msgs_call': self.msgs_call,
            'msgs_yield': self.msgs_yield,
            'msgs_invocation': self.msgs_invocation,
            'msgs_result': self.msgs_result,
            'msgs_error': self.msgs_error,
            'msgs_publish': self.msgs_publish,
            'msgs_published': self.msgs_published,
            'msgs_event': self.msgs_event,
            'msgs_register': self.msgs_register,
            'msgs_registered': self.msgs_registered,
            'msgs_subscribe': self.msgs_subscribe,
            'msgs_subscribed': self.msgs_subscribed,
        }
        return obj

    @staticmethod
    def parse(data):
        assert type(data) == dict, 'data parsed must have type dict, but was "{}"'.format(type(data))
        obj = MasterNodeUsage()

        timestamp = data.get('timestamp', None)
        assert timestamp is None or type(
            timestamp) == int, '"timestamp" must have type int, but was "{}"'.format(type(timestamp))
        if timestamp is None:
            # set current time as default
            obj._timestamp = np.datetime64(time_ns(), 'ns')
        else:
            # set the value contained in the parsed data
            obj._timestamp = np.datetime64(timestamp, 'ns')

        timestamp_from = data.get('timestamp_from', None)
        assert timestamp_from is None or type(
            timestamp_from) == int, '"timestamp_from" must have type int, but was "{}"'.format(
                type(timestamp_from))
        obj._timestamp_from = np.datetime64(timestamp_from, 'ns') if timestamp_from is not None else None

        mrealm_id = data.get('mrealm_id', None)
        assert mrealm_id is None or type(
            mrealm_id) == str, '"mrealm_id" must have type str, but was "{}"'.format(type(mrealm_id))
        if mrealm_id:
            obj._mrealm_id = uuid.UUID(mrealm_id)

        metering_id = data.get('metering_id', None)
        assert metering_id is None or type(
            metering_id) == str, '"metering_id" must have type str, but was "{}"'.format(type(metering_id))
        if metering_id:
            obj._metering_id = uuid.UUID(metering_id)

        pubkey = data.get('pubkey', None)
        assert pubkey is None or type(pubkey) == bytes and len(
            pubkey) == 32, '"pubkey" must have type bytes of length 32, but was "{}" of length {}'.format(
                type(pubkey),
                len(pubkey) if type(pubkey) == bytes else None)
        obj._pubkey = pubkey

        client_ip_address = data.get('client_ip_address', None)
        assert client_ip_address is None or type(client_ip_address) == bytes and len(client_ip_address) in [
            4, 16
        ], '"client_ip_address" must have type bytes of length 4 or 16, but was "{}" of length {}'.format(
            type(client_ip_address),
            len(client_ip_address) if type(client_ip_address) == bytes else None)
        obj._client_ip_address = client_ip_address

        client_ip_version = data.get('client_ip_version', None)
        assert client_ip_version is None or client_ip_version == 0 or (
            type(client_ip_version) == int and client_ip_version in [4, 6]
        ), '"client_ip_version" must have value [4, 6], but was "{}"'.format(client_ip_version)
        obj._client_ip_version = client_ip_version

        client_ip_port = data.get('client_ip_port', None)
        assert client_ip_port is None or client_ip_port == 0 or (
            type(client_ip_port) == int and client_ip_port in range(
                2**16)), '"client_ip_port" must have value [0, 2**16[, but was "{}"'.format(client_ip_port)
        obj._client_ip_port = client_ip_port

        seq = data.get('seq', None)
        assert seq is None or type(seq) == int, '"seq" must have type int, but was "{}"'.format(type(seq))
        obj._seq = seq

        sent = data.get('sent', None)
        assert sent is None or type(sent) == int, '"sent" must have type int, but was "{}"'.format(type(sent))
        if sent is not None:
            obj._sent = np.datetime64(sent, 'ns') if sent else None

        processed = data.get('processed', None)
        assert processed is None or type(
            processed) == int, '"processed" must have type int, but was "{}"'.format(type(processed))
        obj._processed = np.datetime64(processed, 'ns') if processed else None

        status = data.get('status', 0)
        assert status is None or (type(status) == int
                                  and status in range(4)), '"status" must have type int, but was "{}"'.format(
                                      type(status))
        obj._status = status

        status_message = data.get('status_message', None)
        assert status_message is None or type(
            status_message) == str, '"status_message" must have type str, but was "{}"'.format(
                type(status_message))
        obj._status_message = status_message

        # metering data:

        count = data.get('count', None)
        assert count is None or type(count) == int
        obj._count = count

        total = data.get('total', None)
        assert total is None or type(total) == int
        obj._total = total

        nodes = data.get('nodes', None)
        assert nodes is None or type(nodes) == int
        obj._nodes = nodes

        controllers = data.get('controllers', None)
        assert controllers is None or type(controllers) == int
        obj._controllers = controllers

        hostmonitors = data.get('hostmonitors', None)
        assert hostmonitors is None or type(hostmonitors) == int
        obj._hostmonitors = hostmonitors

        routers = data.get('routers', None)
        assert routers is None or type(routers) == int
        obj._routers = routers

        containers = data.get('containers', None)
        assert containers is None or type(containers) == int
        obj._containers = containers

        guests = data.get('guests', None)
        assert guests is None or type(guests) == int
        obj._guests = guests

        proxies = data.get('proxies', None)
        assert proxies is None or type(proxies) == int
        obj._proxies = proxies

        marketmakers = data.get('marketmakers', None)
        assert marketmakers is None or type(marketmakers) == int
        obj._marketmakers = marketmakers

        sessions = data.get('sessions', None)
        assert sessions is None or type(sessions) == int
        obj._sessions = sessions

        msgs_call = data.get('msgs_call', None)
        assert msgs_call is None or type(msgs_call) == int
        obj._msgs_call = msgs_call

        msgs_yield = data.get('msgs_yield', None)
        assert msgs_yield is None or type(msgs_yield) == int
        obj._msgs_yield = msgs_yield

        msgs_invocation = data.get('msgs_invocation', None)
        assert msgs_invocation is None or type(msgs_invocation) == int
        obj._msgs_invocation = msgs_invocation

        msgs_result = data.get('msgs_result', None)
        assert msgs_result is None or type(msgs_result) == int
        obj._msgs_result = msgs_result

        msgs_error = data.get('msgs_error', None)
        assert msgs_error is None or type(msgs_error) == int
        obj._msgs_error = msgs_error

        msgs_publish = data.get('msgs_publish', None)
        assert msgs_publish is None or type(msgs_publish) == int
        obj._msgs_publish = msgs_publish

        msgs_published = data.get('msgs_published', None)
        assert msgs_published is None or type(msgs_published) == int
        obj._msgs_published = msgs_published

        msgs_event = data.get('msgs_event', None)
        assert msgs_event is None or type(msgs_event) == int
        obj._msgs_event = msgs_event

        msgs_register = data.get('msgs_register', None)
        assert msgs_register is None or type(msgs_register) == int
        obj._msgs_register = msgs_register

        msgs_registered = data.get('msgs_registered', None)
        assert msgs_registered is None or type(msgs_registered) == int
        obj._msgs_registered = msgs_registered

        msgs_subscribe = data.get('msgs_subscribe', None)
        assert msgs_subscribe is None or type(msgs_subscribe) == int
        obj._msgs_subscribe = msgs_subscribe

        msgs_subscribed = data.get('msgs_subscribed', None)
        assert msgs_subscribed is None or type(msgs_subscribed) == int
        obj._msgs_subscribed = msgs_subscribed

        return obj

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    @property
    def timestamp(self):
        if self._timestamp is None and self._from_fbs:
            self._timestamp = np.datetime64(self._from_fbs.Timestamp(), 'ns')
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        assert isinstance(value, np.datetime64)
        self._timestamp = value

    @property
    def timestamp_from(self):
        if self._timestamp_from is None and self._from_fbs:
            self._timestamp_from = np.datetime64(self._from_fbs.TimestampFrom(), 'ns')
        return self._timestamp_from

    @timestamp_from.setter
    def timestamp_from(self, value):
        assert isinstance(value, np.datetime64)
        self._timestamp_from = value

    @property
    def mrealm_id(self):
        if self._mrealm_id is None and self._from_fbs:
            if self._from_fbs.MrealmIdLength():
                _mrealm_id = self._from_fbs.MrealmIdAsBytes()
                if _mrealm_id:
                    self._mrealm_id = uuid.UUID(bytes=bytes(_mrealm_id))
        return self._mrealm_id

    @mrealm_id.setter
    def mrealm_id(self, value):
        assert value is None or isinstance(value, uuid.UUID)
        self._mrealm_id = value

    @property
    def metering_id(self):
        if self._metering_id is None and self._from_fbs:
            if self._from_fbs.MeteringIdLength():
                _metering_id = self._from_fbs.MeteringIdAsBytes()
                if _metering_id:
                    self._metering_id = uuid.UUID(bytes=bytes(_metering_id))
        return self._metering_id

    @metering_id.setter
    def metering_id(self, value):
        assert value is None or isinstance(value, uuid.UUID)
        self._metering_id = value

    @property
    def pubkey(self):
        if self._pubkey is None and self._from_fbs:
            if self._from_fbs.PubkeyLength():
                self._pubkey = self._from_fbs.PubkeyAsBytes()
        return self._pubkey

    @pubkey.setter
    def pubkey(self, value):
        assert value is None or (type(value) == bytes and len(value) == 32)
        self._pubkey = value

    @property
    def client_ip_address(self):
        if self._client_ip_address is None and self._from_fbs:
            if self._from_fbs.ClientIpAddressLength():
                self._client_ip_address = self._from_fbs.ClientIpAddressAsBytes()
        return self._client_ip_address

    @client_ip_address.setter
    def client_ip_address(self, value):
        assert value is None or (type(value) == bytes and len(value) in [4, 16])
        self._client_ip_address = value

    @property
    def client_ip_version(self):
        if self._client_ip_version is None and self._from_fbs:
            self._client_ip_version = self._from_fbs.ClientIpVersion()
        return self._client_ip_version

    @client_ip_version.setter
    def client_ip_version(self, value):
        assert value is None or (type(value) == int and value in [4, 6])
        self._client_ip_version = value

    @property
    def client_ip_port(self):
        if self._client_ip_port is None and self._from_fbs:
            self._client_ip_port = self._from_fbs.ClientIpPort()
        return self._client_ip_port

    @client_ip_port.setter
    def client_ip_port(self, value):
        assert value is None or (type(value) == int and value in range(2**16))
        self._client_ip_port = value

    @property
    def seq(self):
        if self._seq is None and self._from_fbs:
            self._seq = self._from_fbs.Seq()
        return self._seq

    @seq.setter
    def seq(self, value):
        assert value is None or type(value) == int
        self._seq = value

    @property
    def sent(self):
        if self._sent is None and self._from_fbs:
            self._sent = np.datetime64(self._from_fbs.Sent(), 'ns')
        return self._sent

    @sent.setter
    def sent(self, value):
        assert value is None or isinstance(value, np.datetime64)
        self._sent = value

    @property
    def processed(self):
        if self._processed is None and self._from_fbs:
            self._processed = np.datetime64(self._from_fbs.Processed(), 'ns')
        return self._processed

    @processed.setter
    def processed(self, value):
        assert value is None or isinstance(value, np.datetime64)
        self._processed = value

    @property
    def status(self):
        if self._status is None and self._from_fbs:
            self._status = self._from_fbs.Status()
        return self._status

    @status.setter
    def status(self, value):
        assert value is None or (type(value) == int and value in range(4))
        self._status = value

    @property
    def status_message(self):
        if self._status_message is None and self._from_fbs:
            status_message = self._from_fbs.StatusMessage()
            if status_message:
                self._status_message = status_message.decode('utf8')
        return self._status_message

    @status_message.setter
    def status_message(self, value):
        assert value is None or type(value) == str
        self._status_message = value

    @property
    def count(self):
        if self._count is None and self._from_fbs:
            self._count = self._from_fbs.Count()
        return self._count

    @count.setter
    def count(self, value):
        assert value is None or type(value) == int
        self._count = value

    @property
    def total(self):
        if self._total is None and self._from_fbs:
            self._total = self._from_fbs.Total()
        return self._total

    @total.setter
    def total(self, value):
        assert value is None or type(value) == int
        self._total = value

    @property
    def nodes(self):
        if self._nodes is None and self._from_fbs:
            self._nodes = self._from_fbs.Nodes()
        return self._nodes

    @nodes.setter
    def nodes(self, value):
        assert value is None or type(value) == int
        self._nodes = value

    @property
    def controllers(self):
        if self._controllers is None and self._from_fbs:
            self._controllers = self._from_fbs.Controllers()
        return self._controllers

    @controllers.setter
    def controllers(self, value):
        assert value is None or type(value) == int
        self._controllers = value

    @property
    def hostmonitors(self):
        if self._hostmonitors is None and self._from_fbs:
            self._hostmonitors = self._from_fbs.Hostmonitors()
        return self._hostmonitors

    @hostmonitors.setter
    def hostmonitors(self, value):
        assert value is None or type(value) == int
        self._hostmonitors = value

    @property
    def routers(self):
        if self._routers is None and self._from_fbs:
            self._routers = self._from_fbs.Routers()
        return self._routers

    @routers.setter
    def routers(self, value):
        assert value is None or type(value) == int
        self._routers = value

    @property
    def containers(self):
        if self._containers is None and self._from_fbs:
            self._containers = self._from_fbs.Containers()
        return self._containers

    @containers.setter
    def containers(self, value):
        assert value is None or type(value) == int
        self._containers = value

    @property
    def guests(self):
        if self._guests is None and self._from_fbs:
            self._guests = self._from_fbs.Guests()
        return self._guests

    @guests.setter
    def guests(self, value):
        assert value is None or type(value) == int
        self._guests = value

    @property
    def proxies(self):
        if self._proxies is None and self._from_fbs:
            self._proxies = self._from_fbs.Proxies()
        return self._proxies

    @proxies.setter
    def proxies(self, value):
        assert value is None or type(value) == int
        self._proxies = value

    @property
    def marketmakers(self):
        if self._marketmakers is None and self._from_fbs:
            self._marketmakers = self._from_fbs.Marketmakers()
        return self._marketmakers

    @marketmakers.setter
    def marketmakers(self, value):
        assert value is None or type(value) == int
        self._marketmakers = value

    @property
    def sessions(self):
        if self._sessions is None and self._from_fbs:
            self._sessions = self._from_fbs.Sessions()
        return self._sessions

    @sessions.setter
    def sessions(self, value):
        assert value is None or type(value) == int
        self._sessions = value

    @property
    def msgs_call(self):
        if self._msgs_call is None and self._from_fbs:
            self._msgs_call = self._from_fbs.MsgsCall()
        return self._msgs_call

    @msgs_call.setter
    def msgs_call(self, value):
        assert value is None or type(value) == int
        self._msgs_call = value

    @property
    def msgs_yield(self):
        if self._msgs_yield is None and self._from_fbs:
            self._msgs_yield = self._from_fbs.MsgsYield()
        return self._msgs_yield

    @msgs_yield.setter
    def msgs_yield(self, value):
        assert value is None or type(value) == int
        self._msgs_yield = value

    @property
    def msgs_invocation(self):
        if self._msgs_invocation is None and self._from_fbs:
            self._msgs_invocation = self._from_fbs.MsgsInvocation()
        return self._msgs_invocation

    @msgs_invocation.setter
    def msgs_invocation(self, value):
        assert value is None or type(value) == int
        self._msgs_invocation = value

    @property
    def msgs_result(self):
        if self._msgs_result is None and self._from_fbs:
            self._msgs_result = self._from_fbs.MsgsResult()
        return self._msgs_result

    @msgs_result.setter
    def msgs_result(self, value):
        assert value is None or type(value) == int
        self._msgs_result = value

    @property
    def msgs_error(self):
        if self._msgs_error is None and self._from_fbs:
            self._msgs_error = self._from_fbs.MsgsError()
        return self._msgs_error

    @msgs_error.setter
    def msgs_error(self, value):
        assert value is None or type(value) == int
        self._msgs_error = value

    @property
    def msgs_publish(self):
        if self._msgs_publish is None and self._from_fbs:
            self._msgs_publish = self._from_fbs.MsgsPublish()
        return self._msgs_publish

    @msgs_publish.setter
    def msgs_publish(self, value):
        assert value is None or type(value) == int
        self._msgs_publish = value

    @property
    def msgs_published(self):
        if self._msgs_published is None and self._from_fbs:
            self._msgs_published = self._from_fbs.MsgsPublished()
        return self._msgs_published

    @msgs_published.setter
    def msgs_published(self, value):
        assert value is None or type(value) == int
        self._msgs_published = value

    @property
    def msgs_event(self):
        if self._msgs_event is None and self._from_fbs:
            self._msgs_event = self._from_fbs.MsgsEvent()
        return self._msgs_event

    @msgs_event.setter
    def msgs_event(self, value):
        assert value is None or type(value) == int
        self._msgs_event = value

    @property
    def msgs_register(self):
        if self._msgs_register is None and self._from_fbs:
            self._msgs_register = self._from_fbs.MsgsRegister()
        return self._msgs_register

    @msgs_register.setter
    def msgs_register(self, value):
        assert value is None or type(value) == int
        self._msgs_register = value

    @property
    def msgs_registered(self):
        if self._msgs_registered is None and self._from_fbs:
            self._msgs_registered = self._from_fbs.MsgsRegistered()
        return self._msgs_registered

    @msgs_registered.setter
    def msgs_registered(self, value):
        assert value is None or type(value) == int
        self._msgs_registered = value

    @property
    def msgs_subscribe(self):
        if self._msgs_subscribe is None and self._from_fbs:
            self._msgs_subscribe = self._from_fbs.MsgsSubscribe()
        return self._msgs_subscribe

    @msgs_subscribe.setter
    def msgs_subscribe(self, value):
        assert value is None or type(value) == int
        self._msgs_subscribe = value

    @property
    def msgs_subscribed(self):
        if self._msgs_subscribed is None and self._from_fbs:
            self._msgs_subscribed = self._from_fbs.MsgsSubscribed()
        return self._msgs_subscribed

    @msgs_subscribed.setter
    def msgs_subscribed(self, value):
        assert value is None or type(value) == int
        self._msgs_subscribed = value

    @staticmethod
    def cast(buf):
        return MasterNodeUsage(_MasterNodeUsage.GetRootAsMasterNodeUsage(buf, 0))

    def build(self, builder):

        mrealm_id = self.mrealm_id.bytes if self.mrealm_id else None
        if mrealm_id:
            mrealm_id = builder.CreateString(mrealm_id)

        pubkey = self.pubkey
        if pubkey:
            pubkey = builder.CreateString(bytes(pubkey))

        client_ip_address = self.client_ip_address
        if client_ip_address:
            client_ip_address = builder.CreateString(bytes(client_ip_address))

        status_message = self.status_message
        if status_message:
            status_message = builder.CreateString(status_message)

        metering_id = self.metering_id.bytes if self.metering_id else None
        if metering_id:
            metering_id = builder.CreateString(metering_id)

        MasterNodeUsageGen.MasterNodeUsageStart(builder)

        if self.timestamp is not None:
            MasterNodeUsageGen.MasterNodeUsageAddTimestamp(builder, self.timestamp.astype('long'))

        if mrealm_id:
            MasterNodeUsageGen.MasterNodeUsageAddMrealmId(builder, mrealm_id)

        if self.timestamp_from is not None:
            MasterNodeUsageGen.MasterNodeUsageAddTimestampFrom(builder, self.timestamp_from.astype('long'))

        if pubkey:
            MasterNodeUsageGen.MasterNodeUsageAddPubkey(builder, pubkey)

        if client_ip_address:
            MasterNodeUsageGen.MasterNodeUsageAddClientIpAddress(builder, client_ip_address)

        if self.client_ip_version:
            MasterNodeUsageGen.MasterNodeUsageAddClientIpVersion(builder, self.client_ip_version)

        if self.client_ip_port:
            MasterNodeUsageGen.MasterNodeUsageAddClientIpPort(builder, self.client_ip_port)

        if self.seq:
            MasterNodeUsageGen.MasterNodeUsageAddSeq(builder, self.seq)

        if self.sent is not None:
            MasterNodeUsageGen.MasterNodeUsageAddSent(builder, self.sent.astype('long'))

        if self.processed is not None:
            MasterNodeUsageGen.MasterNodeUsageAddProcessed(builder, self.processed.astype('long'))

        if self.status:
            MasterNodeUsageGen.MasterNodeUsageAddStatus(builder, self.status)

        if status_message:
            MasterNodeUsageGen.MasterNodeUsageAddStatusMessage(builder, status_message)

        if metering_id:
            MasterNodeUsageGen.MasterNodeUsageAddMeteringId(builder, metering_id)

        if self.count:
            MasterNodeUsageGen.MasterNodeUsageAddCount(builder, self.count)

        if self.total:
            MasterNodeUsageGen.MasterNodeUsageAddTotal(builder, self.total)

        if self.nodes:
            MasterNodeUsageGen.MasterNodeUsageAddNodes(builder, self.nodes)

        if self.controllers:
            MasterNodeUsageGen.MasterNodeUsageAddControllers(builder, self.controllers)

        if self.hostmonitors:
            MasterNodeUsageGen.MasterNodeUsageAddHostmonitors(builder, self.hostmonitors)

        if self.routers:
            MasterNodeUsageGen.MasterNodeUsageAddRouters(builder, self.routers)

        if self.containers:
            MasterNodeUsageGen.MasterNodeUsageAddContainers(builder, self.containers)

        if self.guests:
            MasterNodeUsageGen.MasterNodeUsageAddGuests(builder, self.guests)

        if self.proxies:
            MasterNodeUsageGen.MasterNodeUsageAddProxies(builder, self.proxies)

        if self.marketmakers:
            MasterNodeUsageGen.MasterNodeUsageAddMarketmakers(builder, self.marketmakers)

        if self.sessions:
            MasterNodeUsageGen.MasterNodeUsageAddSessions(builder, self.sessions)

        if self.msgs_call:
            MasterNodeUsageGen.MasterNodeUsageAddMsgsCall(builder, self.msgs_call)

        if self.msgs_yield:
            MasterNodeUsageGen.MasterNodeUsageAddMsgsYield(builder, self.msgs_yield)

        if self.msgs_invocation:
            MasterNodeUsageGen.MasterNodeUsageAddMsgsInvocation(builder, self.msgs_invocation)

        if self.msgs_result:
            MasterNodeUsageGen.MasterNodeUsageAddMsgsResult(builder, self.msgs_result)

        if self.msgs_error:
            MasterNodeUsageGen.MasterNodeUsageAddMsgsError(builder, self.msgs_error)

        if self.msgs_publish:
            MasterNodeUsageGen.MasterNodeUsageAddMsgsPublish(builder, self.msgs_publish)

        if self.msgs_published:
            MasterNodeUsageGen.MasterNodeUsageAddMsgsPublished(builder, self.msgs_published)

        if self.msgs_event:
            MasterNodeUsageGen.MasterNodeUsageAddMsgsEvent(builder, self.msgs_event)

        if self.msgs_register:
            MasterNodeUsageGen.MasterNodeUsageAddMsgsRegister(builder, self.msgs_register)

        if self.msgs_registered:
            MasterNodeUsageGen.MasterNodeUsageAddMsgsRegistered(builder, self.msgs_registered)

        if self.msgs_subscribe:
            MasterNodeUsageGen.MasterNodeUsageAddMsgsSubscribe(builder, self.msgs_subscribe)

        if self.msgs_subscribed:
            MasterNodeUsageGen.MasterNodeUsageAddMsgsSubscribed(builder, self.msgs_subscribed)

        final = MasterNodeUsageGen.MasterNodeUsageEnd(builder)

        return final
