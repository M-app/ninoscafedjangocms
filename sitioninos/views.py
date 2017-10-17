from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Nino
from .forms import NinoCreateForm
# Create your views here.

class NinosListView(ListView):
	def get_queryset(self):
		slug = self.kwargs.get('slug')
		if slug:
			queryset = Nino.objects.filter(
				Q(etapa__iexact = slug) |
				Q(etapa__icontains = slug)
				)
		else:
			queryset = Nino.objects.all()
		return queryset

class NinosDetailView(DetailView):
	#queryset = Nino.objects.all()
	def get_object(self, *args, **kwargs):
		titulo = self.kwargs.get('titulo')
		obj = get_object_or_404(Nino, slug = titulo)
		return obj

class NinoCreateView(CreateView):
	form_class = NinoCreateForm
	template_name = 'sitioninos/nino_create_form.html'
	success_url = '/niños/'

def nino_create(request):
	form = NinoCreateForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		#instance = form.save(commit = False)
		form.save()
		return HttpResponseRedirect('/niños/')
	context = {
		'form' : form,
	}
	return render(request,'sitioninos/nino_create_form.html',context)
# class RestauranteDetailView(DetailView):
# 	queryset = Restaurante.objects.all()

# 	# def get_object(self, *args, **kwargs):
# 	# 	rest_id = self.kwargs.get('rest_id')
# 	# 	obj = get_object_or_404(Restaurante, id = rest_id)
# 	# 	return obj