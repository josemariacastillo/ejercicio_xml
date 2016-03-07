# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from lxml import etree

datos=etree.parse("festivales.xml")

localidad=unicode(raw_input("Localidad: "),'utf8')
festivales=datos.xpath("//Festival")

encontrado=False

for f in festivales:
	if localidad in f.xpath("Localidad/text()"):
		fi=open("localidad.html","w")
		fi.write("<h1>"+f.xpath("Nombre/text()")[0]+"</h1>"+"\n")
		fi.write("<p>"+f.xpath("Descripcion/text()")[0]+"</p>"+"\n")
		fi.write("<a href="+f.xpath("URL/text()")[0]+">"+"Enlace"+"</a>"+"\n")
		fi.close()
		encontrado=True
		print "Se ha generado el fichero localidad.html"

if encontrado==False:
	print "Error al generar el fichero.html a localidad No existe"

