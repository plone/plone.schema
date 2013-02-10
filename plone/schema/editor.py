from zope.interface import Attribute
from zope.schema import URI
from zope.schema.interfaces import IURI

from plone.schemaeditor.fields import FieldFactory


class IURI(IURI):

    # prevent some settings from being included in the field edit form
    default = Attribute('')


URIFactory = FieldFactory(URI, u'URI Field')
