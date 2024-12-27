from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
# Create your views here.

all_suggestions = []

class NewTaskForm(forms.Form):
    suggestion = forms.CharField(label = "suggestion")

def index(request):
    global all_suggestions
    
    if "suggestions" not in request.session:
        request.session["suggestions"] = []
    
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        
        if form.is_valid():
            suggestion = form.cleaned_data["suggestion"]
            request.session["suggestions"] += [suggestion]
            all_suggestions += [suggestion]
            
            return render(request, "suggestions/index.html", 
                          {"form": NewTaskForm()}
            )
        
        else:
            return render(request, "suggestions/index.html", {
                "form": form
            })
    else:
        return render(request, "suggestions/index.html", {
            "form": NewTaskForm()
        })
