# -*- coding: utf-8 -*-
#!/usr/bin/env python

#Pedir una cadena por teclado y mostrar todos los Festivales 
#cuyo nombre empieza por dicha cadena, junto con su URL donde su ubica el festival.

from lxml import etree

datos=etree.parse("festivales.xml")

cad=raw_input("Introduce un festival: ")

festivales=datos.xpath("//Festival")

for f in festivales:
	if f.xpath("Nombre/text()")[0].startswith(cad):
		print f.xpath("Nombre/text()")[0]
		print f.xpath("URL/text()")[0]
