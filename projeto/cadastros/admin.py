from django.contrib import admin

# importar as classes
from .models import Atividade, Campo, Classe, Compra, Status

# Register your models here.
admin.site.register(Campo)
admin.site.register(Atividade)
admin.site.register(Status)
admin.site.register(Classe)
admin.site.register(Compra)