from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util
from django.contrib import messages

import markdown2
from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'}), label = "")

class NewEntryForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Give a title to the entry...'}), label = "")
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder' : 'Enter the Markdown content...'}) , label = "")

def index(request):
    entries = util.list_entries()
    entries = [entry.lower() for entry in entries]

    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():             #Server-side Validation
            q = form.cleaned_data["q"]
            q = request.POST["q"]
            if q.lower() in entries:  
                return HttpResponseRedirect(reverse("entry" , args = [q]))
            else:
                result = []
                for name in util.list_entries():
                    if q.lower() in name.lower():
                        result.append(name)
                return render(request, "encyclopedia/search_results.html" , {
                    "form" : form, 
                    "result" : result,
                    "title" : q              
                })
    return render(request, "encyclopedia/index.html" )

def entry(request, title):
    content = util.get_entry(title)
    if content == None:
        return render(request, "encyclopedia/error.html" , {
            "title" : title.capitalize()
        })
    return render(request, "encyclopedia/entry.html", {
        "title" : title.capitalize(),
        "content" : markdown2.markdown(content)
    })

def newpage(request):
    entries = util.list_entries()
    entries = [entry.lower() for entry in entries]

    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            if title.lower() in entries:
                messages.error(request , "An article with this title already exists!")
                return render(request , "encyclopedia/newpage.html" , {
                    "newform" : form
                })
            else:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("entry" , args = [title]))


    return render(request , "encyclopedia/newpage.html" , {
        "newform" : NewEntryForm()
    })

def edit(request, title):
    if request.method == "POST":
        content = request.POST["content"]
        util.save_entry(title , content)
        return HttpResponseRedirect(reverse("entry", args = [title]))

    return render(request, "encyclopedia/edit.html" , {
        "title" : title.capitalize(),
        "content" : util.get_entry(title)
    })

