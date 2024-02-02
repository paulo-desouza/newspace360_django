from django.db import models
from content.models import Content

class EndUser(models.Model):

    first_name = models.CharField(
        verbose_name = "Primeiro Nome do seu Cliente",
        max_length = 15,
        
    )

    last_name =models.CharField(
        verbose_name = "Sobrenome do seu cliente",
        max_length = 15,
        
    )

    basic_user = models.OneToOneField(
        "basic_user.BasicUser",
        verbose_name = "Usuário",
        on_delete = models.PROTECT

    )

    content = models.ManyToManyField(
        Content,
        verbose_name = "Conteúdo permitido ao usuário",

    )

    class Meta:
        verbose_name = "CLIENTE"
        verbose_name_plural = "CLIENTES"
        db_table = "end_user"

    def __str__(self):
        return self.client_name
    
