from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import Group


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = [
            "name",  # El campo correcto es 'name', no 'nombre'
            "permissions",
        ]
        error_messages = {
            "name": {
                "required": "El nombre del grupo es requerido.",
                "unique": "Ya existe un grupo con este nombre.",
            },
            "permissions": {
                "required": "Debe seleccionar al menos un permiso.",
            },
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Ingrese nombre del grupo",
                "id": "id_name",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "permissions": forms.CheckboxSelectMultiple(attrs={
                "class": "text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600",
            }),
        }
        labels = {
            "name": "Nombre del Grupo",
            "permissions": "Permisos",
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name:
            return name.strip().title()  # Capitalizar y remover espacios
        return name

    def clean_permissions(self):
        permissions = self.cleaned_data.get("permissions")
        if not permissions or len(permissions) == 0:
            raise forms.ValidationError("Debe seleccionar al menos un permiso.")
        return permissions