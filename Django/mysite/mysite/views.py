from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.date.today()
    html = "<html><body>This is the home page. Today is %s.</body></html>" % now
    return HttpResponse(html)

def kulwant(request):
    html = "<html><body>This is Kulwant Rai's page.</body></html>"
    return HttpResponse(html)

