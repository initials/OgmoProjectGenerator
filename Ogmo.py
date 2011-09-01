from xml.dom.minidom import Document
import os
import re
from PIL import Image
import shutil


#############################################################################################
############ Set These Before you run this script
#############################################################################################

_projectName = 'Super Lemonade Factory'


_defaultWidth = '480'
_defaultHeight = '320'

_minWidth = '480'
_minHeight = '320'

_maxWidth = '4800'
_maxHeight = '3200'

jobImagesDir = ['/Users/initials/developer/SLF/resource/']
				
walkThroughHigherDirectories = True 	# do you want to inspect the directories 
										# above images for quicktimes?
										# setting to true takes longer
										
_outputFile = "/Users/initials/developer/SLF/out/out2.oep"										
							

#############################################################################################
############ Ok that's all!
#############################################################################################							
							
							
							
										

# Create the minidom document
doc = Document()

# Create the <wml> base element
project = doc.createElement("project")
doc.appendChild(project)

paragraph1 = doc.createElement("name")
project.appendChild(paragraph1)

# Give the <p> elemenet some text
ptext = doc.createTextNode(_projectName)
paragraph1.appendChild(ptext)


settings = doc.createElement("settings")
project.appendChild(settings)

# Give the <p> elemenet some text
defaultWidth = doc.createElement("defaultWidth")
settings.appendChild(defaultWidth)

ptext = doc.createTextNode(_defaultWidth)
defaultWidth.appendChild(ptext)

dh = doc.createElement("defaultHeight")
settings.appendChild(dh)

ptext = doc.createTextNode(_defaultHeight)
dh.appendChild(ptext)

mw = doc.createElement("minWidth")
settings.appendChild(mw)
ptext = doc.createTextNode(_minWidth)
mw.appendChild(ptext)

mh = doc.createElement("minHeight")
settings.appendChild(mh)
ptext = doc.createTextNode(_minHeight)
mh.appendChild(ptext)

maxWidth = doc.createElement("maxWidth")
settings.appendChild(maxWidth)
ptext = doc.createTextNode(_maxWidth)
maxWidth.appendChild(ptext)

maxHeight = doc.createElement("maxHeight")
settings.appendChild(maxHeight)
ptext = doc.createTextNode(_maxHeight)
maxHeight.appendChild(ptext)

bgColor = doc.createElement("bgColor")
settings.appendChild(bgColor)
ptext = doc.createTextNode("0x000000")
bgColor.appendChild(ptext)

workingDirectory = doc.createElement("workingDirectory")
settings.appendChild(workingDirectory)
ptext = doc.createTextNode("../resource")
workingDirectory.appendChild(ptext)



tilesets = doc.createElement("tilesets")
project.appendChild(tilesets)

new = doc.createElement("tileset")
new.setAttribute("name", "tiles")
new.setAttribute("image", "level1/level1_tiles.png")
new.setAttribute("tileWidth", "10")
new.setAttribute("tileHeight", "10")
tilesets.appendChild(new)



objects = doc.createElement("objects")
project.appendChild(objects)

prefix = ''
dircount = 1

for i in range(len(jobImagesDir)):
	#can print all stuff here once
	#print i, jobImagesDir[i]

	for root, dirs, files in os.walk(jobImagesDir[i]):
		print dirs
		for name in files:       
			filename = root + "/" + name
			try:
				im = Image.open(filename)

			
				ObjectName = name.split('.')
						
				#this is what we are aiming for:
				# <object name="Ship" image="ship.png" width="18" height="18" originX="9" originY="9" limit="1" />
				new = doc.createElement("object")
				new.setAttribute("name", ObjectName[0])
				new.setAttribute("image", filename)
				new.setAttribute("width", str(im.size[0]))
				new.setAttribute("height", str(im.size[1]))
				new.setAttribute("originX", "0")
				new.setAttribute("originY", "0")			
				objects.appendChild(new)

			except:
				im = 'no.no'


		if (walkThroughHigherDirectories):
			pass
			

		else:
			break;
		



settings = doc.createElement("layers")
project.appendChild(settings)

new = doc.createElement("grid")
new.setAttribute("name", "solids")
new.setAttribute("gridSize", "10")
new.setAttribute("exportAsObjects", "true")
new.setAttribute("color", "0xAAFFFFFF")
settings.appendChild(new)

new = doc.createElement("tiles")
new.setAttribute("name", "stage")
new.setAttribute("gridSize", "10")
new.setAttribute("tileWidth", "10")
new.setAttribute("exportTileSize", "true")
new.setAttribute("exportTileIDs", "true")
settings.appendChild(new)


new = doc.createElement("objects")
new.setAttribute("name", "objects")
new.setAttribute("gridSize", "10")
new.setAttribute("drawGridSize", "10")
settings.appendChild(new)

f = open(_outputFile, "w")
try:
    f.write(doc.toprettyxml(indent="  "))
finally:
    f.close()