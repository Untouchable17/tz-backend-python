from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=150, verbose_name=_("Название"))
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="subcategories",
        verbose_name=_("Родительская категория"),
    )
    url = models.CharField(max_length=150, blank=True, verbose_name=_("Ссылка"))

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("menu_app:category_detail", args=[str(self.id)])

    def get_elder_ids(self):
        return self.get_ancestors().values_list("id", flat=True)