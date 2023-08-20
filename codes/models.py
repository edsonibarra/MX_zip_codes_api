from django.db import models


class Code(models.Model):
    d_codigo = models.CharField(max_length=200)
    d_asenta = models.CharField(max_length=200)
    d_tipo_asenta = models.CharField(max_length=200)
    D_mnpio = models.CharField(max_length=200)
    d_estado = models.CharField(max_length=200)
    d_ciudad = models.CharField(max_length=200)
    d_CP = models.CharField(max_length=200)
    c_estado = models.CharField(max_length=200)
    c_oficina = models.CharField(max_length=200)
    c_CP = models.CharField(max_length=200)
    c_tipo_asenta = models.CharField(max_length=200)
    c_mnpio = models.CharField(max_length=200)
    id_asenta_cpcons = models.CharField(max_length=200)
    d_zona = models.CharField(max_length=200)
    c_cve_ciudad = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.d_codigo