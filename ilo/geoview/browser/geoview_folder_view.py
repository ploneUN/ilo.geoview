from five import grok
from plone.directives import dexterity, form
from ilo.geoview.content.geoview_folder import Igeoviewfolder

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(Igeoviewfolder)
    grok.require('zope2.View')
    grok.template('geoview_folder_view')
    grok.name('view')

