import re
from django import forms
from django.forms import ModelForm
from applications.security.models import User
from django.contrib.auth.hashers import make_password

class UserForm(ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Ingrese contraseña",
            "id": "id_password",
            "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
        }),
        required=True,  #
        label="Contraseña",
    )
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "dni",
            "image",
            "direction",
            "phone",
            "groups",
            "user_permissions",
            "password",
        ]
        error_messages = {
            "username": {
                "unique": "Ya existe un usuario con este nombre de usuario.",
                "required": "El nombre de usuario es requerido.",
            },
            "email": {
                "unique": "Ya existe un usuario con este email.",
                "invalid": "Ingrese un email válido.",
                "required": "El email es requerido.",
            },
            "dni": {
                "unique": "Ya existe un usuario con esta cédula.",
                "required": "La cédula es requerida.",
            },
        }
        widgets = {
            "username": forms.TextInput(attrs={
                "placeholder": "Ingrese nombre de usuario",
                "id": "id_username",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Ingrese email",
                "id": "id_email",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "first_name": forms.TextInput(attrs={
                "placeholder": "Ingrese nombre",
                "id": "id_first_name",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "last_name": forms.TextInput(attrs={
                "placeholder": "Ingrese apellido",
                "id": "id_last_name",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "dni": forms.TextInput(attrs={
                "placeholder": "Ingrese cédula",
                "id": "id_dni",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "image": forms.FileInput(attrs={
                "id": "id_image",
                "class": "block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400",
            }),
            "direction": forms.TextInput(attrs={
                "placeholder": "Ingrese dirección",
                "id": "id_direction",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "Ingrese teléfono",
                "id": "id_phone",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "groups": forms.CheckboxSelectMultiple(attrs={
                "class": "text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600",
            }),
            "permissions": forms.CheckboxSelectMultiple(attrs={
                "class": "text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600",
            }),
        }
        labels = {
            "username": "Nombre de Usuario",
            "email": "Email",
            "first_name": "Nombre",
            "last_name": "Apellido",
            "dni": "Cédula",
            "image": "Foto Usuario",
            "direction": "Dirección",
            "phone": "Teléfono",
            "groups": "Grupos",
            "permissions": "Permisos",
            "password": "contraseña",
        }

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username:
            return username.lower()
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email:
            return email.lower()
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if first_name:
            return first_name.title()
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if last_name:
            return last_name.title()
        return last_name

    def clean_dni(self):
        dni = self.cleaned_data.get("dni")
        if dni:
            # Remover espacios y caracteres especiales
            dni = re.sub(r'[^0-9]', '', dni)
            
            # Validar que tenga 10 dígitos (Ecuador)
            if len(dni) != 10:
                raise forms.ValidationError("La cédula debe tener 10 dígitos.")
            
            # Validar algoritmo de cédula ecuatoriana
            if not self._validate_ecuadorian_dni(dni):
                raise forms.ValidationError("La cédula ingresada no es válida.")
                
        return dni

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if phone:
            # Remover espacios y caracteres especiales excepto + y -
            phone = re.sub(r'[^\d+\-]', '', phone)
            
            # Validar formato de teléfono
            if not re.match(r'^[\d+\-]{7,15}$', phone):
                raise forms.ValidationError("Ingrese un número de teléfono válido.")
                
        return phone

    def _validate_ecuadorian_dni(self, dni):
        """Valida cédula ecuatoriana usando el algoritmo oficial"""
        try:
            # Coeficientes para validación
            coefficients = [2, 1, 2, 1, 2, 1, 2, 1, 2]
            
            # Calcular suma
            total = 0
            for i in range(9):
                digit = int(dni[i])
                result = digit * coefficients[i]
                if result >= 10:
                    result = result - 9
                total += result
            
            # Calcular dígito verificador
            remainder = total % 10
            check_digit = 0 if remainder == 0 else 10 - remainder
            
            return check_digit == int(dni[9])
        except (ValueError, IndexError):
            return False
        from django.contrib.auth.hashers import make_password

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")

        if password:
            user.password = make_password(password)
        elif user.pk:
        # En edición, si no se ingresa nueva contraseña, se mantiene la existente
            old_password = User.objects.get(pk=user.pk).password
            user.password = old_password

        if commit:
            user.save()
            self.save_m2m()
        return user