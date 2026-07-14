from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_on = models.DateTimeField(
        verbose_name="Criado em",
        auto_now_add=True,
    )
    changed_on = models.DateTimeField(
        verbose_name="Alterado em",
        auto_now=True,
    )
    is_active = models.BooleanField(
        verbose_name="Ativo?",
        default=True,
    )
