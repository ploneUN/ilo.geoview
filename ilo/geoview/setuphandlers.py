from collective.grok import gs
from ilo.geoview import MessageFactory as _

@gs.importstep(
    name=u'ilo.geoview', 
    title=_('ilo.geoview import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('ilo.geoview.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
