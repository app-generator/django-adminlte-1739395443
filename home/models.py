# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Clientes(models.Model):

    #__Clientes_FIELDS__
    apelido = models.TextField(max_length=255, null=True, blank=True)
    razão social = models.TextField(max_length=255, null=True, blank=True)
    tipo de cliente = models.CharField(max_length=255, null=True, blank=True)
    plano = models.ForeignKey(Planos, on_delete=models.CASCADE)
    pacote = models.ForeignKey(Pacotes, on_delete=models.CASCADE)

    #__Clientes_FIELDS__END

    class Meta:
        verbose_name        = _("Clientes")
        verbose_name_plural = _("Clientes")


class Planos(models.Model):

    #__Planos_FIELDS__
    usuarios = models.IntegerField(null=True, blank=True)
    visualizacao = models.IntegerField(null=True, blank=True)
    armazenamento = models.IntegerField(null=True, blank=True)
    streaming = models.IntegerField(null=True, blank=True)
    salas_virtuais = models.IntegerField(null=True, blank=True)
    midias_embed = models.IntegerField(null=True, blank=True)
    paginas = models.IntegerField(null=True, blank=True)
    apps_android_mobile = models.BooleanField()
    apps_ios_mobile = models.BooleanField()
    apps_ipad = models.BooleanField()
    apps_chromecast = models.BooleanField()
    apps_android_tv = models.BooleanField()
    apps_ios_tv = models.BooleanField()
    apps_roku = models.BooleanField()
    apps_firetv = models.BooleanField()
    apps_smart_samsung = models.BooleanField()
    apps_smart_lg = models.BooleanField()
    apps_appmembers = models.BooleanField()

    #__Planos_FIELDS__END

    class Meta:
        verbose_name        = _("Planos")
        verbose_name_plural = _("Planos")


class Pacotes(models.Model):

    #__Pacotes_FIELDS__
    apelido = models.TextField(max_length=255, null=True, blank=True)
    canais = models.BooleanField()
    filmes = models.BooleanField()

    #__Pacotes_FIELDS__END

    class Meta:
        verbose_name        = _("Pacotes")
        verbose_name_plural = _("Pacotes")


class Servidor(models.Model):

    #__Servidor_FIELDS__
    nome = models.TextField(max_length=255, null=True, blank=True)
    servidor primario url = models.TextField(max_length=255, null=True, blank=True)
    servidor primario token = models.TextField(max_length=255, null=True, blank=True)
    servidor primario flussonic = models.BooleanField()
    servidor secundario url = models.TextField(max_length=255, null=True, blank=True)
    servidor secundario token = models.TextField(max_length=255, null=True, blank=True)
    servidor secundario flussonic = models.BooleanField()

    #__Servidor_FIELDS__END

    class Meta:
        verbose_name        = _("Servidor")
        verbose_name_plural = _("Servidor")


class Tipo Do Fluxo(models.Model):

    #__Tipo Do Fluxo_FIELDS__
    nome = models.TextField(max_length=255, null=True, blank=True)

    #__Tipo Do Fluxo_FIELDS__END

    class Meta:
        verbose_name        = _("Tipo Do Fluxo")
        verbose_name_plural = _("Tipo Do Fluxo")


class Canal(models.Model):

    #__Canal_FIELDS__
    tipo do fluxo = models.ForeignKey(Tipo do fluxo, on_delete=models.CASCADE)
    servidor = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    url = models.TextField(max_length=255, null=True, blank=True)
    epg = models.IntegerField(null=True, blank=True)
    codigo epg = models.TextField(max_length=255, null=True, blank=True)
    segurança = models.IntegerField(null=True, blank=True)
    miniatura = models.TextField(max_length=255, null=True, blank=True)
    poster = models.TextField(max_length=255, null=True, blank=True)
    status = models.BooleanField()

    #__Canal_FIELDS__END

    class Meta:
        verbose_name        = _("Canal")
        verbose_name_plural = _("Canal")



#__MODELS__END
