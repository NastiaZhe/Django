from django.shortcuts import render, HttpResponse

def domace(request):
    kontext = {
        "meno": "Anastasiia",
    }
    return render(request, "domace/domace.html", kontext)
    
