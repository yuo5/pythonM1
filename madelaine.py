#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:28:07 2018

@author: madelain
"""

######### TP1 #########


###### EXERCICE 1

def somdiv(n):
    s=0
    for d in range(1,n):
        if n%d == 0:
            s=s+d
    return(s)

# si ca retourne n, c est un nombre parfait
# si ca retourne autre chose ce n est pas un nombre parfait

# on peut faire range(1,n//2+1)
# car on ne trouvera pas de diviseur de n au dessus de n/2
# // c'est la division entiere/euclidienne
    
def nbparfait(m):
    return somdiv(m) == m

def parfaits(p):
    l = []
    for i in range(p+1):
        if nbparfait(i):
            l.append(i)
    return(l)

# attention, ne pas ecrire l = l.append(...)


def amicaux(q):
    liste=[]
    for i in range(q+1):
        for j in range(i+1):
            if somdiv(j)==i and somdiv(i)==j and i != j :
                liste.append([i,j])
    return(liste)

def amicauxameliore(q):
    liste=[]
    for i in range(q+1):
        sdi=somdiv(i)
        for j in range(i+1,q):
            if somdiv(j)==i and sdi == j:
                liste.append([i,j])
    return(liste)

def amicauxameliore2(q):
    liste=[]
    for i in range(q+1):
        sdi=somdiv(i)
        if somdiv(sdi) == i and i < sdi < q :
                liste.append([i,sdi])
    return(liste)




###### EXERCICE 2

from math import sqrt

def estpremier(n):
    if n in [0,1]: return False
    for d in range(2,int(sqrt(n))+1):
        if n%d == 0:
            return False
    return True

def chanceux(p):
    for k in range(p-1):
        if estpremier(p+k*k+k)!=True:
            return('pas chanceux')
    return('chanceux')
    
# ou if not estpremier(p+k**2+k)
# on peut rajouter :
# if p in [0,1]: return False
    
def listechanceux(n):
    l=[]
    for i in range(n+1):
        if chanceux(i)=='chanceux':
            l.append(i)
    return(l)
    

    
    
###### EXERCICE 3
    
def sommecube(n):
    max=((1000000)**(1/3)+1)//1
    for i in range(max+1):
        cubei=i**3
        for j in range(max+1):
            if cubei+j**3!=n:
                return(False)
    return([i,j])

# on peut prendre max = int(n**(1/3))
    
def listecube(m):
    l=[]
    for i in range(m+1):
        if sommecube(i):
            l.append(i)
    return(l)
    
    
## correction :
from math import *

def taxicab(N):
    n=int(N**(1/3))+1
    #n2=ceil(N**(1/3)) # pour avoir l arrondi superieur
    #n3=round(...) donne l arrondi
    # N**(1/3)=99.999999999999
    # int(N**(1/3)) = 99
    # donc il faut rajouter 1
    # int sert a tronquer
    liste=[]
    for i in range(1,n+1):
        cubei=i**3
        for j in range(i+1,n+1):
            cubej=j**3
            sommeij=cubei+cubej
            if sommeij<N:
                for k in range(i+1,n+1):
                    cubek=k**3
                    for l in range(k+1,n+1):
                        if sommeij==cubek+l**3:
                            liste.append([sommeij,'s obtient avec',i,j,'et',k,l])
    return(liste)

## avec sortie sympathique :   
def taxicab2(N):
    n=int(N**(1/3))+1
    for i in range(1,n+1):
        cubei=i**3
        for j in range(i+1,n+1):
            cubej=j**3
            sommeij=cubei+cubej
            if sommeij<N:
                for k in range(i+1,n+1):
                    cubek=k**3
                    for l in range(k+1,n+1):
                        if sommeij==cubek+l**3:
                            print(f"{sommeij} s ecrit {i}**3+{j}**3 ou {k}**3+{l}**3")
    