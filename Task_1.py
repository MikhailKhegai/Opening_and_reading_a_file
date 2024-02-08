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
print(cook_book)