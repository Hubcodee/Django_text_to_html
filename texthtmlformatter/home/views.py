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
        with open("text.txt", "w") as f:
            f.writelines(htmlcode)

        with open("text.txt", 'r') as f:
            lines = f.read()

        with open("text.txt", 'w') as f:
            for line in lines:
                f.write(line.replace('<', '&lt;'))
            for line in lines:
                f.write(line.replace('>', '&gt;'))

        with open("text.txt", 'r') as f:
            lines = f.read()

        return(render(request, "result.html", {"htmlcode": str(htmlcode), "html": lines}))
    else:
        htmlcode = "<h2>Oops there seems some problem, Please go back and resumit your Text</h2>"
        return(HttpResponse(htmlcode))
