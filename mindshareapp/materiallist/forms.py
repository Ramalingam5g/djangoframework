from django import forms  
from materiallist.models import Material  
class MaterialForm(forms.ModelForm):  
    class Meta:  
        model = Material  
        fields = "__all__"  