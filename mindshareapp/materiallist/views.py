from django.shortcuts import redirect,render
from materiallist.models import Material
from materiallist.forms import MaterialForm


def home_view(request):
    context ={}
    context['form']= MaterialForm()
    return render(request, "home.html", context)


# Create your views here.
