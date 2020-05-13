import model


def izpis_igre(igra):
    tekst = (
        '==================================================\n\n'
        'Število preostalih poskusov: {stevilo_preostalih_poskusov} \n\n'
        '        {pravilni_del_gesla}\n\n'
        'Neuspeli poskusi: {neuspeli_poskusi}'
    ).format(
        stevilo_preostalih_poskusov=model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1,
        pravilni_del_gesla=igra.pravilni_del_gesla(),
        neuspeli_poskusi=igra.nepravilni_ugibi()
    )
    return tekst

def izpis_zmage(igra):
    tekst = (
        '==================================================\n\n'
        'Wipiiiiiii, zmaga! Geslo je bilo: {geslo}\n\n'
        '==================================================\n\n'
    ).format(
        geslo=igra.geslo  
    )
    return tekst

def izpis_poraza(igra):
    tekst = (
        '==================================================\n\n'
        'Boooo, poraz! Geslo je bilo: {geslo}\n\n'
    ).format(
        geslo=igra.geslo  
    )
    return tekst

def izpis_napake(igra):
    return '#### Ugiba se ena črka naenkrat. ####\n'

def zahtevaj_vnos():
    return input('Črka: ')



def pozeni_vmesnik():
    igra = model.nova_igra()

    while True:
        # Najprej izpišemo stanje, da vidimo, koliko črk je 
        print(izpis_igre(igra))
        # Čakamo na črko od uporabnika
        poskus = zahtevaj_vnos()
        rezultat_ugiba = igra.ugibaj(poskus)
        if rezultat_ugiba == model.VEC_KOT_CRKA:
            print(izpis_napake(igra))
        elif rezultat_ugiba == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif rezultat_ugiba == model.PORAZ:
            print(izpis_poraza(igra))
            break
    return

#Zaženi igro:
pozeni_vmesnik()