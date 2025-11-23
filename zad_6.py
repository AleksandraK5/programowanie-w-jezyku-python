def newlist(a:list, b:list) -> list:
    combined_list = a+b
    unique_list = set(combined_list)
    list_c = []
    for item in unique_list:
        list_c.append(item**3)
    return list_c
