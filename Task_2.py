with open('recipes.txt', encoding='utf') as f:
    cook_book = {}
    for l in f:
        dish_name = l.strip()
        dish_qt = range(int(f.readline()))
        list_ = []
        for qt in dish_qt:
            ingredient_name, quantity, measure = f.readline().strip().split('|')
            list_.append({'ingredient_name' : ingredient_name, 'quantity' : quantity, 'measure' : measure})
        cook_book.update({dish_name : list_})
        f.readline()
#print(cook_book)
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            shop_list[list(ingredient.values())[0]] = {'measure' : list(ingredient.values())[2], 'quantity' : int(list(ingredient.values())[1]) * person_count}
    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))