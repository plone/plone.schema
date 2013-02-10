from zope.interface import Attribute
from zope.schema import URI
from zope.schema.interfaces import IURI

from plone.schemaeditor.fields import FieldFactory

from plone.schema.field import Email
from plone.schema.interfaces import IEmail

from plone.schema import _


class IURI(IURI):

    # prevent some settings from being included in the field edit form
    default = Attribute('')


class IEmail(IEmail):

    # prevent some settings from being included in the field edit form
    default = Attribute('')


URIFactory = FieldFactory(URI, _(u'URI Field'))
EmailFactory = FieldFactory(Email, _(u'Email Field'))
