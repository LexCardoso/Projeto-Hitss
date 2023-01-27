from django.contrib.auth.models import User
from django.db import models


def user_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'usuario_{0}/{1}'.format(instance.user.id, filename)

# Create your models here.
class Campo(models.Model): # FORNECEDOR
    nome = models.CharField(max_length=50)
    situacao = models.CharField(max_length=150, verbose_name="Situação")
    id_sap = models.CharField(max_length=150, verbose_name="Id SAP")
    id_servico = models.CharField(max_length=150, verbose_name="Id Serviço")
    centro = models.CharField(max_length=150, verbose_name="Centro")
    cnae = models.CharField(max_length=150, verbose_name="Cnae")
    razao_social = models.CharField(max_length=150, verbose_name="Razão Social")
    cnpj = models.CharField(max_length=150, verbose_name="CNPJ")

    def __str__(self):
        return "{} ({})".format(self.nome, self.razao_social)

class Status(models.Model): # VAGA
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    #FK AQUI

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)

class Classe(models.Model): # PROJETO
    nome = models.CharField(max_length=50)
    gestor = models.CharField(max_length=150, verbose_name="Gestor")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")

    def __str__(self):
        return "{} {} ({})".format(self.nome, self.gestor, self.descricao)

class Atividade(models.Model): # RECURSO
    nome = models.CharField(max_length=150, verbose_name="Nome", blank=True)
    descricao = models.CharField(max_length=150, verbose_name="Descrição", blank=True)
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT, verbose_name="Fornecedor")#FK Fornecedor
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Vaga")#FK VAGA
    classe = models.ForeignKey(Classe, on_delete=models.PROTECT, verbose_name="Projeto")#FK PROJETO
    

    def __str__(self):
        return "{} - {} ({})".format(self.nome, self.descricao, self.campo.nome)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["nome", "descricao"], name="unica_num_atividade_campo")
        ]

class Compra(models.Model): # PROJETO
    Torre = models.CharField(max_length=50)
    Fornecedor = models.CharField(max_length=150)
    Competencia = models.CharField(max_length=150)
    Tipo = models.CharField(max_length=50)
    Valor = models.CharField(max_length=50)


    def __str__(self):
        return "{} - ({})".format(self.Torre, self.Fornecedor)



class Campus(models.Model):
    nome = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50, verbose_name="Cidade!")
    telefone = models.CharField(max_length=150, verbose_name="Telefone!")

    def __str__(self):
        return "{} {} ({})".format(self.nome, self.cidade, self.telefone)

class Servidor(models.Model):
    nome_completo = models.CharField(max_length=100)
    siape = models.CharField(max_length=10)
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}  ({})".format(self.numero, self.descricao, self.campo.nome, self.data_final)


class Progressao(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.PROTECT, verbose_name= 'Classe pretendida!')
    data_inicial = models.DateField()
    data_final = models.DateField()
    observacao = models.CharField(max_length=255, verbose_name= 'Observacao!')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{} -> {} | {} ({})".format(self.usuario, self.classe, self.data_inicial, self.data_final)

class Comprovante(models.Model):
    progressao = models.ForeignKey(Progressao, on_delete=models.PROTECT, verbose_name= 'Progressao!')
    atividade = models.ForeignKey(Atividade, on_delete=models.PROTECT)
    quantidade = models.DecimalField(decimal_places=2, max_digits=5)
    data = models.DateField()
    data_final = models.DateField()
    arquivo = models.FileField(upload_to=user_path)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return "[{}] {} - {}/{}".format(self.pk, self.usuario, self.progressao, self.atividade)

class Validacao(models.Model):
    comprovante = models.ForeignKey(Comprovante, on_delete=models.PROTECT)
    validado_em = models.DateField(auto_now_add=True)
    validado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    quantidade = models.DecimalField(decimal_places=2, max_digits=5)
    justificativa = models.TextField(max_length=255)

    def __str__(self):
        return "[{}] pontuacao!: {}/{} por {}".format(self.comprovante.pk, self.quantidade, self.comprovante.quantidade, self.usuario)

