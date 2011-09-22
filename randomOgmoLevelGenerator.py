from xml.dom.minidom import Document
import os
import re
from PIL import Image
import shutil
import random


#############################################################################################
############ Set These Before you run this script
#############################################################################################


_width = '640'
_height = '640'
										
_outDir = "C:/Users/User/Documents/My Dropbox/slf/randomLevels"
newFileNameRandom=random.randint(0,1000000)		
_outFile = _outDir + '/level' + str(newFileNameRandom) +'.oel'
									
							

#############################################################################################
############ Ok that's all!
#############################################################################################							
							
							
							
										

# Create the minidom document
doc = Document()

# Create the <wml> base element
project = doc.createElement("level")
doc.appendChild(project)

# Give the <p> elemenet some text
width = doc.createElement("width")
project.appendChild(width)

ptext = doc.createTextNode(_width)
width.appendChild(ptext)

dh = doc.createElement("height")
project.appendChild(dh)

ptext = doc.createTextNode(_height)
dh.appendChild(ptext)



solids = doc.createElement("solids")
project.appendChild(solids)

for i in range(1):
	new = doc.createElement("rect")
	new.setAttribute("x", str(i*10))
	new.setAttribute("y", "10")
	new.setAttribute("w", "10")
	new.setAttribute("h", "10")

	solids.appendChild(new)
	
	
	
RX=-200;
RY=-200;
for rxx in range (3):
	RX+=200
	RY+=200

	for yy in range (3):
		rw = 20;
		numBlocks = int(3+random.random()*4);
		maxW = 10;
		minW = 2;
		maxH = 8;
		minH = 1;
		bx=0;
		by=0;
		bw=0;
		bh=0;
		check=False;
		i=0;
		for i in range(12):
			#while(not check):
			bw = minW + random.random()*(maxW-minW);
			bh = minH + random.random()*(maxH-minH);
			bx = -1 + random.random()*(rw+1-bw);
			by = -1 + random.random()*(rw+1-bh);
			
			new = doc.createElement("rect")
			new.setAttribute("x", str(int(RX+bx*10)))
			new.setAttribute("y", str(int(RY+by*10)))
			new.setAttribute("w", str(int(bw*10)))
			new.setAttribute("h", str(int(bh*10)))
		
			solids.appendChild(new)
					
			#b = new FlxTileblock(RX+bx*10,RY+by*10,bw*10,bh*10);


	

#ptext = doc.createTextNode("solids")
#solids.appendChild(ptext)






f = open(_outFile, "w")
try:
    f.write(doc.toprettyxml(indent="  "))
finally:
    f.close()