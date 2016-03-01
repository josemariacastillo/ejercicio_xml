# -*- coding: utf-8 -*-
#!/usr/bin/env python

#Programa que pida por teclado la latitud longitud, y muestre la URL de su ubicación del mas cercano.

from lxml import etree

datos=etree.parse("festivales.xml")

latitud=float(raw_input("Introduzca una latitud: "))
#longitud=raw_input("Introduzca una longitud: ")

festivales=datos.xpath("//Festival")
resultado=[]

for f in festivales:
	latitudes=map(float,f.xpath("Latitud/text()"))
	for n in latitudes:
		print n
		resul=(n-latitud)*1000000
		resul = int(resul)
		resultado.append(resul)

		
print min(resultado)/1000000
	

