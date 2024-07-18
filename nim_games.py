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


def premier_tour():
    print(f'Il y a 21 allumettes les voici \n {nim} \n à tour de rôle, choisissez le nombre d\'allumette à enlever,'
          f'vous pouvez enlever 1, 2, 3 ou 4 allumettes. le dernier qui enlève la ou les allumettes à gagner')


def partie_lance():
    while True:
        try:
            len_nim_nb = len_tableau(nim)
            nombre_supprimer = int(input("Veuillez choisir le nombre d'allumette à enlever : "))
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


premier_tour()
partie_lance()
