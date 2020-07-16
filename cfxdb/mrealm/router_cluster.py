##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import pprint

from cfxdb.mrealm.cluster import Cluster


class RouterCluster(Cluster):
    """
    CFC Web Cluster database configuration object.
    """
    def __init__(self,
                 oid=None,
                 label=None,
                 description=None,
                 tags=None,
                 name=None,
                 status=None,
                 changed=None,
                 _unknown=None):
        """

        :param oid: Object ID of node
        :type oid: uuid.UUID

        :param label: Optional user label of node
        :type label: str

        :param description: Optional user description of node
        :type description: str

        :param tags: Optional list of user tags on node
        :type tags: list[str]

        :param _unknown: Any unparsed/unprocessed data attributes
        :type _unknown: None or dict
        """
        Cluster.__init__(self,
                         oid=oid,
                         label=label,
                         description=description,
                         tags=tags,
                         name=name,
                         status=status,
                         changed=changed)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if not Cluster.__eq__(self, other):
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    def marshal(self):
        """
        Marshal this object to a generic host language object.

        :return: dict
        """
        obj = Cluster.marshal(self)

        obj.update({})

        return obj

    @staticmethod
    def parse(data):
        """
        Parse generic host language object into an object of this class.

        :param data: Generic host language object
        :type data: dict

        :return: instance of :class:`ManagementRealm`
        """
        assert type(data) == dict

        obj = Cluster.parse(data)
        data = obj._unknown

        # future attributes (yet unknown) are not only ignored, but passed through!
        _unknown = {}
        for k in data:
            if k not in []:
                _unknown[k] = data[k]

        obj = RouterCluster(oid=obj.oid,
                            label=obj.label,
                            description=obj.description,
                            tags=obj.tags,
                            name=obj.name,
                            status=obj.status,
                            changed=obj.changed,
                            _unknown=_unknown)

        return obj