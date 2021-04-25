from django.shortcuts import render
import markdown2, random
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request,title):
    #html = markdown2.markdown_path("entries/"+title+".md")
    html = util.get_entry(title)
    if html == None:
        return (render(request, "encyclopedia/error.html",{
            "error": "404",
            "message": "article not found"}))
    else: 
        return render(request, "encyclopedia/title.html", {
            "content": markdown2.markdown(html),  # or use `html = markdown_path(PATH)`
            "title": title
    })

def search(request):
    query = request.POST.get('query')
    if query in util.list_entries():
        html = util.get_entry(query)
        return render(request, "encyclopedia/title.html", {
            "content": markdown2.markdown(html),  # or use `html = markdown_path(PATH)`
            "title": title})
    else: 
        entries = util.list_entries()
        results = []
        for entry in entries:
            if query.lower() in entry.lower():
                results.append(entry)
        return render(request, "encyclopedia/search.html",{
            "results": results})

def newPage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newPage.html")
    else: 
        if request.POST.get('newTitle') in util.list_entries():
            return (render(request, "encyclopedia/error.html",{
                "error": "500",
                "message": "article already exists"}))
        else:
            util.save_entry(request.POST.get('newTitle'), request.POST.get('newMD'))
            html = util.get_entry(request.POST.get('newTitle'))
            return render(request, "encyclopedia/title.html", {
                "content": markdown2.markdown(html),  # or use `html = markdown_path(PATH)`
                "title": request.POST.get('newTitle')})

def editPage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/editPage.html",{
                "content": util.get_entry(request.GET.get('title')),  # or use `html = markdown_path(PATH)`
                "title": request.GET.get('title')})
    else: 
        util.save_entry(request.POST.get('newTitle'), request.POST.get('newMD'))
        html = util.get_entry(request.POST.get('newTitle'))
        return render(request, "encyclopedia/title.html", {
            "content": markdown2.markdown(html),  # or use `html = markdown_path(PATH)`
            "title": request.POST.get('newTitle')})

def randPage(request):
    entries = util.list_entries()
    x = len(entries)
    y = random.randint(0,x-1)
    randEntry = entries[y]
    html = util.get_entry(randEntry)
    return render(request, "encyclopedia/title.html", {
        "content": markdown2.markdown(html),  # or use `html = markdown_path(PATH)`
        "title": randEntry})
