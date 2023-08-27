import nuke

#from AutoProjectSettings import SaveandClose
import AutoProjectSettings


#Add to menu and assign shortcut key
nodeMenu = nuke.menu('Nuke').findItem('File')
nodeMenu.addCommand('New Comp from Footage', 'AutoProjectSettings.SaveandClose()', 'ctrl+shift+r')