# TASK_00
def squeak_decorator(func):
    def squeak(*args):
        print("SQUEAK")
        return func(*args)
    return squeak
@squeak_decorator
def add_ingot(purse):
    n = purse.get("gold_ingots")
    new_purse = {"gold_ingots": 1 + n}
    return new_purse

@squeak_decorator
def get_ingot(purse):
    n = purse.get("gold_ingots")
    if n <= 0:
        new_purse = {"gold_ingots": 0}
    else:
        new_purse = {"gold_ingots": n - 1}
    return new_purse

@squeak_decorator
def empty(purse):
    return {"gold_ingots": 0}


# TASK_01
@squeak_decorator
def split_booty(*purses):
    general = 0
    res_list = []
    for pur in purses:
        if "gold_ingots" in pur:
            if pur.get("gold_ingots") < 0:
                empty(pur)
            general += pur.get("gold_ingots")
        res_list.append({"gold_ingots": 0})
    if general > 0:
        avg = general // len(res_list)
        mod = general % len(res_list)
        for i in range(0, len(res_list)):
            res_list[i] = {"gold_ingots": avg}
        for i in range(0, len(res_list)):
            while mod != 0:
                res_list[i] = add_ingot(res_list[i])
                mod -= 1
                i += 1
    return res_list


if __name__ == '__main__':

    res = split_booty({"gold_ingots": 3}, {"gold_ingots": 5}, {"apples": 10})
    # res = split_booty({"gold_ingots": -10}, {"gold_ingots": 0}, {"apples": 10})
    # print(res)
