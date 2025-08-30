from django.urls import path
from inicio.views import inicio, armar_plan, detalle_plan, listado_planes, PlanBorrar, PlanActualizar

urlpatterns = [
    path('', inicio, name='inicio'),
    path('planes/', listado_planes, name='listado_planes'),
    path('planes/armar/', armar_plan, name='armar_plan'),
    path('planes/<int:id_plan>/', detalle_plan, name='detalle_plan'),
    path('planes/<int:pk>/borrar/', PlanBorrar.as_view(), name='borrar_plan'),
    path('planes/<int:pk>/actualizar/', PlanActualizar.as_view(), name='actualizar_plan'),
]
