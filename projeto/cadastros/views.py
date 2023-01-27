from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import (Atividade, Campo, Campus, Classe, Compra, Progressao,
                     Status)

# Create your views here.

#class BaseView(View):
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['current_path'] = self.request.path
#        path = context['current_path']
#        path_list = path.split('/')
#        context['current_path'] = path_list[2].capitalize()
#        return context

class CampoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):#FORNECEDOR
    group_required = [u'ICPO-admin']
    login_url = reverse_lazy('login')
    model = Campo
    fields = ['nome','situacao','id_sap','id_servico','centro','cnae','razao_social','cnpj']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastrar Fornecedores(Campos)"
        context['descricao'] = "Preencha os dados para cadastrar um Fornecedor(Campo)"
        context['botao'] = "Cadastrar"

        return context

class AtividadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):#RECURSO
    group_required = [u'ICPO-admin']
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['nome', 'descricao', 'campo', 'status', 'classe']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastrar Recurso(Atividade)"
        context['descricao'] = "Preencha os dados para cadastrar um Recurso(Atividade)"
        context['botao'] = "Cadastrar"

        return context

class StatusCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView): #VAGA
    group_required = [u'ICPO-admin']
    login_url = reverse_lazy('login')
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-status')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastrar Vaga(Status)"
        context['descricao'] = "Preencha os dados para cadastrar um Vaga(Status)"
        context['botao'] = "Cadastrar"

        return context

class ClasseCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView): # PROJETO
    group_required = [u'ICPO-admin']
    login_url = reverse_lazy('login')
    model = Classe
    fields = ['nome', 'gestor', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-classes')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastrar Projeto(Classe)"
        context['descricao'] = "Preencha os dados para cadastrar um Projeto(Classe)"
        context['botao'] = "Cadastrar"

        return context

class ProgressaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Progressao
    fields = ['classe', 'data_inicial', 'data_final', 'observacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-progressao')

    def form_valid(self, form):

        #antes do super nao foi criado o objeto nem salvo no banco
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url

class CampusCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u'ICPO-admin']
    login_url = reverse_lazy('login')
    model = Campus
    fields = ['cidade', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Campus"
        context['botao'] = "Cadastrar"

        return context

################################ UPDATE ################################

class CampoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u'ICPO-admin', u'Gestores']
    login_url = reverse_lazy('login')
    model = Campo
    fields = ['nome', 'situacao','id_sap','id_servico','centro','cnae','razao_social','cnpj']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

    def get_context_data(self, *args, **kwargs):
                context = super().get_context_data(*args, **kwargs)

                context['titulo'] = "Editar Fornecedor(Campo)"
                context['descricao'] = "Preencha os dados para editar o Fornecedor(Campo)"
                context['botao'] = "Salvar"

                return context

class AtividadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u'ICPO-admin', u'Gestores']
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['nome', 'descricao', 'campo', 'status', 'classe']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')

    def get_context_data(self, *args, **kwargs):
                context = super().get_context_data(*args, **kwargs)

                context['titulo'] = "Editar Recurso(Atividade)"
                context['descricao'] = "Preencha os dados para editar o Recurso(Atividade)"
                context['botao'] = "Salvar"

                return context

class StatusUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u'ICPO-admin', u'Gestores']
    login_url = reverse_lazy('login')
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-status')

    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)

            context['titulo'] = "Editar Vaga(Status)"
            context['descricao'] = "Preencha os dados para editar a Vaga(Status)"
            context['botao'] = "Salvar"

            return context

class ClasseUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u'ICPO-admin', u'Gestores']
    login_url = reverse_lazy('login')
    model = Classe
    fields = ['nome', 'gestor', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-classes')

    def get_context_data(self, *args, **kwargs):
                context = super().get_context_data(*args, **kwargs)

                context['titulo'] = "Editar Projeto(Classe)"
                context['descricao'] = "Preencha os dados para editar a Projeto(Classe)"
                context['botao'] = "Salvar"

                return context

class CampusUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u'ICPO-admin', u'Gestores']
    login_url = reverse_lazy('login')
    model = Campus
    fields = ['cidade', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Cadastro de Campus"
        context['botao'] = "Salvar"

        return context

class ProgressaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u'ICPO-admin', u'Gestores']
    login_url = reverse_lazy('login')
    model = Progressao
    fields = ['classe', 'data_inicial', 'data_final', 'observacao']
    template_name = 'cadastros/form.html'
    uccess_url = reverse_lazy('listar-progressao')

    def get_object(self, queryset=None):
        
        self.object = get_object_or_404(Progressao, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

################################ DELETE ################################

class CampoDelete(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    group_required = [u'ICPO-admin']
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campos')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Campo, pk=self.kwargs['pk'])
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluir Fornecedor(Campo)"
        context['descricao'] = "Excluir Fornecedor(Campo)?"
        context['botao'] = "Excluir"
        return context

class AtividadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = [u'ICPO-admin']
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividades')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Atividade, pk=self.kwargs['pk'])
        return self.object

    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)

            context['titulo'] = "Excluir Recurso(Atividade)"
            #context['descricao'] = "Excluir a Vaga(Status)?"
            context['botao'] = "Excluir"

            return context

class ClasseDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = [u'ICPO-admin']
    login_url = reverse_lazy('login')
    model = Classe
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-classes')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Classe, pk=self.kwargs['pk'])
        return self.object

    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)

            context['titulo'] = "Excluir Projeto(Classe)"
            #context['descricao'] = "Excluir a Vaga(Status)?"
            context['botao'] = "Excluir"

            return context

class StatusDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = [u'ICPO-admin']
    login_url = reverse_lazy('login')
    model = Status
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-status')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Status, pk=self.kwargs['pk'])
        return self.object

    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)

            context['titulo'] = "Excluir Vaga(Status)"
            #context['descricao'] = "Excluir a Vaga(Status)?"
            context['botao'] = "Excluir"

            return context

class ProgressaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = [u'ICPO-admin']
    login_url = reverse_lazy('login')
    model = Progressao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-progressao')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Progressao, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
################################ LISTA ################################

class CampoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u'ICPO-admin', u'Gestores', u'Fornecedores']
    login_url = reverse_lazy('login')
    fields = ['nome','situacao','id_sap','id_servico','centro']
    model = Campo
    template_name = 'cadastros/listas/campo.html'



class AtividadeList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u'ICPO-admin', u'Gestores', u'Fornecedores']
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'



class ClasseList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u'ICPO-admin', u'Gestores', u'Fornecedores']
    login_url = reverse_lazy('login')
    model = Classe
    template_name = 'cadastros/listas/classes.html'
    fields = ['nome', 'gestor', 'descricao']

class StatusList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u'ICPO-admin', u'Gestores', u'Fornecedores']
    login_url = reverse_lazy('login')
    model = Status
    template_name = 'cadastros/listas/status.html'

class CompraList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u'ICPO-admin', u'Gestores', u'Fornecedores']
    login_url = reverse_lazy('listar-compra')
    model = Compra
    template_name = 'cadastros/listas/compra_servico.html'




class ProgressaoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u'ICPO-admin', u'Gestores', u'Fornecedores']
    login_url = reverse_lazy('login')
    model = Progressao
    template_name = 'cadastros/listas/progressao.html'

    def get_queryset(self):
        self.object_list = Progressao.objects.filter(usuario=self.request.user)
        return self.object_list