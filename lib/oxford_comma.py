# def oxford_comma(items):
#     # return ' and '.join(items)
#     return ' and '.join([', '.join(items[:-1]), items[-1]] if len(items) > 2 else items)


def oxford_comma(items):
    if len(items) > 2:
        return ', '.join(items[:-1]) + ', and ' + items[-1]
    elif len(items) == 2:
        return ' and '.join(items)
    elif len(items) == 1:
        return items[0]
    else:
        return ''