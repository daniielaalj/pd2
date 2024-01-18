def ieraksti_vardu():
    try:
        with open('lietotajs', 'w') as faila_atslega
             faila_atslega.write(vards)
        print("Vārds veiksmīgi ierakstīts failā.")
    except:
        print("Kļūda ierakstot failā.")
vards = input("Ievadiet savu vārdu: ")
ieraksti_vardu(vards)