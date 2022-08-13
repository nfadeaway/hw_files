from pprint import pprint
import os


def cook_book():
    cook_book_dict = {}
    with open('recipes.txt', encoding='utf-8') as recipes_file:
        recipes_file_lines = recipes_file.readlines()
        i = 0
        while i < len(recipes_file_lines):
            cook_book_dict[recipes_file_lines[i].rstrip()] = []
            for j in range(i + 2, i + 2 + int(recipes_file_lines[i + 1])):
                ingredient = [x for x in recipes_file_lines[j].split(' | ')]
                cook_book_dict[recipes_file_lines[i].rstrip()].append({'ingredient_name': ingredient[0],
                                                                       'quantity': int(ingredient[1]),
                                                                       'measure': ingredient[2].rstrip()})
            i += 3 + int(recipes_file_lines[i + 1])
    return cook_book_dict


def get_shop_list_by_dishes(dishes, person_count):
    dishes = set(dishes)
    ingredients = {}
    for dish in dishes:
        if dish in cook_book():
            for ingredient in cook_book()[dish]:
                if ingredient['ingredient_name'] in ingredients:
                    ingredients[ingredient['ingredient_name']]['quantity'] += \
                        ingredients[ingredient['ingredient_name']]['quantity'] * person_count
                else:
                    ingredients[ingredient['ingredient_name']] = \
                        {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
    return ingredients


def files_union():
    files_list = os.listdir(path='folder')
    files_list = sorted(['folder/' + x for x in files_list], key=os.path.getsize)
    for file in files_list:
        with open(file, encoding='utf-8') as file_in_progress:
            with open('folder/result.txt', 'a+', encoding='utf-8') as result_file:
                lines = file_in_progress.readlines()
                result_file.write(os.path.basename(file) + '\n')
                result_file.write(str(len(lines)) + '\n')
                for line in lines:
                    result_file.write(line)
                result_file.write('\n')


# Задача №1
print(' Задача №1 '.center(50, '*'), '\n')
pprint(cook_book())

# Задача №2
print()
print(' Задача №2 '.center(50, '*'), '\n')
pprint(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2))

# Задача №3 (файлы в папке folder)
files_union()
