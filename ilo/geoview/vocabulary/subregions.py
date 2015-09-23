from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
import copy

class Subregions(grok.GlobalUtility):
    grok.name('ilo.geoview.subregions')
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        results = []
        data = []
        
        results.append(SimpleTerm(value='015', token='015', title='Northern Africa'))
        results.append(SimpleTerm(value='011', token='011', title='Western Africa'))
        results.append(SimpleTerm(value='017', token='017', title='Middle Africa'))
        results.append(SimpleTerm(value='014', token='014', title='Eastern Africa'))
        results.append(SimpleTerm(value='018', token='018', title='Southern Africa'))
        
        results.append(SimpleTerm(value='154', token='154', title='Northern Europe'))
        results.append(SimpleTerm(value='155', token='155', title='Western Europe'))
        results.append(SimpleTerm(value='151', token='151', title='Eastern Europe'))
        results.append(SimpleTerm(value='039', token='039', title='Southern Europe'))
        
        results.append(SimpleTerm(value='021', token='021', title='Northern America'))
        results.append(SimpleTerm(value='029', token='029', title='Caribbean'))
        results.append(SimpleTerm(value='013', token='013', title='Central America'))
        results.append(SimpleTerm(value='005', token='005', title='South America'))
        
        results.append(SimpleTerm(value='143', token='143', title='Central Asia'))
        results.append(SimpleTerm(value='030', token='030', title='Eastern Asia'))
        results.append(SimpleTerm(value='034', token='034', title='Southern Asia'))
        results.append(SimpleTerm(value='035', token='035', title='South-Eastern Asia'))
        results.append(SimpleTerm(value='145', token='145', title='Western Asia'))
        
        results.append(SimpleTerm(value='053', token='053', title='Australia and New Zealand'))
        results.append(SimpleTerm(value='054', token='054', title='Melanesia'))
        results.append(SimpleTerm(value='057', token='057', title='Micronesia'))
        results.append(SimpleTerm(value='061', token='061', title='Polynesia'))
        
        return SimpleVocabulary(results)
            