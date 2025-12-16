def flatten_list(nested_list: list) -> list:
    new_list = []
    for element in nested_list:
        if isinstance(element, list):
            new_list.extend(flatten_list(element))
        else:
            new_list.append(element)
    return new_list
