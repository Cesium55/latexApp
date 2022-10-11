from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import *
from .forms import AddFormulaForm

# Create your views here.

def main(request):
    return render(request, "mainApp/main.html")

def defaulConspect(request):
    data = {}
    data["cats"] = Category.objects.all()
    data["conspects"] = FormulaConspect.objects.all()
    data["test_latex_formula"] = Formula.objects.get(pk=3)
    # for i in data["cats"]:
    #     data[i] = {"name":data[i].name, "children" = FormulaConspect}


    return render(request, "mainApp/defaultConspect.html", data)


def conspectById(request, id):

    try:
        conspect = FormulaConspect.objects.get(pk=id)
    except:
        return HttpResponse("404")
    formulas = Formula.objects.filter(parent = conspect)
    print(formulas)

    data = {}
    data["conspect"] = conspect
    data["formulas"] = formulas
    data["form"] = AddFormulaForm()


    if request.method=="POST":
        form = request.POST
        if(all(i in form for i in ["name", "body", "csrfmiddlewaretoken"])):
            print(form)
            new_formula = Formula(name=form["name"], body=form["body"], isLatex="isLatex" in form, parent=FormulaConspect.objects.get(pk=id))
            new_formula.save()
        else:
            data["error"] = "chego-to ne hvataet"
        return HttpResponseRedirect(request.path)
    else:
        return render(request, "mainApp/conspect.html", data)


def dynamicFormula(request):
    return render(request, "mainApp/dynamic.html")
