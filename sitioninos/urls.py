from django.conf.urls import url


from sitioninos.views import (
    NinosListView,
    NinosDetailView,
    NinoCreateView,
    nino_create,
)

urlpatterns = [
    url(r'^$', NinosListView.as_view(), name="niños-lista"),
    url(r'^nuevo/$', nino_create ,name="niños-nuevo"),
    #url(r'^niños/(?P<slug>\w+)$', NinosListView.as_view()),
    #url(r'^niños/(?P<etapa>\w+)$', NinosListView.as_view()),
    url(r'^(?P<titulo>[\w-]+)/$', NinosDetailView.as_view(),name="niños-detalle"),
    #url(r'^niños/(?P<pk>\w+)$', )
]
