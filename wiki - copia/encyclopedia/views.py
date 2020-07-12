from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from . import util, markdown2
from random import randint
import re

class AddPageForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title', 'autocomplete': 'off'}))
    textarea = forms.CharField(widget=forms.Textarea({'style':'height:65vh;width:85%;margin-top:7px;'}))

class EditPageForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))
    textarea = forms.CharField(widget=forms.Textarea({'style':'height:65vh;width:85%;margin-top:7px'}))

def index(request):
    #check for GET params
    page = request.GET.get('q', None)
    if page is not None:
        # if there is a page that matches the GET params, redirect to it
        if util.get_entry(page) is not None:
            return HttpResponseRedirect(reverse('wiki:pages', kwargs={'page': f'{page.capitalize()}'}))
        # else, show search results with the GET query as a substring
        r = re.compile(f".*{page}.*", re.IGNORECASE)
        search_results = list(filter(r.match, util.list_entries()))
        results_flag = True
        if len(search_results) == 0:
            results_flag = False
        return render(request, "encyclopedia/search_results.html", {
            "search_results": search_results,
            "results": results_flag,
            "query": page
        })

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def pages(request, page):
    #check for GET params
    get_page = request.GET.get('q', None)
    if get_page is not None:
        entry = util.get_entry(get_page)
        if entry is not None:
            entry = markdown2.markdown(util.get_entry(get_page))
            return render(request, "encyclopedia/pages.html", {
                "page": get_page.capitalize(),
                "entry": entry
            })
        r = re.compile(f".*{get_page}.*", re.IGNORECASE)
        search_results = list(filter(r.match, util.list_entries()))
        results = True
        if len(search_results) == 0:
            results = False
        return render(request, "encyclopedia/search_results.html", {
            "search_results": search_results,
            "results": results,
            "query": get_page
        })

    entry = util.get_entry(page)
    if entry is not None:
        # convert the markdown content into html
        entry = markdown2.markdown(entry)
    return render(request, "encyclopedia/pages.html", {
        "page": page,
        "entry": entry
    })

def add_page(request):
    #check for GET params
    get_page = request.GET.get('q', None)
    if get_page is not None:
         # if there is a page that matches the GET params, redirect to it
        if util.get_entry(get_page) is not None:
            return HttpResponseRedirect(reverse('wiki:pages', kwargs={'page': f'{get_page.capitalize()}'}))
        # else, show search results with the GET query as a substring
        r = re.compile(f".*{get_page}.*", re.IGNORECASE)
        search_results = list(filter(r.match, util.list_entries()))
        results = True
        if len(search_results) == 0:
            results = False
        return render(request, "encyclopedia/search_results.html", {
            "search_results": search_results,
            "results": results,
            "query": get_page
        })

    if request.method == "POST":
        form = AddPageForm(request.POST)
        if form.is_valid():
            #lower every title to check without caring about case
            title = form.cleaned_data["title"]
            text = form.cleaned_data["textarea"]
            if title.lower() not in [x.lower() for x in util.list_entries()]:
                util.save_entry(title, text)
                return HttpResponseRedirect(reverse('wiki:pages', kwargs={'page': f'{title}'}))
            else:
                return render(request, "encyclopedia/page_exists.html",{
                    "title": title
                })
        else:
            return render(request, "encyclopedia/add_page.html",{
                "form": form
            })

    return render(request, "encyclopedia/add_page.html",{
        "form": AddPageForm()
    })

def edit_page(request, page):
    #check for GET params
    get_page = request.GET.get('q', None)
    if get_page is not None:
         # if there is a page that matches the GET params, redirect to it
        if util.get_entry(get_page) is not None:
            return HttpResponseRedirect(reverse('wiki:pages', kwargs={'page': f'{get_page.capitalize()}'}))
        # else, show search results with the GET query as a substring
        r = re.compile(f".*{get_page}.*", re.IGNORECASE)
        search_results = list(filter(r.match, util.list_entries()))
        results = True
        if len(search_results) == 0:
            results = False
        return render(request, "encyclopedia/search_results.html", {
            "search_results": search_results,
            "results": results,
            "query": get_page
        })

    if request.method == "POST":
        form = EditPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            text = form.cleaned_data["textarea"]
            util.save_entry(title, text)
            return HttpResponseRedirect(reverse('wiki:pages', kwargs={'page': f'{title}'}))
        else:
            return render(request, "encyclopedia/edit_page.html",{
                "form": form
            })
    
    # populate a form with the actual data of the page and give it the user to modify
    data = {'title': page, 'textarea': util.get_entry(page)}
    form = EditPageForm(initial=data)
    return render(request, "encyclopedia/edit_page.html",{
        "page": page,
        "form": form
    })

# gets a random page by accesing the list of pages at a random index  
def random_page(request):
    entries = util.list_entries()
    page = entries[randint(0, len(entries) - 1)]
    return HttpResponseRedirect(reverse('wiki:pages', kwargs={'page': page}))