from app.currensy_calc.calc_nb import calc


def all_values(val_list: list, need_curr, quantity):
    list_for_temp = []
    for i in val_list:
        c = calc(i, need_curr, quantity)
        list_for_temp.append({c: i})
    return list_for_temp




