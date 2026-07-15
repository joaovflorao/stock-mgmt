from core.schemas import BaseModel
from django.db import models


class ProductBrand(BaseModel):
    class Meta:
        db_table = "product_brand"
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    name = models.CharField(
        verbose_name="Nome",
        max_length=255,
        unique=True,
    )

    def __str__(self) -> str:
        return str(self.name)
