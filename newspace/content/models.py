from django.db import models

class Content(models.Model):

    address = models.CharField(
        max_length = 50,
        verbose_name = "Endereço da Propriedade"
    )

    matterport_embed = models.TextField(
        max_length = 1000,
        verbose_name = "Codigo da Matterport"
    )

    photo1 = models.ImageField(
        upload_to ='photos/', blank=True,
        verbose_name= "Primeira foto (Usada como icone do produto)")

    photo2 = models.ImageField(
        upload_to ='photos/', blank=True,
        verbose_name= "Segunda Foto")

    photo3 = models.ImageField(
        upload_to ='photos/', blank=True,
        verbose_name= "Terceira Foto")


    video_link1 = models.CharField(
        max_length = 300,
        verbose_name = "Link para o video no youtube.",
        blank=True,
    )

    video_link2 = models.CharField(
        max_length = 300,
        verbose_name = "Link para o video no youtube.",
        blank=True,
    )

    video_link3 = models.CharField(
        max_length = 300,
        verbose_name = "Link para o video no youtube.",
        blank=True,
    )

    download_link = models.CharField(
        max_length = 300,
        verbose_name = "Link para o cliente fazer o download de todas as midias.",
        blank=True,
    )


    class Meta:
        verbose_name = "Conteúdo"
        verbose_name_plural = "Conteúdo"
        db_table = "content"


    def __str__(self):
        return self.address