def lasit_teksta_failu():
    try:
     with open('r') as faila_atslega:
        rindas = faila_atslega.readlines()
        if len(rindas) >= 3:
            tresa_rinda = rindas[2].strip()
            print(tresa_rinda)
        else:
            print("Failā ir mazāk par trīs rindiņām.")
    except FileNotFoundError:
       print(f"Teksta fails ar nosaukumu '' nav atrasts.")
    except:
       print("Kļūda nolasot teksta failu.")
teksta_faila_nosaukums = input("Ievadiet teksta faila nosaukumu: ")
lasit_teksta_failu(teksta_faila_nosaukums)