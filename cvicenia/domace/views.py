from django.shortcuts import render, HttpResponse

def domace(request):
    kontext = {
        "meno": "Anastasiia",
    }
    return render(request, "domace/domace.html", kontext)
def du2_(request):
    kontext = {
        "meno": "Anastasiia",
        "trieda": "3.at",
        "vek": 18,
        "predmety": ["programovanie", "matematika", "3D technologie"],
    }
    return render(request, "domace/du2_.html", kontext)
    
