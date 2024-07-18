#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux de Nim (variante simple et de Marienbad)
"""

nim_nb = ["|", "|", "|", "|", "|", "|", "|",
          "|", "|", "|", "|", "|", "|", "|",
          "|", "|", "|", "|", "|", "|", "|"]


def supprimer_elements(tableau, nombre_elements):
    for _ in range(nombre_elements):
        tableau.pop()

print(nim_nb)
nombre_a_supprimer = int(input("veuillez choisir le nombre d'allumette à enlever (1, 2, 3 ou 4) : "))
supprimer_elements(nim_nb, nombre_a_supprimer)


while True:
    try:
        len_nim_nb = len(nim_nb)
        nombre_supprimer = int(input("Joueur suivant veuillez choisir le nombre "
                                     "d'allumette à enlever (1, 2, 3 ou 4) : "))
        supprimer_elements(nim_nb, nombre_supprimer)
        if len_nim_nb > 1:
            print(nim_nb)
        else:
            print("bravo")
            break

    except ValueError:
        print(f"Erreur : saisissez un nombre entier valide")
