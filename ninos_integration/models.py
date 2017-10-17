from django.db import models
from django.db import models
from sitioninos.models import Nino
from cms.models.pluginmodel import CMSPlugin


class NinoPluginModel(CMSPlugin):
    nino = models.ForeignKey(Nino)
    def __unicode__(self):
        return self.nino.titulo

class Hola(CMSPlugin):
    nombre_invitado = models.CharField(max_length=50, default='Invitado')
