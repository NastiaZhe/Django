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
def du3_teplota(request):
    ans = None
    if request.method == 'POST':
        tep = float(request.POST["tep"])
        smer = request.POST["smer"]

        if smer == 'c>f':
            ans = str(round(tep * 9 / 5 + 32, 1)) + " °F"
        elif smer == 'f>c':
            ans = str(round((tep - 32) * 5 / 9, 1)) + " °C"

    return render(request, 'domace/du3_teplota.html', {'ans': ans})
    
