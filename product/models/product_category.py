from core.schemas import BaseModel
from django.db import models


class ProductCategory(BaseModel):
    class Meta:
        db_table = "product_category"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    name = models.CharField(
        verbose_name="Nome",
        max_length=255,
        unique=True,
    )
    parent = models.ForeignKey(
        "self",
        verbose_name="Categoria pai",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="subcategories",
    )

    def __str__(self) -> str:
        return str(self.name)
