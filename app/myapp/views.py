from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from .forms import NameForm
from transformers import pipeline


classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

# sentences = ["I am not having a great day"]

# print(model_outputs[0])
# Create your views here.

def home(request):
    # return HttpResponse("hello world")
    return render(request, "home.html")



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            yourName = form.cleaned_data['your_name']

            model_outputs = classifier(yourName)
            m = (model_outputs[0])
            for s in m: 

                if 'score' in s is not None:
                    s['label'] = s['label'].capitalize()
                    s['score'] = round(s['score'] * 100, 2) 
                    css_styles = f"background-color: green; width: {s['score']}%;"
                    print(s['label'])
                

            args = {"yourName": yourName}
            # redirect to a new URL:
            
            return render(request, "home.html" , {"yourName": yourName, "model" : m, css_styles: "css_styles", "form": form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "home.html", {"form": form})