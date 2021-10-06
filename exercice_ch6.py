#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici

        values = list()

        while len(values) != 10:
            print("Veuiller s'il vous plait insérer 10 valeurs avec des espaces entre elles: \n")
            values = input().split(" ")

            if len(values) != 10:
                print("Vous n'avez pas inscrit les variables correctement, veuillez réessayer")
                values = list()

    return sorted(values)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici

        print("Veuillez inscrire le premier mot : \n")
        words = [input()]

        print("Veuillez inscrire le deuxième mot : \n")
        words.append(input())

        for letter in words[0]:
            return letter in words[1]

    else:
        for letter in words[0]:
            return letter in words[1]

def contains_doubles(items: list) -> bool:

    return list(set(items)) != items


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne

    best_average = 0
    best_student = ""

    for name, grades in student_grades.items():
        student_grades[name] = sum([note for note in grades]) / (len(grades))

    for student in student_grades:
        if student_grades[student] > best_average:
            best_average = student_grades[student]
            best_student = student

    return {best_student: best_average}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    letter_dictionnary = dict()
    for letter in sentence:
        if letter in letter_dictionnary:
            letter_dictionnary[letter] += 1
        else:
            letter_dictionnary[letter] = 1

    return letter_dictionnary


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données

    livre_recette = dict()

    print("combien de recettes voulez vous ajouter?")
    nb_entries = int(input())

    for i in range(nb_entries):
        print(f"Quel est le nom de votre recette numéro {i}: ")
        recette = input()

        print("Quels sont les ingrédients de cette recette "
              "(laissez un espace entre chaque ingrédient): ")
        ingredients = input().split(" ")

        livre_recette[recette] = ingredients

    return livre_recette


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    recette = ""

    while recette not in ingredients:

        print("Quel est le nom de la recette que vous cherchez: ")
        recette = input()

        if recette in ingredients:
            print("Voici les ingrédients de la recette choisi:", ingredients[recette])
        else:
            print("Désolé, mais cette recette n'est pas dans le livre de recette")


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    print(frequence(sentence))

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
