from django.shortcuts import render,HttpResponse
from .texttohtml import formatHtml

def index(request):
    return(render(request,"index.html"))

def inputfile(request):
    return(render(request,"input.html"))

def result(request):
    if request.method=="POST":
        text=request.POST.get("textcode")
        htmlcode=formatHtml("\n\n"+text+"\n\n")   # html generated code is coming from this function
        print(htmlcode)
        return(render(request,"result.html",{"htmlcode":str(htmlcode)}))
    else:
        htmlcode="<h2>Oops there seems some problem, Please go back and resumit your Text</h2>"
        return(HttpResponse(htmlcode))