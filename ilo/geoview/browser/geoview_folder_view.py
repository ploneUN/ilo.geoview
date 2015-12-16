from five import grok
from plone.directives import dexterity, form
from ilo.geoview.content.geoview_folder import Igeoviewfolder
from Products.CMFCore.utils import getToolByName
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(Igeoviewfolder)
    grok.require('zope2.View')
    grok.template('geoview_folder_view')
    grok.name('view')
    
    @property
    def catalog(self):
        return getToolByName(self.context, 'portal_catalog')
    
    def map_contents(self):
        context= self.context
        catalog = self.catalog
        ctype = context.item_type
        path = '/'.join(context.getPhysicalPath())
        results = catalog.unrestrictedSearchResults(path={'query':path, 'depth':1}, review_state='published')
        
        return results
    
    def map_count(self):
        context= self.context
        results = self.map_contents()
        map_vocabs = self.map_vocabulary()
        data = {}
        final = []
        ctype = context.item_type
        
        for result in results:
            if result.portal_type in ctype:
                if result.portal_type == 'ilo.mou.mou':
                    obj = result._unrestrictedGetObject()
                    raw = {}
                    if hasattr(obj, 'sender_country'):
                        if obj.sender_country not in data:
                            data[obj.sender_country] = {'mou':1, 'sec':0}
                        else:
                            data[obj.sender_country]['mou'] += 1
                    
                    if hasattr(obj, 'receiving_country'):
                        if obj.receiving_country not in data:
                            data[obj.receiving_country] = {'mou':1, 'sec':0}
                        else:
                            data[obj.receiving_country]['mou'] += 1
                if result.portal_type == 'ilo.mou.sec':
                    obj = result._unrestrictedGetObject()
                    raw = {}
                    if hasattr(obj, 'sender_country'):
                        if obj.sender_country not in data:
                            data[obj.sender_country] = {'mou':0, 'sec':1}
                        else:
                            data[obj.sender_country]['sec'] += 1
                    
                    if hasattr(obj, 'receiving_country'):
                        if obj.receiving_country not in data:
                            data[obj.receiving_country] = {'mou':0, 'sec':1}
                        else:
                            data[obj.receiving_country]['sec'] += 1
        
        map_vocabs = self.map_vocabulary()
        
        for ky in map_vocabs.keys():
            mou = 0
            sec = 0
            if ky in data:
                mou = data[ky]['mou']
                sec = data[ky]['sec']
            
            final.append({'title':map_vocabs[ky],
                          'mou':mou,
                          'sec':sec,
                          'count':mou+sec,
                          'code':ky})
        
        
        
        #for ky in data.keys():
        #    if ky in map_vocabs:
        #        final.append({'title':map_vocabs[ky],
        #                      'count':data[ky]})
        
            
        
        
        return final
    
    def map_vocabulary(self):
        context = self.context
        brains = getUtility(IVocabularyFactory, 'ilo.mou.country').__call__(context)
        results = {}
        for brain in brains:
            if self.correct_country_name(brain.value):
                results[brain.value] = self.correct_country_name(brain.value).title()
            else:
                results[brain.value] = brain.title
        return results
    
    def correct_country_name(self, country):
        countries = {'BL': 'plurinational state of bolivia',
                     'CD': 'democratic republic of the congo',
                     'IR': 'islamic republic of iran',
                     'KP': 'democratic peoples republic of korea',
                     'KR': 'republic of korea',
                     'MK': 'republic of macedonia',
                     'TZ': 'united republic of tanzania',
                     'VE': 'bolivarian republic of venezuela'}
        if country in countries:
            return countries[country]
        return None
    
    def show_regions(self):
        context = self.context
        regions = getUtility(IVocabularyFactory, 'ilo.geoview.subregions').__call__(context)
        results = []
        data = {}
        subregions = context.subregion
        if context.default_region:
            data[context.default_region] = ''
        for subregion in subregions:
            if subregion not in data:
                data[subregion] = ''
        for region in regions:
            if region.value in data:
                data[region.value] = region.title
        
        return data
    
    def show_small_countries(self):
        results = self.map_count()
        if results:
            for result in results:
                if (result['code'] in ('SG', 'HK')) and (result['sec'] or result['mou']):
                    return True
        return False
    
            
        
    
    
    
            
    
        
    
