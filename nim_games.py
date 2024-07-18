#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux de Nim (variante simple et de Marienbad)
"""


nim = ["|", "|", "|", "|", "|", "|", "|",
       "|", "|", "|", "|", "|", "|", "|",
       "|", "|", "|", "|", "|", "|", "|"]


def len_tableau(nim_nb):
    return len(nim_nb)


def supprimer_elements(tableau, nombre_elements):
    for _ in range(nombre_elements):
        tableau.pop()


def partie_lance():
    while True:
        try:
            len_nim_nb = len_tableau(nim)
            nombre_supprimer = int(input("Veuillez choisir le nombre d'allumette à enlever :"))
            if nombre_supprimer < 1 or nombre_supprimer > 4:
                print("Veuillez entrer un nombre entre 1 et 4.")
                continue
            supprimer_elements(nim, nombre_supprimer)
            if len_nim_nb > 1:
                print(nim)
            else:
                print("Bravo ! Vous avez gagné.")
                break

        except ValueError:
            print(f"Erreur : saisissez un nombre entier valide")


partie_lance()



