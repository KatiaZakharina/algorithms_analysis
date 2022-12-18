def dict_to_list(dict):
    dictlist = []

    for key, value in dict.items():
        temp = [key, value]
        dictlist.append(temp)

    return dictlist
