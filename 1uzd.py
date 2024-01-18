def lasit_teksta_failu(txt):
    try:
        with open(txt, 'r') as faila_atslega:
            saturs = faila_atslega.read()
            print(saturs)
    except FileNotFoundError:
        print(f"Teksta fails ar nosaukumu '{txt}'nav atrasts.")
    except:
        print("Kļūda nolasot teksta failu.")