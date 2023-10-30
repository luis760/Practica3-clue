# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:43:38 2023

@author: 52331
"""

import numpy as np
import os
import random

# Definir personajes, locaciones y armas
personajes = ["Sr. Blanco", "Prof. Plum", "Miss Scarlet", "Col. Mustard", "Sra. Peacock"]
locaciones = ["Casa", "Hotel", "Cocina", "Sala de estar", "Baño"]
armas = ["Cuchillo", "Candelabro", "Llave inglesa", "Cuerda", "Revólver"]

# Función para generar una historia
def generar_historia():
    personaje_culpable = random.choice(personajes)
    locacion_culpable = random.choice(locaciones)
    arma_culpable = random.choice(armas)
    print("Usted puede preguntar 10 veces ya sea: personaje, localizacion y arma ");
    print("Una vez terminadas esas 10 veces debe de responder personaje, locacion y arma del asesinato");
    for i in range (10):
        print("acerca de que desea preguntar:");
        print("1-personaje");
        print("2-localizacion");
        print("3-arma");
        menu1 = input("")

        if(menu1=='1'):
            print("Acerca de que personaje quiere saber: ");
            for i in range(5):
                print(personajes[i]);
            submenupersonaje=input("");
            submenupersonaje=int(submenupersonaje);
            if(personajes[submenupersonaje-1]==personaje_culpable):
                print("No se encontraron grabaciones de :  " , personajes[submenupersonaje-1] , " en las cintas de video a la hora del crimen ");
            else:
                print("Si se encontraron grabaciones de :  " , personajes[submenupersonaje-1] , " en las cintas de video a la hora del crimen ");
        if(menu1=='2'):
            print("Acerca de que locacion quiere saber: ");
            for i in range(5):
                print(locaciones[i]);
            submenulocacion=input("");
            submenulocacion=int(submenulocacion);
            if(locaciones[submenulocacion-1]==locacion_culpable):
                print("No se encontraron grabaciones en :  " , locaciones[submenulocacion-1] , " en las cintas de video a la hora del crimen ");
            else:
                print("Si se encontraron grabaciones en :  " , locaciones[submenulocacion-1] , " en las cintas de video a la hora del crimen ");
        if(menu1=='3'):
            print("Acerca de que arma quiere saber: ");
            for i in range(5):
                print(armas[i]);
            submenuarmas=input("");
            submenuarmas=int(submenuarmas);
            if(armas[submenuarmas-1]==arma_culpable):
                print("No se encontraron grabaciones del arma :  " , armas[submenuarmas-1] , " en las cintas de video a la hora del crimen ");
            else:
                print("Si se encontraron grabaciones del arma :  " , armas[submenuarmas-1] , " en las cintas de video a la hora del crimen ");

    print("Listo, has agotado tus preguntas : ");
    print("Digite el personaje culpable: ")
    for i in range(5):
        print(i,":" ,personajes[i]);
        
    submenupersonaje=input("");
    submenupersonaje=int(submenupersonaje);
    personaje_elegido=personajes[submenupersonaje-1]
    if(personaje_elegido==personaje_culpable):
        print(personaje_elegido, " es el culpable");  
    else:
        print("este no es el personaje culpable");
    print("Digite la locacalizacion culpable: ")
    for i in range(5):
        print(i,":" ,locaciones[i]);
        
    submenulocacion=input("");
    submenulocacion=int(submenulocacion);
    locacion_elegida=locaciones[submenulocacion-1]
    if(locacion_elegida==locacion_culpable):
        print(locacion_elegida, " es la locacion del asesinato culpable"); 
    else:
        print("locacion incorrecta");
    print("Digite el arma del culpable: ")
    for i in range(5):
        print(i,":" ,personajes[i]);
        
    submenuarma=input("");
    submenuarma=int(submenuarma);
    arma_elegida=armas[submenuarma-1]
    if(arma_elegida==arma_culpable):
        print(arma_elegida, " es el arma con la que se ejecuto al incauto");
    else:
        print("arma incorrecta");
    
    
    
# Generar cinco historias
for i in range(1):
    generar_historia()