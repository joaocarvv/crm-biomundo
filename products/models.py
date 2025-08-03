from django.db import models

class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Nome"
    )
    description = models.TextField(
        blank=True, 
        null=True,
        verbose_name="Descrição",
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name="Preço",
    )
    quantity = models.IntegerField(
        verbose_name="Quantidade",
        default=0,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
        )
    updated_at = models.DateTimeField(
        auto_now=True
        )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.name

