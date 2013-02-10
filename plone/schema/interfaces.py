from zope.schema.interfaces import INativeStringLine
from zope.schema.interfaces import ValidationError

from plone.schema import _


class IEmail(INativeStringLine):
    """A field containing an email address
    """


class InvalidEmail(ValidationError):
    __doc__ = _("""The specified Email is not valid.""")
