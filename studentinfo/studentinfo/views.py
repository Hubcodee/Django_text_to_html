from django.http import HttpResponse

prn=1841048
name="Shivanshu"
clas="T.Y Computer Engineering"
def index(request):
    return HttpResponse("<h2>Hello I am  {} My PRN is {} and I am in {} ;This is my first WebApp.</h2>.".format(name,prn,clas))
