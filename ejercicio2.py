# -*- coding: utf-8 -*-
#!/usr/bin/env python

#Programa que lea por teclado el nombre de una comarca y cuente sus Festivales.
from lxml import etree

datos=etree.parse("festivales.xml")

comarca=raw_input("Introduce una comarca: ").upper()

festivales=datos.xpath("//Festival")


encontrado=False
contador=0

for f in festivales:
	if comarca in f.xpath("Comarca/text()"):
		for n in f.xpath("Nombre/text()"):
			encontrado=True
			

		if encontrado==True:
			contador=contador+1

	
print contador	