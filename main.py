# with open('data.txt', 'rt', encoding='utf-8') as f:
#     cook_book = {}
#     for line in f:
#         dish_name = line.strip()
#         ingredients_count = int(f.readline())
#         ingredients_list = []
#         for i in range(ingredients_count):
#             temp = f.readline().strip()
#             ingredient_name, quantity, measure = temp.split(' | ')
#             ingredients_list.append({
#                 'ingredient_name': ingredient_name,
#                 'quantity': quantity,
#                 'measure': measure
#             })
#         f.readline()
#         cook_book[dish_name] = ingredients_list
#
#
# # print(cook_book)
#
#
# def get_shop_list_by_dishes(dish_name, person_count):
#     ingredient_book = {}
#     for dish in dish_name:
#         if dish in cook_book.keys():
#             for ingredients in cook_book[dish]:
#                 if ingredients['ingredient_name'] in ingredient_book.keys():
#                     ingredient_book[ingredients['ingredient_name']]['quantity'] += int(
#                         ingredients['quantity']) * person_count
#                 else:
#                     ingredient_book[ingredients['ingredient_name']] = {'measure': ingredients['measure'],
#                                                                        'quantity': int(
#                                                                            ingredients['quantity']) * person_count}
#     return ingredient_book


# print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


data = []
for name in ('1.txt', '2.txt', '3.txt'):
    with open(name, 'rt', encoding='utf-8') as f:
        text = f.readlines()
    data += [(name, text)]

data.sort(key=lambda el: len(el[1]))

with open('final.txt', 'w', encoding='utf-8') as f:
    for value in data:
        f.write(f'{value[0]}\n'
                f'{len(value[1])}\n'
                f'{"".join(value[1])}\n')









