from books.models import Language

languages = ('árabe', 'bielorruso', 'búlgaro', 'catalán', 'checo', 'danés', 'alemán', 'griego', 'inglés', 'español',
             'estonio', 'finés', 'francés', 'irlandés', 'croata', 'húngaro', 'indonesio', 'islandés', 'italiano',
             'hebreo', 'japonés', 'coreano', 'lituano', 'letón', 'macedonio', 'malayo', 'maltés', 'neerlandés',
             'noruego', 'polaco', 'portugués', 'rumano', 'ruso', 'eslovaco', 'eslovenio', 'albanés', 'serbio', 'sueco',
             'tailandés', 'turco', 'ucranio', 'vietnamita', 'chino')

for language in languages:
    l = Language()
    l.language = language.title()
    l.save()
