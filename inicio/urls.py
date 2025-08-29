from django.urls import path
from inicio.views import inicio, armar_plan, detalle_plan, editar_plan, listado_planes

urlpatterns = [
    path('', inicio, name='inicio'),
    path('planes/', listado_planes, name='listado_de_autos'),
    path('planes/armar/', armar_plan, name='armar_plan'),
    path('planes/<int:id_plan>/', detalle_plan, name='detalle_plan'),
    path('planes/<int:pk>/borrar/', AutoBorrar.as_view(), name='borrar_plan'),
    path('planes/<int:pk>/actualizar/', AutoActualizar.as_view(), name='actualizar_plan'),
]
