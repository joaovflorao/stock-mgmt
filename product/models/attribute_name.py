from core.schemas import BaseModel
from django.db import models


class AttributeName(BaseModel):
    class Meta:
        db_table = "product_attribute_name"
        verbose_name = "Nome de Atributo"
        verbose_name_plural = "Nomes de Atributo"

    name = models.CharField(
        verbose_name="Nome",
        max_length=100,
        unique=True,
    )

    def __str__(self) -> str:
        return str(self.name)
