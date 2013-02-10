
from zope.component import adapter

from zope.interface import implementsOnly
from zope.interface import implementer

from z3c.form.interfaces import ITextWidget
from z3c.form.interfaces import IFormLayer
from z3c.form.interfaces import IFieldWidget

from z3c.form.browser.text import TextWidget
from z3c.form.widget import FieldWidget

from zope.schema.interfaces import IURI


class IURIWidget(ITextWidget):
    """ URI Widget """


class URIWidget(TextWidget):
    implementsOnly(IURIWidget)

    klass = u'uri-widget'
    value = None


@adapter(IURI, IFormLayer)
@implementer(IFieldWidget)
def URIFieldWidget(field, request):
    """IFieldWidget factory for URIWidget."""
    return FieldWidget(field, URIWidget(request))
