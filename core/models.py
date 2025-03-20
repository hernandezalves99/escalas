from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    TIPO_FUNCAO = (
        ("1", "Bateria"),
        ("2", "Guitarra"),
        ("3", "Vocal"),
        ("4", "Teclado"),
        ("5", "Baixo"),
        ("6", "Violao"),
        ("7", "Som"),
        ("8", "Projetor"),
        ("9", "Fotofilm"),
        ("10", "Live"),
        ("11", "Total Midia")
        
    )

    TIPO_ATUACAO = (
        ("1", "Louvor"),
        ("2", "Midia"),
        ("3", "Midia e Louvor")
        
    )
    #first_name = models.CharField(max_length=50, blank=False, null=True)
    endereco = models.TextField(blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    #mininsterio = models.CharField(max_length=50,blank=True, null=True)
    #funcao_1 = models.CharField(max_length=50,blank=True, null=True, choices=TIPO_FUNCAO, verbose_name="1ª Função")
    #funcao_2 = models.CharField(max_length=50,blank=True, null=True, choices=TIPO_FUNCAO, verbose_name="2ª Função")
    atuacao = models.CharField(max_length=50,blank=True, null=True, choices=TIPO_ATUACAO, verbose_name="Atuação")
    birthday = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento")

    def __str__(self):
        return f"{self.username} - {self.first_name}"
    


class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    participantes = models.ManyToManyField(Usuario, through="Escala")

    def __str__(self):
        return f"{self.titulo}- {self.data}" 
    
class Escala(models.Model):
    FUNCAO_CHOICES = (
        ("1", "Bateria"),
        ("2", "Guitarra"),
        ("3", "Vocal"),
        ("4", "Teclado"),
        ("5", "Baixo"),
        ("6", "Violao"),
        ("7", "Som"),
        ("8", "Projetor"),
        ("9", "Fotofilm"),
        ("10", "Live")
        
    )
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="escalas")
    participante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="participantes", blank=True, null=True)
    funcao = models.CharField(max_length=10, choices=FUNCAO_CHOICES, blank=True, null=True, verbose_name="Função")

    def __str__(self):
        return f"Escalas para {self.evento.titulo}"
