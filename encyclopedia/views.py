import markdown
from django.shortcuts import render
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(requests, title):
    text = util.get_entry(title)
    if text is not None:
        md = markdown.Markdown()
        result = md.convert(text)
        return render(requests, "encyclopedia/page.html", {
            "content": result,
            "title": title
        })
    else:
        return render(requests, "encyclopedia/page.html", {
            "content": "<h2> Статья не найдена 1 </h2>"
        })


