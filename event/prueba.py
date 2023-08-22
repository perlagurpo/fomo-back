import locale

def get_available_locales():
    available_locales = []

    for lang in locale.locale_alias.keys():
        try:
            locale.setlocale(locale.LC_TIME, lang)
            available_locales.append((lang, locale.nl_langinfo(locale.DAY_1)))
        except locale.Error:
            continue

    return available_locales

# Llamada a la función para obtener la lista de localizaciones disponibles
locales_list = get_available_locales()
print(locales_list)

