import re

from zope.interface import implementer

from zope.schema import NativeStringLine
from zope.schema.interfaces import IFromUnicode

from plone.schema.interfaces import IEmail
from plone.schema.interfaces import InvalidEmail

# Taken from http://www.regular-expressions.info/email.html
_isemail = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}"
_isemail = re.compile(_isemail).match


@implementer(IEmail, IFromUnicode)
class Email(NativeStringLine):
    """Email schema field
    """

    def _validate(self, value):
        super(Email, self)._validate(value)
        if _isemail(value):
            return

        raise InvalidEmail(value)

    def fromUnicode(self, value):
        v = str(value.strip())
        self.validate(v)
        return v
