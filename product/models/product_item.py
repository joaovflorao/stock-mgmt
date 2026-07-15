from core.schemas import BaseModel
from django.db import models
from .product_base import ProductBase
from .attribute_name import AttributeName
from django_jsonform.models.fields import JSONField


ATTRIBUTES_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "keys": {
            "key": {"type": "string", "title": "Nome"},
            "value": {"type": "string", "title": "Valor"},
        },
    },
}


class ProductItem(BaseModel):
    class Meta:
        db_table = "product_item"
        verbose_name = "Item de Produto"
        verbose_name_plural = "Itens de Produto"
        ordering = ["sku"]

    product = models.ForeignKey(
        ProductBase,
        verbose_name="Produto",
        on_delete=models.CASCADE,
        related_name="items",
    )
    sku = models.CharField(
        verbose_name="SKU",
        max_length=50,
        unique=True,
    )
    barcode = models.CharField(
        verbose_name="Código de barras",
        max_length=50,
        blank=True,
        null=True,
        unique=True,
    )
    attributes = JSONField(
        verbose_name="Características",
        schema=ATTRIBUTES_SCHEMA,
        default=list,
        blank=True,
    )
    cost_price = models.DecimalField(
        verbose_name="Preço de custo",
        max_digits=12,
        decimal_places=2,
        default=0,
    )
    sale_price = models.DecimalField(
        verbose_name="Preço de venda",
        max_digits=12,
        decimal_places=2,
        default=0,
    )
    weight = models.DecimalField(
        verbose_name="Peso",
        max_digits=8,
        decimal_places=3,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.product.name} ({self.sku})"

    def save(self, *args, **kwargs):
        self.attributes = self._normalize_attributes(self.attributes)
        super().save(*args, **kwargs)

    @staticmethod
    def _normalize_attributes(attributes) -> list:
        normalized = []
        for pair in attributes:
            clean_key = pair["key"].strip().title()
            clean_value = str(pair["value"]).strip()
            normalized.append({"key": clean_key, "value": clean_value})
            AttributeName.objects.get_or_create(name=clean_key)
        return normalized