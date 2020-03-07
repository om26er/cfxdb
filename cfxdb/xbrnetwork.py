# XBR Network - Copyright (c) Crossbar.io Technologies GmbH. All rights reserved.

import uuid
import pprint

import cbor2
import flatbuffers
import numpy as np

from zlmdb import table, MapUuidFlatBuffers, MapStringUuid, MapBytes32FlatBuffers, MapBytes20Uuid,\
    MapUuidTimestampBytes32
from autobahn.xbr import pack_uint256, unpack_uint256

from .gen.xbrnetwork import Account as AccountGen
from .gen.xbrnetwork import VerifiedAction as VerifiedActionGen
from .gen.xbrnetwork import UserKey as UserKeyGen

# FIXME: https://github.com/crossbario/crossbarfx/issues/501
from cfxdb import Blocks, TokenApprovals, TokenTransfers, Members, Markets, IndexMarketsByOwner,\
    Actors, IndexMarketsByActor, Attributes


class _AccountGen(AccountGen.Account):
    """
    Expand methods on the class code generated by flatc.

    FIXME: come up with a PR for flatc to generated this stuff automatically.
    """
    @classmethod
    def GetRootAsAccount(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = _AccountGen()
        x.Init(buf, n + offset)
        return x

    def OidAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def WalletAddressAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def RegisteredAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None


class Account(object):
    """
    XBR Network members.
    """

    ACCOUNT_LEVEL_NONE = 0
    """
    Unset.
    """

    ACCOUNT_LEVEL_ACTIVE = 1
    """
    Account is active.
    """

    ACCOUNT_LEVEL_VERIFIED = 2
    """
    Account is active and verified.
    """

    ACCOUNT_LEVEL_RETIRED = 3
    """
    Account is retired.
    """

    ACCOUNT_LEVEL_PENALTY = 4
    """
    Account is subject to a temporary penalty.
    """

    ACCOUNT_LEVEL_BLOCKED = 5
    """
    Account is currently blocked and cannot current actively participate in the market.
    """

    ACCOUNT_LEVEL = list(range(6))
    """
    Valid account levels.
    """

    WALLET_TYPE_NONE = 0
    """
    Wallet type unset ("null").
    """

    WALLET_TYPE_IMPORTED = 1
    """
    Account (primary) wallet was imported (the user provided the wallet public address).
    """

    WALLET_TYPE_METAMASK = 2
    """
    Account (primary) wallet was imported (the user provided the wallet public address).
    """

    WALLET_TYPE_HOSTED = 3
    """
    Account wallet in hosted (in this database).
    """

    WALLET_TYPE = list(range(4))
    """
    Valid account wallet types.
    """

    WALLET_TYPE_TO_STRING = {
        0: 'none',
        1: 'imported',
        2: 'metamask',
        3: 'hosted',
    }
    """
    Map of ``wallet-type-code`` to ``wallet-type-name``.
    """

    WALLET_TYPE_FROM_STRING = {
        'none': 0,
        'imported': 1,
        'metamask': 2,
        'hosted': 3,
    }
    """
    Map of ``wallet-type-name`` to ``wallet-type-code``.
    """
    def __init__(self, from_fbs=None):
        self._from_fbs = from_fbs

        # Globally unique and static member ID.
        # [uint8] (uuid)
        self._oid = None

        # Timestamp (epoch time in ns) of initial creation of this record.
        # uint64 (timestamp)
        self._created = None

        # XBR Network username (must be globall unique on https://xbr.network)
        # string
        self._username = None

        # User (primary) email address.
        # string
        self._email = None

        # Timestamp (epoch time in ns) when the user email was (last) verified or 0 if unverified.
        # uint64 (timestamp)
        self._email_verified = None

        # Type of (primary) user crypto wallet in use.
        # WalletType
        self._wallet_type = None

        # Public address of user crypto wallet in use.
        # [uint8] (address)
        self._wallet_address = None

        # Block number (on the blockchain) when the member (originally) registered.
        # [uint8] (uint256)
        self._registered = None

        # EULA the member agreed to when joining the market (IPFS Multihash string).
        # string (multihash)
        self._eula = None

        # Optional member profile (IPFS Multihash string).
        # string (multihash)
        self._profile = None

        # Current member level.
        # AccountLevel
        self._level = None

    def marshal(self):
        obj = {
            'oid': self.oid,
            'created': self.created,
            'username': self.username,
            'email': self.email,
            'email_verified': self.email_verified,
            'wallet_type': self.wallet_type,
            'wallet_address': self.wallet_address,
            'registered': self.registered,
            'eula': self.eula,
            'profile': self.profile,
            'level': self.level,
        }
        return obj

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    @property
    def oid(self) -> uuid.UUID:
        """
        Globally unique and static member ID.
        """
        if self._oid is None and self._from_fbs:
            if self._from_fbs.OidLength():
                _oid = self._from_fbs.OidAsBytes()
                self._oid = uuid.UUID(bytes=bytes(_oid))
            else:
                self._oid = uuid.UUID(bytes=b'\x00' * 20)
        return self._oid

    @oid.setter
    def oid(self, value: uuid.UUID):
        assert value is None or isinstance(value, uuid.UUID)
        self._oid = value

    @property
    def created(self) -> np.datetime64:
        """
        Timestamp (epoch time in ns) of initial creation of this record.
        """
        if self._created is None and self._from_fbs:
            self._created = np.datetime64(self._from_fbs.Created(), 'ns')
        return self._created

    @created.setter
    def created(self, value: np.datetime64):
        assert value is None or isinstance(value, np.datetime64)
        self._created = value

    @property
    def username(self) -> str:
        """
        XBR Network username (must be globally unique on https://xbr.network)
        """
        if self._username is None and self._from_fbs:
            username = self._from_fbs.Username()
            if username:
                self._username = username.decode('utf8')
        return self._username

    @username.setter
    def username(self, value: str):
        assert value is None or type(value) == str
        self._username = value

    @property
    def email(self) -> str:
        """
        User (primary) email address.
        """
        if self._email is None and self._from_fbs:
            email = self._from_fbs.Email()
            if email:
                self._email = email.decode('utf8')
        return self._email

    @email.setter
    def email(self, value: str):
        assert value is None or type(value) == str
        self._email = value

    @property
    def email_verified(self) -> np.datetime64:
        """
        Timestamp (epoch time in ns) when the user email was (last) verified or 0 if unverified.
        """
        if self._email_verified is None and self._from_fbs:
            self._email_verified = np.datetime64(self._from_fbs.EmailVerified(), 'ns')
        return self._email_verified

    @email_verified.setter
    def email_verified(self, value: np.datetime64):
        assert value is None or isinstance(value, np.datetime64)
        self._email_verified = value

    @property
    def wallet_type(self) -> int:
        """
        Type of (primary) user crypto wallet in use.
        """
        if self._wallet_type is None and self._from_fbs:
            self._wallet_type = self._from_fbs.WalletType()
        return self._wallet_type or 0

    @wallet_type.setter
    def wallet_type(self, value: int):
        assert value is None or type(value) == int
        self._wallet_type = value

    @property
    def wallet_address(self) -> bytes:
        """
        Public address of user crypto wallet in use.
        """
        if self._wallet_address is None and self._from_fbs:
            if self._from_fbs.WalletAddressLength():
                self._wallet_address = self._from_fbs.WalletAddressAsBytes()
        return self._wallet_address

    @wallet_address.setter
    def wallet_address(self, value: bytes):
        assert value is None or (type(value) == bytes and len(value) == 20)
        self._wallet_address = value

    @property
    def registered(self) -> int:
        """
        Block number (on the blockchain) when the member (originally) registered.
        """
        if self._registered is None and self._from_fbs:
            if self._from_fbs.RegisteredLength():
                _registered = self._from_fbs.RegisteredAsBytes()
                self._registered = unpack_uint256(bytes(_registered))
            else:
                self._registered = 0
        return self._registered

    @registered.setter
    def registered(self, value: int):
        assert value is None or type(value) == int
        self._registered = value

    @property
    def eula(self) -> str:
        """
        EULA the member agreed to when joining the market (IPFS Multihash string).
        """
        if self._eula is None and self._from_fbs:
            eula = self._from_fbs.Eula()
            if eula:
                self._eula = eula.decode('utf8')
        return self._eula

    @eula.setter
    def eula(self, value: str):
        assert value is None or type(value) == str
        self._eula = value

    @property
    def profile(self) -> str:
        """
        Optional member profile (IPFS Multihash string).
        """
        if self._profile is None and self._from_fbs:
            profile = self._from_fbs.Profile()
            if profile:
                self._profile = profile.decode('utf8')
        return self._profile

    @profile.setter
    def profile(self, value: str):
        assert value is None or type(value) == str
        self._profile = value

    @property
    def level(self) -> int:
        """
        Current member level.
        """
        if self._level is None and self._from_fbs:
            self._level = self._from_fbs.Level()
        return self._level

    @level.setter
    def level(self, value: int):
        assert value is None or type(value) == int
        self._level = value

    @staticmethod
    def cast(buf):
        return Account(_AccountGen.GetRootAsAccount(buf, 0))

    def build(self, builder):

        oid = self.oid.bytes if self.oid else None
        if oid:
            oid = builder.CreateString(oid)

        username = self.username
        if username:
            username = builder.CreateString(username)

        email = self.email
        if email:
            email = builder.CreateString(email)

        wallet_address = self.wallet_address
        if wallet_address:
            wallet_address = builder.CreateString(wallet_address)

        registered = self.registered
        if registered:
            registered = builder.CreateString(pack_uint256(registered))

        eula = self.eula
        if eula:
            eula = builder.CreateString(eula)

        profile = self.profile
        if profile:
            profile = builder.CreateString(profile)

        AccountGen.AccountStart(builder)

        if oid:
            AccountGen.AccountAddOid(builder, oid)

        if self.created:
            AccountGen.AccountAddCreated(builder, int(self.created))

        if username:
            AccountGen.AccountAddUsername(builder, username)

        if email:
            AccountGen.AccountAddEmail(builder, email)

        if self.email_verified:
            AccountGen.AccountAddEmailVerified(builder, int(self.email_verified))

        if self.wallet_type:
            AccountGen.AccountAddWalletType(builder, self.wallet_type)

        if wallet_address:
            AccountGen.AccountAddWalletAddress(builder, wallet_address)

        if registered:
            AccountGen.AccountAddRegistered(builder, registered)

        if eula:
            AccountGen.AccountAddEula(builder, eula)

        if profile:
            AccountGen.AccountAddProfile(builder, profile)

        if self.level:
            AccountGen.AccountAddLevel(builder, self.level)

        final = AccountGen.AccountEnd(builder)

        return final


@table('d155dff2-ac36-4c69-b1b0-254ce2eb237d', build=Account.build, cast=Account.cast)
class Accounts(MapUuidFlatBuffers):
    """
    Database table for XBR member accounts.
    """


@table('760d42a0-110e-474b-ab85-6e2396af035d')
class IndexAccountsByUsername(MapStringUuid):
    """
    Database (index) table for username-to-account mapping.
    """


@table('76706b89-8639-491e-8989-afc5a7c8a5b4')
class IndexAccountsByEmail(MapStringUuid):
    """
    Database (index) table for (user-)email-to-account mapping.
    """


@table('432ae4fa-a23e-45d7-b2a4-c9ae868df2b3')
class IndexAccountsByWallet(MapBytes20Uuid):
    """
    Database (index) table for (user-)wallet-to-account mapping.
    """


class _VerifiedActionGen(VerifiedActionGen.VerifiedAction):
    """
    Expand methods on the class code generated by flatc.

    FIXME: come up with a PR for flatc to generated this stuff automatically.
    """
    @classmethod
    def GetRootAsVerifiedAction(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = _VerifiedActionGen()
        x.Init(buf, n + offset)
        return x

    def OidAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def VerifiedOidAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def VerifiedDataAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None


class VerificationType(object):

    NONE = 0
    """
    Unset
    """

    MEMBER_ONBOARD_EMAIL = 1
    """
    Member onboarded, using verification via member primary email.
    """

    MEMBER_LOGIN_EMAIL = 2
    """
    Member created a market, using verification via member primary email.
    """

    CREATE_MARKET_EMAIL = 3
    """
    Member joined a market, using verification via member primary email.
    """


class VerifiedAction(object):
    """
    User actions (such as "on-board new user") yet to be verified. Actions to be verified are
    identified using their "Verification Action ID". A verificatin email is sent to the (primary)
    email address of the user, and to verify, the user must click the verification link contained
    in the email. The verification link contains the verification action ID and code.
    """

    VERIFICATION_TYPE_NONE = 0
    """
    Unset verification action type ("null").
    """

    VERIFICATION_TYPE_ONBOARD_MEMBER = 1
    """
    Verification action type for on-boarding new members via email verification.
    """

    VERIFICATION_TYPE_LOGIN_MEMBER = 2
    """
    Verification action type for login of member (client) via email verification.
    """

    VERIFICATION_TYPE_CREATE_MARKET = 3
    """
    Verification action type for creation of new data market via email verification.
    """

    VERIFICATION_TYPE_JOIN_MARKET = 4
    """
    Verification action type for joining an existing market via email verification.
    """

    VERIFICATION_TYPE = list(range(5))
    """
    All valid verification action types.
    """

    VERIFICATION_STATUS_NONE = 0
    """
    Unset verification action status ("null").
    """

    VERIFICATION_STATUS_PENDING = 1
    """
    Verification is still pending.
    """

    VERIFICATION_STATUS_VERIFIED = 2
    """
    Verification has been successfully completed.
    """

    VERIFICATION_STATUS_FAILED = 3
    """
    Verification has failed.
    """

    VERIFICATION_STATUS_EXPIRED = 4
    """
    Action cannot be verified any longer since it has expired.
    """

    VERIFICATION_STATUS = list(range(5))
    """
    All valid verification status codes.
    """
    def __init__(self, from_fbs=None):
        self._from_fbs = from_fbs

        # Globally unique and static ID of action .
        # [uint8] (uuid)
        self._oid = None

        # Timestamp (epoch time in ns) of initial creation of this record.
        # uint64 (timestamp)
        self._created = None

        # Verification type.
        # VerificationType (uint8)
        self._vtype = None

        # Verification type.
        # VerificationStatus (uint8)
        self._vstatus = None

        # Verification code sent.
        # string
        self._vcode = None

        # ID of object of verified action.
        # [uint8] (uuid)
        self._verified_oid = None

        # Action data, serialized in CBOR.
        # [uint8]
        self._verified_data = None

    def marshal(self):
        obj = {
            'oid': self.oid,
            'created': self.created,
            'vtype': self.vtype,
            'vstatus': self.vstatus,
            'vcode': self.vcode,
            'verified_oid': self.verified_oid,
            'verified_data': self.verified_data,
        }
        return obj

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    @property
    def oid(self) -> uuid.UUID:
        """
        Globally unique and static ID of action.
        """
        if self._oid is None and self._from_fbs:
            if self._from_fbs.OidLength():
                _oid = self._from_fbs.OidAsBytes()
                self._oid = uuid.UUID(bytes=bytes(_oid))
            else:
                self._oid = uuid.UUID(bytes=b'\x00' * 20)
        return self._oid

    @oid.setter
    def oid(self, value: uuid.UUID):
        assert value is None or isinstance(value, uuid.UUID)
        self._oid = value

    @property
    def created(self) -> np.datetime64:
        """
        Timestamp (epoch time in ns) of initial creation of this record.
        """
        if self._created is None and self._from_fbs:
            self._created = np.datetime64(self._from_fbs.Created(), 'ns')
        return self._created

    @created.setter
    def created(self, value: np.datetime64):
        assert value is None or isinstance(value, np.datetime64)
        self._created = value

    @property
    def vtype(self) -> int:
        """
        Verification type.
        """
        if self._vtype is None and self._from_fbs:
            self._vtype = self._from_fbs.Vtype()
        return self._vtype or 0

    @vtype.setter
    def vtype(self, value: int):
        assert value is None or (type(value) == int and value in self.VERIFICATION_TYPE)
        self._vtype = value

    @property
    def vstatus(self) -> int:
        """
        Verification type.
        """
        if self._vstatus is None and self._from_fbs:
            self._vstatus = self._from_fbs.Vstatus()
        return self._vstatus or 0

    @vstatus.setter
    def vstatus(self, value: int):
        assert value is None or (type(value) == int and value in self.VERIFICATION_STATUS)
        self._vstatus = value

    @property
    def vcode(self) -> str:
        """
        Verification code sent.
        """
        if self._vcode is None and self._from_fbs:
            vcode = self._from_fbs.Vcode()
            if vcode:
                self._vcode = vcode.decode('utf8')
        return self._vcode

    @vcode.setter
    def vcode(self, value: str):
        assert value is None or type(value) == str
        self._vcode = value

    @property
    def verified_oid(self) -> uuid.UUID:
        """
        ID of object of verified action.
        """
        if self._verified_oid is None and self._from_fbs:
            if self._from_fbs.VerifiedOidLength():
                _verified_oid = self._from_fbs.VerifiedOidAsBytes()
                self._verified_oid = uuid.UUID(bytes=bytes(_verified_oid))
            else:
                self._verified_oid = uuid.UUID(bytes=b'\x00' * 16)
        return self._verified_oid

    @verified_oid.setter
    def verified_oid(self, value: uuid.UUID):
        assert value is None or isinstance(value, uuid.UUID)
        self._verified_oid = value

    @property
    def verified_data(self) -> dict:
        """
        Action data, serialized in CBOR.
        """
        if self._verified_data is None and self._from_fbs:
            _verified_data = self._from_fbs.VerifiedDataAsBytes()
            if _verified_data:
                self._verified_data = cbor2.loads(_verified_data)
            else:
                self._verified_data = {}
        return self._verified_data

    @verified_data.setter
    def verified_data(self, value: dict):
        assert value is None or type(value) == dict
        self._verified_data = value

    @staticmethod
    def cast(buf):
        return VerifiedAction(_VerifiedActionGen.GetRootAsVerifiedAction(buf, 0))

    def build(self, builder):

        oid = self.oid.bytes if self.oid else None
        if oid:
            oid = builder.CreateString(oid)

        vcode = self.vcode
        if vcode:
            vcode = builder.CreateString(vcode)

        verified_oid = self.verified_oid.bytes if self.verified_oid else None
        if verified_oid:
            verified_oid = builder.CreateString(verified_oid)

        verified_data = self.verified_data
        if verified_data:
            verified_data = builder.CreateString(cbor2.dumps(verified_data))

        VerifiedActionGen.VerifiedActionStart(builder)

        if oid:
            VerifiedActionGen.VerifiedActionAddOid(builder, oid)

        if self.created:
            VerifiedActionGen.VerifiedActionAddCreated(builder, int(self.created))

        if self.vtype:
            VerifiedActionGen.VerifiedActionAddVtype(builder, self.vtype)

        if self.vstatus:
            VerifiedActionGen.VerifiedActionAddVstatus(builder, self.vstatus)

        if vcode:
            VerifiedActionGen.VerifiedActionAddVcode(builder, vcode)

        if verified_oid:
            VerifiedActionGen.VerifiedActionAddVerifiedOid(builder, verified_oid)

        if verified_data:
            VerifiedActionGen.VerifiedActionAddVerifiedData(builder, verified_data)

        final = VerifiedActionGen.VerifiedActionEnd(builder)

        return final


@table('84d805a7-c012-4dfa-9b95-e34760767f82', build=VerifiedAction.build, cast=VerifiedAction.cast)
class VerifiedActions(MapUuidFlatBuffers):
    """
    Database table for verification/verified actions, eg on-boarding new XBR members.
    """


class _UserKeyGen(UserKeyGen.UserKey):
    """
    Expand methods on the class code generated by flatc.

    FIXME: come up with a PR for flatc to generated this stuff automatically.
    """
    @classmethod
    def GetRootAsUserKey(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = _UserKeyGen()
        x.Init(buf, n + offset)
        return x

    def PubkeyAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def OwnerAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None


class UserKey(object):
    """
    User client (public) keys.
    """
    def __init__(self, from_fbs=None):
        self._from_fbs = from_fbs

        # User key - a Ed25519 public key - for authenticating using WAMP-cryptosign.
        # [uint8] (uint256)
        self._pubkey = None

        # Timestamp (epoch time in ns) of initial creation of this record.
        # uint64 (timestamp)
        self._created = None

        # ID of user account this user key is owned by.
        # [uint8] (uuid)
        self._owner = None

    def marshal(self):
        obj = {
            'pubkey': bytes(self.pubkey),
            'created': int(self.created),
            'owner': self.owner.bytes,
        }
        return obj

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    @property
    def pubkey(self) -> bytes:
        """
        User key - a Ed25519 public key - for authenticating using WAMP-cryptosign.
        """
        if self._pubkey is None and self._from_fbs:
            if self._from_fbs.PubkeyLength():
                self._pubkey = self._from_fbs.PubkeyAsBytes()
        return self._pubkey

    @pubkey.setter
    def pubkey(self, value: bytes):
        assert value is None or (type(value) == bytes and len(value) == 32)
        self._pubkey = value

    @property
    def created(self) -> np.datetime64:
        """
        Timestamp (epoch time in ns) of initial creation of this record.
        """
        if self._created is None and self._from_fbs:
            self._created = np.datetime64(self._from_fbs.Created(), 'ns')
        return self._created

    @created.setter
    def created(self, value: np.datetime64):
        assert value is None or isinstance(value, np.datetime64)
        self._created = value

    @property
    def owner(self) -> uuid.UUID:
        """
        ID of user account this user key is owned by.
        """
        if self._owner is None and self._from_fbs:
            if self._from_fbs.OwnerLength():
                _owner = self._from_fbs.OwnerAsBytes()
                self._owner = uuid.UUID(bytes=bytes(_owner))
            else:
                self._owner = uuid.UUID(bytes=b'\x00' * 20)
        return self._owner

    @owner.setter
    def owner(self, value: uuid.UUID):
        assert value is None or isinstance(value, uuid.UUID)
        self._owner = value

    @staticmethod
    def cast(buf):
        return UserKey(_UserKeyGen.GetRootAsUserKey(buf, 0))

    def build(self, builder):

        owner = self.owner.bytes if self.owner else None
        if owner:
            owner = builder.CreateString(owner)

        pubkey = self.pubkey
        if pubkey:
            pubkey = builder.CreateString(pubkey)

        UserKeyGen.UserKeyStart(builder)

        if pubkey:
            UserKeyGen.UserKeyAddPubkey(builder, pubkey)

        if self.created:
            UserKeyGen.UserKeyAddCreated(builder, int(self.created))

        if owner:
            UserKeyGen.UserKeyAddOwner(builder, owner)

        final = UserKeyGen.UserKeyEnd(builder)

        return final


@table('5b5d0ce7-33f4-4421-a6ab-ed77cafc763a', build=UserKey.build, cast=UserKey.cast)
class UserKeys(MapBytes32FlatBuffers):
    """
    Database table for user client keys.
    """


@table('68b736f8-27df-4e3e-b80f-1b855ae5596f')
class IndexUserKeyByAccount(MapUuidTimestampBytes32):
    """
    Database (index) table for (member_oid, created) -> userkey mapping.
    """


class Schema(object):
    """
    XBR Network backend database schema.
    """

    attributes: Attributes
    """
    Generic meta-data attributes that can be stored on objects in tables. Primary key of this table is ``(table_oid, object_oid, attribute)``.
    """

    blocks: Blocks
    """
    Ethereum blocks basic information.
    """

    token_approvals: TokenApprovals
    """
    Token approvals archive.
    """

    token_transfers: TokenTransfers
    """
    Token transfers archive.
    """

    members: Members
    """
    XBR network members.
    """

    markets: Markets
    """
    XBR markets.
    """

    idx_markets_by_owner: IndexMarketsByOwner
    """
    Index on XBR markets.
    """

    idx_markets_by_actor: IndexMarketsByActor
    """
    Index on XBR markets.
    """

    actors: Actors
    """
    XBR market actors.
    """

    accounts: Accounts
    """
    Member accounts database table :class:`xbrnetwork.Accounts`.
    """

    idx_accounts_by_username: IndexAccountsByUsername
    """
    Index "by username" of member accounts :class:`xbrnetwork.IndexAccountsByUsername`.
    """

    idx_accounts_by_email: IndexAccountsByEmail
    """
    Index "by email" of member accounts :class:`xbrnetwork.IndexAccountsByEmail`.
    """

    idx_accounts_by_wallet: IndexAccountsByWallet
    """
    Index "by wallet" of member accounts :class:`xbrnetwork.IndexAccountsByWallet`.
    """

    verified_actions: VerifiedActions
    """
    Verified actions database table :class:`xbrnetwork.VerifiedActions`.
    """

    user_keys: UserKeys
    """
    User client keys database table :class:`xbrnetwork.UserKeys`.
    """

    idx_user_key_by_account: IndexUserKeyByAccount
    """
    Index "by pubkey" of user keys :class:`xbrnetwork.IndexUserKeyByAccount`.
    """
    def __init__(self, db):
        self.db = db

    @staticmethod
    def attach(db):
        """
        Attach database schema to database instance.

        :param db: Database to attach schema to.
        :type db: :class:`zlmdb.Database`
        """
        schema = Schema(db)

        schema.attributes = db.attach_table(Attributes)

        schema.blocks = db.attach_table(Blocks)

        schema.token_approvals = db.attach_table(TokenApprovals)

        schema.token_transfers = db.attach_table(TokenTransfers)

        schema.members = db.attach_table(Members)

        schema.markets = db.attach_table(Markets)

        schema.idx_markets_by_owner = db.attach_table(IndexMarketsByOwner)
        schema.markets.attach_index('idx1', schema.idx_markets_by_owner, lambda market:
                                    (market.owner, market.timestamp))

        schema.actors = db.attach_table(Actors)
        schema.idx_markets_by_actor = db.attach_table(IndexMarketsByActor)

        # schema.actors.attach_index('idx1', schema.idx_markets_by_actor, lambda actor:
        #                            (actor.actor, actor.timestamp))

        schema.accounts = db.attach_table(Accounts)

        schema.idx_accounts_by_username = db.attach_table(IndexAccountsByUsername)
        schema.accounts.attach_index('idx1', schema.idx_accounts_by_username,
                                     lambda account: account.username)

        schema.idx_accounts_by_email = db.attach_table(IndexAccountsByEmail)
        schema.accounts.attach_index('idx2', schema.idx_accounts_by_email, lambda account: account.email)

        schema.idx_accounts_by_wallet = db.attach_table(IndexAccountsByWallet)
        schema.accounts.attach_index('idx3', schema.idx_accounts_by_wallet,
                                     lambda account: account.wallet_address)

        schema.verified_actions = db.attach_table(VerifiedActions)

        schema.user_keys = db.attach_table(UserKeys)

        schema.idx_user_key_by_account = db.attach_table(IndexUserKeyByAccount)
        schema.user_keys.attach_index('idx1', schema.idx_user_key_by_account, lambda user_key:
                                      (user_key.owner, user_key.created))

        return schema
