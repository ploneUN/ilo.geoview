from five import grok
from plone.directives import dexterity, form
from ilo.geoview.content.geoview_folder import Igeoviewfolder
from Products.CMFCore.utils import getToolByName
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from ilo.mou.content.mou import Imou

grok.templatedir('templates')

class geoview_folder_mou_list(dexterity.DisplayForm):
    grok.context(Igeoviewfolder)
    grok.require('zope2.View')
    grok.name('mou_list')
    
    @property
    def catalog(self):
        return getToolByName(self.context, 'portal_catalog')
    
    def form_request(self):
        if self.request:
            if self.request.form:
                form = self.request.form
                if 'country' in form:
                    return form['country']
        return None
    
    def list_mous_sec(self, ctype=None):
        context = self.context
        results = []
        
        if self.form_request():
            country = self.form_request()
            brains = self.catalog.unrestrictedSearchResults(portal_type=ctype, review_state='published')
            for brain in brains:
                obj = brain._unrestrictedGetObject()
                if country in [obj.sender_country, obj.receiving_country]:
                    results.append({'title':brain.Title,
                                    'path':obj.absolute_url(),
                                    'description':brain.Description,
                                    'countries':self.country_name(obj.sender_country)+', '+self.country_name(obj.receiving_country)})
        return results
    
    def country_name(self, country):
        brains = getUtility(IVocabularyFactory, 'ilo.mou.country').__call__(self.context)
        for brain in brains:
            if brain.value == country:
                return brain.title
        return ''