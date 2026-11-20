from django.shortcuts import render

def cv1_index(request):
    kontext = {
        "meno": "Anastasiia",
    }
    return render(request, "cv1/cv1_index.html", kontext)

def cv1_obchod(request):
    kontext = [
        {"nazov": "kura", "cena": 7.50},
        {"nazov": "cukor", "cena": 2.99},
        {"nazov": "voda", "cena": 0.99},
        {"nazov": "panvica", "cena": 15.90},
    ]
    max_cena = request.GET.get("max_cena", "").strip()
    chyba = None
    if max_cena != "":
        try:
            limit = float(max_cena.replace(",", "."))
            produkty = [p for p in produkty if p["cena"] <= limit]
        except ValueError:
            chyba = "Zadaj ine cislo."
    return render(request, "cv1_obchod.html", {
        "produkty": produkty,
        "max_cena": max_cena,
        "chyba": chyba,
    })

def cv1_body(request):
    vysledok = None
    chyba = None
    if request.method == "POST":
        try:
            body = float(request.POST.get("body", "").strip().replace(",", "."))
            max = float(request.POST.get("max", "").strip().replace(",", "."))
            if max <= 0 or body < 0 or body > max:
                raise ValueError
            percento = body / max * 100
            if percento >= 90:
                znamka = 1
            elif percento >= 75:
                znamka = 2
            elif percento >= 50:
                znamka = 3
            elif percento >= 30:
                znamka = 4
            else:
                znamka = 5
            perc_text = f"{percento:.1f}".replace(".", ",")
            vysledok = f"{body:g} z {max:g} bodov = {perc_text} % → známka {znamka}"
        except ValueError:
            chyba = "Zadaj ine cislo"

    return render(request, "cv1_body.html", {
        "vysledok": vysledok,
        "chyba": chyba,
        })