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


nombre_a_supprimer = int(input("veuillez choisir le nombre d'allumette à enlever (1, 2, 3 ou 4) : "))
supprimer_elements(nim_nb, nombre_a_supprimer)
print(nim_nb)
