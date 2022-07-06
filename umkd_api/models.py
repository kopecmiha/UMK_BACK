from django.db import models
from django.utils.translation import gettext_lazy as _


class Competence(models.Model):
    code = models.CharField(_("Code"), blank=True, unique=True, max_length=10)
    description = models.TextField(verbose_name=_("Description"), blank=True)
    objects = models.Manager()

    class Meta:
        verbose_name = _("Competence")
        verbose_name_plural = _("Competences")

    def __str__(self):
        return self.code


class Indicator(models.Model):
    code = models.CharField(_("Code"), blank=True, unique=True, max_length=10)
    description = models.TextField(verbose_name=_("Description"), blank=True)
    competence = models.ForeignKey(
        to=Competence,
        on_delete=models.CASCADE,
        verbose_name=_("Competence"),
    )
    type = models.CharField(_("Type"), blank=True, max_length=20)
    objects = models.Manager()

    class Meta:
        verbose_name = _("Indicator")
        verbose_name_plural = _("Indicator")
