import pprint
 
import xml.dom.minidom
from xml.dom.minidom import Node

#############################################################################################
############ Set These Before you run this script
#############################################################################################


level = '/Users/initials/developer/OgmoProjectGenerator/man.oel'
													
_outputFile = '/Users/initials/developer/SLF/ogmo/tempProject.oep'										
_originalSize = 16
_newSize =20;
							

#############################################################################################
############ Ok that's all!
#############################################################################################							
							
							
doc = xml.dom.minidom.parse(level)
							
mapping = {}
 
for node in doc.getElementsByTagName("rect"):
	x = node.getAttribute("x")
	y = node.getAttribute("y")
	w = node.getAttribute("w")
	h = node.getAttribute("h")

	x = (int(x)/_originalSize)*_newSize;
	y = (int(y)/_originalSize)*_newSize;
	w = (int(w)/_originalSize)*_newSize;
	h = (int(h)/_originalSize)*_newSize;


	print '<rect x=\"'+str(x)+'\" y=\"'+str(y)+'\" w=\"'+str(w)+'\" h=\"'+str(h)+'\"/>'