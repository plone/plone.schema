from zope.interface import implementer
from zope.schema import Dict as ZopeDictField
from zope.schema.interfaces import IDict
from zope.schema.interfaces import WrongType


@implementer(IDict)
class Dict(ZopeDictField):
    def __init__(self, widget=None, **kw):
        if widget and not isinstance(widget, str):
            raise WrongType

        self.widget = widget

        super(Dict, self).__init__(**kw)
