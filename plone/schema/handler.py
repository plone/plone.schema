try:
    from plone.supermodel.exportimport import BaseHandler
    HAVE_SUPERMODEL = True
except ImportError:
    HAVE_SUPERMODEL = False

if HAVE_SUPERMODEL:
    from zope.schema import URI

    from plone.schema.field import Email

    URIHandler = BaseHandler(URI)
    EmailHandler = BaseHandler(Email)
