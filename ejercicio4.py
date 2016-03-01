# -*- coding: utf-8 -*-
#!/usr/bin/env python

#Programa que pida una comarca y muestra a la localidad que pertenece.

from lxml import etree

datos=etree.parse("festivales.xml")

comarca=raw_input("Introduce una comarca: ").upper()

festivales=datos.xpath("//Festival")

for f in festivales:
	if comarca in f.xpath("Comarca/text()"):
		print f.xpath("Localidad/text()")[0]