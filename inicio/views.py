from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Plan
from inicio.forms import FormularioCrearPlan, FormularioBuscarPlan
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    
    return render(request, 'inicio.html')
    
 
@login_required
def armar_plan(request):
    
    
    print(request.POST)
    
    if request.method == "POST":
        formulario = FormularioCrearPlan(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data

            plan = Plan(nombre=info.get('nombre'), dias=info.get('dias'), fotos_inicial=info.get('fotos_inicial'))
            plan.save()
        
            return redirect('listado_planes')
    else:
        formulario = FormularioCrearPlan()
        
    return render(request, 'armar_plan.html', {'formulario': formulario})

def listado_planes(request):

    formulario = FormularioBuscarPlan(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
        dias_a_buscar = formulario.cleaned_data['dias']
        planes_buscados = Plan.objects.filter(nombre__icontains=nombre_a_buscar, dias_a_buscar__icontains=dias_a_buscar)
    # else:
    #     autos_buscados = Auto.objects.all()
    
    return render(request, 'listado_planes.html', {'planes_buscados': planes_buscados, 'formulario': formulario})


def detalle_plan(request, id_plan):
    plan = Plan.objects.get(id=id_plan)
    return render(request, 'detalle_plan.html', {'plan': plan})


class PlanBorrar(LoginRequiredMixin, DeleteView):
    model = Plan
    template_name = "borrar_plan.html"
    success_url = reverse_lazy('listado_planes')


class PlanActualizar(LoginRequiredMixin, UpdateView):
    model = Plan
    template_name = "editar_plan.html"
    success_url = reverse_lazy('listado_planes')
    fields = '__all__'
    