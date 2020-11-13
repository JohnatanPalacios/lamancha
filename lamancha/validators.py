from django import forms
import emoji
import string


class CharacterValidator:
    def validate(self, password, user=None):
        if emoji.emoji_count(password):
            raise forms.ValidationError('Su contraseña no puede contener emojis')

    def get_help_text(self):
        return 'Su contraseña no puede contener emojis'


class WhitespaceValidator:
    def validate(self, password, user=None):
        if self.contains_whitespace(password):
            raise forms.ValidationError('Su contraseña no puede contener espacios en blanco')

    def get_help_text(self):
        return 'Su contraseña no puede contener espacios en blanco'

    def contains_whitespace(self, password):
        return True in [c in password for c in string.whitespace]


# alfanumerico password.isalnum() retorna false o true
# saber si una cadena contine solo minusculas islower()
# saber si una cadena contine esolo mayusculas isupper()
