from django.contrib.auth.models import User
from django.views.generic.edit import CreateView


# Create your views here.
class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    model = User
    fields = ['username', 'email', 'password']