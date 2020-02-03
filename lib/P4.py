import random
import os
import subprocess
import time
import sys


class Board():
    """Grille de jeu et methodes pour la modifier"""
    def __init__(self,p1="X",p2="O"):
        """Initialisation de la grille"""
        # dimensions de la grille 
        self.couleurs = (p1, p2)
        # generation de la grille
        self.nbrCol = 7
        self.nbrLig = 8
        self.grille = []
        for i in range(self.nbrCol):
            self.grille.append([])
        # historique
        self.history = []

    def add(self, col, couleur, silent = None):
        """ajouter un jeton
           col = 1.. numéro de la colonne
           retour : la position du jeton (col, ligne)
                     (None, code erreur)  si erreur"""
        # quelques vérifications avant d'ajouter le jeton
        if not couleur in self.couleurs:
            if not silent : print ("Couleur non conforme :",couleur)
            return (None, 0)
        if (col<1) or (col>self.nbrCol):
            if not silent : print ("Valeur colonne non conforme : ",col)
            return (None, 1)
        if len(self.grille[col-1])==self.nbrLig:
            if not silent : print ("Impossible d'ajouter jeton, colonne pleine : ",col)
            return (None, 2)
        self.grille[col-1].append(couleur)
        self.history.append( (couleur, col-1) )
        return (col-1, len(self.grille[col-1])-1)

    def print_l(self):
        """Retourné une liste avec chaque ligne en str"""
        ##print( self.grille)
        lretour = []
        rut =""
        for j in range(self.nbrLig-1,-1,-1):
            line = ''
            for i in range(self.nbrCol):
                if len(self.grille[i]) <= j:
                    line = line + ":white_circle:  "
                else:
                    ##print(i,j)
                    if self.grille[i][j] == "X":
                        line = line + ':red_circle:  '
                    if self.grille[i][j] == "O":
                        line = line + ":large_blue_circle:  "
            lretour.append(line)
        for lop in lretour:
            rut= rut+lop+"\n"
        return rut   

    def print(self):




        """imprimer la grille"""
        ##print( self.grille)
        for j in range(self.nbrLig-1,-1,-1):
            line = str(j+1)+' '
            for i in range(self.nbrCol):
                ###print (len(self.grille[i]),j)
                if len(self.grille[i]) <= j:
                    line = line + "|   "
                else:
                    ###print(i,j)
                    line = line + "| "+self.grille[i][j]+' '
            line = line + "|"
        print ('  ',end='')






    def color(self, location):
        """returns the color of the location (col, lig)"""
        ###print("Location : ",location)
        if (len(self.grille[location[0]]) <= location[1]):
            return None
        return self.grille[location[0]][location[1]]

    def check(self, start, debug=False):
        """compter les jetons alignés
           retour : nombre max. alignés"""
        dirs = [(1,0), (0,1), (1,1), (-1,1)]
        maxAlign = 0
        print ("start",start)
        myColor = self.color(start)
        if not myColor: #case vide donnee
            print ("Error 001")
            return 0
        for di in dirs:
            if debug: print ("start direction ",di)
            n = 1
            # search in both directions
            for sign in [1.0,-1.0]:
                for i in range(1, (self.nbrCol+self.nbrLig)):
                    x = int(start[0]+float(i)*di[0]*sign)
                    y = int(start[1]+float(i)*di[1]*sign)
                    if (x<0) or (y<0) or (x>=self.nbrCol) or (y>=self.nbrLig): break
                    if debug: print("check ",x,y)
                    if self.color((x,y))==myColor:
                        n += 1
                        if debug: print("found one ; n = ",n)
                    else:
                        break
            if n > maxAlign: maxAlign = n
        return maxAlign

