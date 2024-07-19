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
    print(f"Il y a 21 allumettes, les voici : {nim}")
    print("À tour de rôle, choisissez le nombre d'allumettes à enlever.")
    print("Vous pouvez enlever 1, 2, 3 ou 4 allumettes. Le dernier qui enlève la ou les allumettes a gagné.")


def partie_lance():
    player = 1
    while True:
        try:
            len_nim_nb = len_tableau(nim)
            if len_nim_nb == 0:
                print(f"Bravo ! Joueur {player} a gagné.")
                break
            nombre_supprimer = int(input(f"Joueur {player}, veuillez choisir le nombre d'allumettes à enlever : "))
            if nombre_supprimer < 1 or nombre_supprimer > 4:
                print("Veuillez entrer un nombre entre 1 et 4.")
                continue
            supprimer_elements(nim, nombre_supprimer)
            if len_nim_nb > 1:
                print(nim)
            else:
                print(f"Bravo ! Joueur {player} a gagné.")
                break
            player = 2 if player == 1 else 1

        except ValueError:
            print(f"Erreur : saisissez un nombre entier valide")


premier_tour()
partie_lance()
