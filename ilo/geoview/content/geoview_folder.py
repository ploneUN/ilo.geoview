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
from z3c.form.browser.checkbox import CheckBoxFieldWidget


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

class subregions(object):
    grok.implements(IContextSourceBinder)
    def __call__(self, context):
        results = []
        results.append(SimpleTerm(value='015', token='015', title='Northern Africa'))

class Igeoviewfolder(form.Schema, IImageScaleTraversable):
    """
    Geoview Folder
    """

    form.widget(item_type=CheckBoxFieldWidget)
    item_type = schema.List(
        title=u"For Consideration of",
       required=False,
        value_type=schema.Choice(
            source=content_types()
        ),
    )
    
    #default_region = schema.Choice(
    #    title = _(u"Default Map View"),
    #    required = True,
    #    vocabulary='ilo.geoview.subregions',
    #)
    
    #form.widget(subregion=CheckBoxFieldWidget)
    #subregion = schema.List(
    #    title = _(u"Alternative Map Views"),
    #    required = False,
    #    value_type=schema.Choice(
    #        vocabulary='ilo.geoview.subregions',
    #    )
    #)
    
    #@invariant
    #def validate_regions(self):
    #    if self.subregion:
    #        if self.default_region not in self.subregion:
    #            raise Invalid(_(u"Default map view should belong to the list of selected map views."))
    pass

alsoProvides(Igeoviewfolder, IFormFieldProvider)
