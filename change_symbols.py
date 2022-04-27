def remove_symbols(string):
    return string.replace(' ', '\ ').replace('(', '\(').replace(')', '\)').replace(
        '&', '\&').replace('.', '').replace('/', '')
