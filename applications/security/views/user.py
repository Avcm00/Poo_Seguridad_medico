
from django.contrib import messages
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from applications.security.forms.menu import MenuForm
from applications.security.forms.user import UserForm
from applications.security.models import Menu, Module, User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q


class UserListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'security/user/list.html'
    model = User
    context_object_name = 'users'
    permission_required = 'view_user'

    def get_queryset(self):
       q1 = self.request.GET.get('q')
       self.query = Q()  # Inicializa la consulta
       if q1 is not None:
           self.query.add(Q(username__icontains=q1) | Q(first_name__icontains=q1) | Q(last_name__icontains=q1), Q.OR)
       queryset = self.model.objects.filter(self.query).order_by('id')
       print(queryset)  # Verifica los datos
       return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('security:user_create')
        print(context['permissions'])
        return context


class UserCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = User
    template_name = 'security/user/form.html'
    form_class = UserForm
    success_url = reverse_lazy('security:user_list')
    permission_required = 'add_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar User'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        menu = self.object
        messages.success(self.request, f"Éxito al crear el User {menu.username}.")
        return response


class UserUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = User
    template_name = 'security/user/form.html'
    form_class = UserForm
    success_url = reverse_lazy('security:user_list')
    permission_required = 'change_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar User'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        menu = self.object
        messages.success(self.request, f"Éxito al actualizar el User {menu.username}.")
        return response


class UserDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = User
    template_name = 'core/delete.html'
    success_url = reverse_lazy('security:user_list')
    permission_required = 'delete_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar User'
        context['description'] = f"¿Desea eliminar el user: {self.object.username}?"
        context['back_url'] = self.success_url
        return context

    
    def form_valid(self, form):
        # Guardar info antes de eliminar
        menu_name = self.object.username
        
        # Llamar al delete del padre
        response = super().form_valid(form)
        
        # Agregar mensaje
        messages.success(self.request, f"Éxito al eliminar lógicamente el User {menu_name}.")
        
        return response