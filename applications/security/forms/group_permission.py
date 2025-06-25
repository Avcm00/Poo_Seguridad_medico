from django import forms
from django.forms import ModelForm
from applications.security.models import GroupModulePermission


class GroupPForm(ModelForm):
    class Meta:
        
        model = GroupModulePermission
        fields = ["group", "module", "permissions"]
        
        labels = {
            "group": "Grupo",
            "module": "Módulo",
            "permissions": "Permisos",
        }

        error_messages = {
            "group": {
                "required": "Debe seleccionar un grupo.",
            },
            "module": {
                "required": "Debe seleccionar un módulo.",
            },
            "permissions": {
                "required": "Debe seleccionar al menos un permiso.",
            },
        }

        widgets = {
            "group": forms.Select(attrs={
                "id": "id_group",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 "
                         "dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 "
                         "dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "module": forms.Select(attrs={
                "id": "id_module",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 "
                         "dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 "
                         "dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "permissions": forms.CheckboxSelectMultiple(attrs={
                "class": "text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 "
                         "dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 "
                         "dark:bg-gray-700 dark:border-gray-600",
            }),
        }

    def clean_group(self):
        group = self.cleaned_data.get("group")
        if not group:
            raise forms.ValidationError("Debe seleccionar un grupo.")
        return group

    def clean_module(self):
        module = self.cleaned_data.get("module")
        if not module:
            raise forms.ValidationError("Debe seleccionar un módulo.")
        return module

    def clean_permissions(self):
        permissions = self.cleaned_data.get("permissions")
        if not permissions:
            raise forms.ValidationError("Debe seleccionar al menos un permiso.")
        return permissions
