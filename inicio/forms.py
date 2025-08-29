from django import forms


class FormularioBasePlan(forms.Form):
    nombre = forms.CharField(max_length=20)
    
class FormularioCrearPlan(FormularioBasePlan):
    precio = forms.DecimalField(max_digits=6, decimal_places=2)
    clases_incluidas = forms.CharField(max_length=40)
    

class FormularioBuscarPlan(FormularioBasePlan): 
    nombre = forms.CharField(max_length=20, required=False)
    precio = forms.DecimalField(max_digits=6, decimal_places=2, required=False)