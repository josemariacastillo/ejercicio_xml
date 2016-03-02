# -*- coding: utf-8 -*-
#!/usr/bin/env python

#Programa que pida por teclado la latitud longitud, y muestre la URL de su ubicación.

from lxml import etree

datos=etree.parse("festivales.xml")

latitud=raw_input("Introduzca una latitud: ")
longitud=raw_input("Introduzca una longitud: ")

festivales=datos.xpath("//Festival")

encontrado=False
for f in festivales:
	if latitud in f.xpath("Latitud/text()") and longitud in f.xpath("Longitud/text()"):
		print "URL: ",f.xpath("URL/text()")[0]
		encontrado=True
	
if encontrado==False:
	print "No coincide la latitud o longitud introducida" 
