import csv
def lasit_cs_failu():
    try:
        with open('r') as faila_atslega:
            lasitajs = csv.reader(faila_atslega)
            for rinda in lasitajs:
                if len(rinda) > 1:
                    otrā_kolonna = rinda[1]
                    print(otrā_kolonna)
    except FileNotFoundError:
        print(f"CSV fails ar nosaukumu '' nav atrasts.")
    except:
        print("Kļūda nolasot CSV failu.")