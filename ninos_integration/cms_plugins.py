from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import NinoPluginModel, Hola
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext as _


@plugin_pool.register_plugin  # register the plugin
class NinoPluginPublisher(CMSPluginBase):
    model = NinoPluginModel  # model where plugin data are saved
    module = _("Becados")
    name = _("Agregar Becado")  # name of the plugin in the interface
    render_template = "ninos_integration/nino_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin
class HolaPlugin(CMSPluginBase):
    model = Hola
    module = _("Hola")
    name = _("Decir Hola")  # name of the plugin in the interface
    render_template = "ninos_integration/hola.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(HolaPlugin, self).render(context, instance, placeholder)
        return context
