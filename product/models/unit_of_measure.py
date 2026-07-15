from core.schemas import BaseModel
from django.db import models


class UnitOfMeasure(BaseModel):
    class Meta:
        db_table = "product_unit"
        verbose_name = "Unidade de Medida"
        verbose_name_plural = "Unidades de Medida"

    name = models.CharField(
        verbose_name="Nome",
        max_length=50,
    )
    abbreviation = models.CharField(
        verbose_name="Abreviação",
        max_length=10,
        unique=True,
    )

    def __str__(self) -> str:
        return str(self.abbreviation)
