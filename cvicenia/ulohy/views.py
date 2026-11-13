from django.shortcuts import render, HttpResponse

def ahoj(request):
    return HttpResponse("Ahoj svet!")

def o_mne(request):
    kontext = {
        "meno": "Anastasiia",
        "vek": 18,
        "zaluby": ["fitko", "auta", "hudba"],
    }
    return render(request, "ulohy/o_mne.html", kontext)

def rozvrh(request):
    hodiny = [
        {"cislo": 1, "predmet": "Programovenie"},
        {"cislo": 2, "predmet": "Programovenie"},
        {"cislo": 3, "predmet": "Programovenie"},
        {"cislo": 4, "predmet": "Anglicky jazyk"},
        {"cislo": 5, "predmet": "IOT"},
        {"cislo": 6, "predmet": "IOT"}
    ]
    return render(request, "ulohy/rozvrh.html", {"den": "Piatok", "hodiny": hodiny})

def pozdrav(request):
    meno = request.GET.get("meno", "") # .get najde a vrati hodnotu prvku s indexom(klucom) meno, ak ho nenajde vlozi prazdny string
    return render(request, "ulohy/pozdrav.html", {"meno": meno})