
from django.contrib import messages
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from applications.security.forms.group_permission import GroupPForm
from applications.security.forms.menu import MenuForm
from applications.security.forms.module import ModuleForm
from applications.security.models import Menu, Module, GroupModulePermission
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q


class GroupPermissionListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'security/group_permission/list.html'
    model = GroupModulePermission
    context_object_name = 'group_permissions'  # <== esta línea debe tener la misma indentación

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1 is not None:
            self.query.add(Q(name__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('security:group_permission_create')
        print(context['permissions'])
        return context


class GroupPermissionCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = GroupModulePermission
    form_class = GroupPForm
    template_name = "security/group_permission/form.html"
    success_url = reverse_lazy("security:group_permission_list")
    permission_required = "add_groupmodulepermission"

    def form_valid(self, form):
        group_id = self.request.POST.get("group") or self.request.GET.get("group")
        if group_id:
            form.instance.group_id = group_id
            return super().form_valid(form)
        else:
            form.add_error("group", "Debe seleccionar un grupo.")
            return self.form_invalid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Group Permission'
        context['back_url'] = self.success_url
        return context

class GroupPermissionUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = GroupModulePermission
    template_name = 'security/group_permission/form.html'
    form_class = GroupPForm
    success_url = reverse_lazy('security:group_permission_list')
    permission_required = 'change_groupmodulepermission'  #  Correcto


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Group Permission'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        menu = self.object
        messages.success(self.request, f"Éxito al actualizar el Group Permission {menu.group}.")
        return response


class GroupPermissionDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = GroupModulePermission
    template_name = 'core/delete.html'
    success_url = reverse_lazy('security:group_permission_list')
    permission_required = 'delete_groupmodulepermission'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Menu'
        context['description'] = f"¿Desea eliminar el Group Permission: {self.object.group}?"
        context['back_url'] = self.success_url
        return context

    
    def form_valid(self, form):
        # Guardar info antes de eliminar
        menu_name = self.object.group
        
        # Llamar al delete del padre
        response = super().form_valid(form)
        
        # Agregar mensaje
        messages.success(self.request, f"Éxito al eliminar lógicamente el Group Permission {menu_name}.")
        
        return response