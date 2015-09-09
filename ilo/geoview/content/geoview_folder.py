from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
#from plone.multilingualbehavior.directives import languageindependent
from collective import dexteritytextindexer

from ilo.geoview import MessageFactory as _
from zope.app.container.interfaces import IObjectAddedEvent
from Products.CMFCore.utils import getToolByName
from plone.i18n.normalizer import idnormalizer


# Interface class; used to define content-type schema.

class content_types(object):
    grok.implements(IContextSourceBinder)
    def __call__(self,context):
        brains = context.allowedContentTypes()
        results = []
        for brain in brains:
            title = brain.Title()
            results.append(SimpleTerm(value=brain.id, token=brain.id, title=title))
        return SimpleVocabulary(results)

class Igeoviewfolder(form.Schema, IImageScaleTraversable):
    """
    Geoview Folder
    """
    content_type = schema.Choice(
           title=_(u"Content Type"),
           required=False,
           source = content_types(),
        )
    pass

alsoProvides(Igeoviewfolder, IFormFieldProvider)