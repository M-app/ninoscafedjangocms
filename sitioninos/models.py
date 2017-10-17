from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.core.urlresolvers import reverse
# Create your models here.
etapas = (
	('Primaria','Primaria'),
	('Básico','Básico'),
	('Diversificado','Diversificado'),
)

def upload_location(instance, filename):
	filename, extension = filename.split('.')
	return "%s/%s.%s" %(instance.slug, 'foto', extension)

class Nino(models.Model):
	apellidos 	= models.CharField(max_length = 50)
	nombres 	= models.CharField(max_length = 50)
	etapa 		= models.CharField(max_length = 15,choices = etapas, default = 'Primaria')
	historia 	= models.TextField(max_length = 1500)
	foto		= models.ImageField(upload_to = upload_location,
									null = True,
									blank = True)
	slug		= models.SlugField(null = True, blank = True)

	def __str__(self):
		return self.nombres + ' ' + self.apellidos

	def get_absolute_url(self):
		return reverse('sitioninos:niños-detalle', kwargs={'titulo':self.slug})

	@property
	def titulo(self):
		return self.nombres + '-' + self.apellidos

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    #instance.categoria = instance.categoria.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=Nino)
