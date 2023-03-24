from typing import Callable


def arrow(func: Callable):
    def wrapper(items):
        dic = {}
        for item in items:
            if type(item) not in (list, set, dict):
                dic[item] = dic.get(item)
        return func(dic)
    return wrapper

def number_filter(func: Callable):
    def wrapper(items):
        filter_items = []
        for item in items:
            if type(item) in (int, float):
                filter_items.append(item)
        return func(filter_items)
    return wrapper



def round_dict(func: Callable):
    def wrapper(filter_items):
        round_items = []
        for i in filter_items:
            round_items.append(round(i))
        return func(round_items)
    return wrapper


# Decorate this function with 3 decorators above in a correct order
def like_numbers(items: list) -> str:
    return f"I like to filter, rounding, doubling, store and decorate numbers: {', '.join(items)}!"

#_______________________________________________________________________________________________________________
@number_filter
@round_dict
def like_numbers(items: list):
    return f"I like to filter, rounding, doubling, " \
           f"store and decorate numbers: {', '.join(items)}!"

items = ["35", 2.1, 4, 8.88, -123, "S", {"a", "b", 5}]

like_numbers(items) # == "I like to filter, rounding, doubling, "
#                        "store and decorate numbers: "
#                        "2 -> 4, 4 -> 8, 9 -> 18, -123 -> -246!"

