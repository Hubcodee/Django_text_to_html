from django.shortcuts import render, HttpResponse
from .texttohtml import formatHtml
from django.template.loader import render_to_string


def index(request):
    return(render(request, "index.html"))


def inputfile(request):
    return(render(request, "input.html"))


def result(request):
    if request.method == "POST":
        text = request.POST.get("textcode")
        # html generated code is coming from this function
        htmlcode = formatHtml("\n\n"+text+"\n\n")
        print(htmlcode)

        return(render(request, "result.html", {"htmlcode": str(htmlcode)}))
    else:
        htmlcode = "<h2>Oops there seems some problem, Please go back and resumit your Text</h2>"
        return(HttpResponse(htmlcode))
