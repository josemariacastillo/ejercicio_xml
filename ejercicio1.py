# -*- coding: utf-8 -*-
#!/usr/bin/env python

#Programa que muestra la lista de Nombres de Festivales y la descripción que tiene cada una.
from lxml import etree

datos=etree.parse("festivales.xml")

festivales=datos.xpath("//Festival")

for f in festivales:
	print f.xpath("Nombre/text()")[0]
	print f.xpath("Descripcion/text()")[0]
		


