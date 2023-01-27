from django.urls import path

from .views import (AtividadeCreate, AtividadeDelete, AtividadeList,
                    AtividadeUpdate, CampoCreate, CampoDelete, CampoList,
                    CampoUpdate, CampusCreate, ClasseCreate, ClasseDelete,
                    ClasseList, ClasseUpdate, CompraList, ProgressaoCreate,
                    ProgressaoDelete, ProgressaoList, ProgressaoUpdate,
                    StatusCreate, StatusDelete, StatusList, StatusUpdate)

'''
from .views import (AtividadeCreate, CampoCreate, CampusCreate, ClasseCreate,
                    StatusCreate)

from .views import (AtividadeUpdate, CampoUpdate)

from .views import (AtividadeDelete, CampoDelete)

from .views import (CampoList, AtividadeList)
'''

urlpatterns = [
    #path('endereco/', MinhaView.as_view(), name='nome-da-url'),
    ##path('', IndexView.as_view(), name='inicio'),
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),
    path('cadastrar/classe/', ClasseCreate.as_view(), name='cadastrar-classe'),
    path('cadastrar/status/', StatusCreate.as_view(), name='cadastrar-status'),
    #path('cadastrar/campus/', CampusCreate.as_view(), name='cadastrar-campus'),
    #path('cadastrar/progressao/', ProgressaoCreate.as_view(), name="cadastrar-progressao"),

    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name="editar-campo"),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name="editar-atividade"),
    path('editar/classe/<int:pk>/', ClasseUpdate.as_view(), name="editar-classe"),
    path('editar/status/<int:pk>/', StatusUpdate.as_view(), name="editar-status"),
    #path('editar/progressao/<int:pk>/', ProgressaoUpdate.as_view(), name="editar-progressao"),

    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name="excluir-campo"),
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name="excluir-atividade"),
    path('excluir/classe/<int:pk>/', ClasseDelete.as_view(), name="excluir-classe"),
    path('excluir/status/<int:pk>/', StatusDelete.as_view(), name="excluir-status"),
    #path('excluir/progressao/<int:pk>/', ProgressaoDelete.as_view(), name="excluir-progressao"),

    path('listar/campo/', CampoList.as_view(), name="listar-campos"),
    path('listar/atividade/', AtividadeList.as_view(), name="listar-atividades"),
    path('listar/classe/', ClasseList.as_view(), name="listar-classes"),
    path('listar/status/', StatusList.as_view(), name="listar-status"),
    path('listar/compra/', CompraList.as_view(), name="listar-compra"),
    #path('listar/progressao/', ProgressaoList.as_view(), name="listar-progressao"),
]