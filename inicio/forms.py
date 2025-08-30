from django import forms


class FormularioBasePlan(forms.Form):
    nombre = forms.CharField(max_length=20)
    
class FormularioCrearPlan(FormularioBasePlan):
    nombre = forms.CharField(max_length=20)
    dias = forms.CharField(max_length=100)
    musculos_a_entrenar = forms.CharField(max_length=200)
    fotos_inicial = forms.ImageField(required=False)
    

class FormularioBuscarPlan(FormularioBasePlan): 
    nombre = forms.CharField(max_length=20, required=False)
    musculos_a_entrenar = forms.CharField(max_length=200)