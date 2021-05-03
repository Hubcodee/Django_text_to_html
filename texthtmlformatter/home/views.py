from django.shortcuts import render, HttpResponse
from bs4 import BeautifulSoup
import re


def index(request):
    return(render(request, "index.html"))


def inputfile(request):
    return(render(request, "input.html"))


def result(request):
    if request.method == "POST":
        text = request.POST.get("textcode")
        # print("TEXT\n"+text)


        orig_prettify = BeautifulSoup.prettify
        r = re.compile(r'^(\s*)', re.MULTILINE)

        # this line creates our customised prettify function from  the provided prettify from beautiful soup
        def prettify(self, encoding=None, formatter="minimal", indent_width=4):
            return r.sub(r'\1' * indent_width, orig_prettify(self, encoding, formatter))

        BeautifulSoup.prettify = prettify
        htmlcode=BeautifulSoup(text, 'html.parser')

        # this way we are adding our own parameter to prettify function
        htmlcode=htmlcode.prettify(indent_width=3)
        # print("PREETYPRINT\n"+htmlcode)
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
