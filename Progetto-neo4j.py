from PercosiMontanari import PercosiMontanari

percorsi_montanari = PercosiMontanari()
# percorsi_montanari.empty_database()
# percorsi_montanari.demo()
# percorsi = percorsi_montanari.percorso(durata_max=300, durata_min=200)
# difficolta = 'facile'
# numero_p = 10
# notte_fuori = 'y'

while True:
    print("""
    Cosa vuoi fare?

        # 1. Calcolare Percorso
        # 2. Terminare sessione
        """)

    while True:
        try:
            scelta_1 = int(input("Inserisci il numero della tua scelta: "))
        except:
            print('\nDevi inserire un numero intero')
        else:
            if scelta_1 > 0 and scelta_1 <= 2:
                break
            else:
                print('\nHai sbagliato ad inserire il numero, riprova')

    if scelta_1 == 1:
        percorsi_montanari.empty_database()
        percorsi_montanari.demo()
        while True:
            try:
                durata_massima = int(input("\nInserisci la durata massima in minuti del percorso: "))
                durata_minima = int(input("\nInserisci la durata massima in minuti del percorso: "))
            except:
                print('\nDevi inserire un numero intero')
            else:
                if durata_massima>0 and  durata_minima>0:
                    break
                else:
                    print('\nGli interi devono essere maggiori di 0')
        while True:
            notte_fuori=input('\nVuoi dormire in un rifugio? (y,n) ')
            if notte_fuori=='y' or notte_fuori=='n':
                break
            else:
                print('\nDevi inserire y se vuoi dormire in un rifugio o n se non vuoi dormire in un rifugio')

        if notte_fuori=='y':
            while True:
                try:
                    numero_p = int(input("\nIn quanti siete? "))
                except:
                    print('\nDevi inserire un numero intero')
                else:
                    if numero_p>0:
                        break
                    else:
                        print('\nIl numero di persone deve essere maggiore di 0')

        while True:
            difficolta=input("\nQuanto difficile vuoi il percorso?(facile, medio, difficile) ")
            if difficolta in ['facile', 'medio', 'difficile']:
                break
            else:
                print('\nLa difficolta deve essere facile, medio o difficile')

        percorsi=percorsi_montanari.percorso(durata_max=durata_massima,durata_min=durata_minima)
        percorsi_montanari.close()
        percorsi_proposti = []
        controllo=True
        for e in percorsi:
            if difficolta == 'facile' and 'medio' not in e['difficolta'].split('/')[1:] and 'difficile' not in e['difficolta'].split('/')[1:]:
                if notte_fuori == 'y':
                    posti = e['capacita'].split('/')[1:]
                    
                    for num in posti:
                        if numero_p <= int(num):
                            controllo=False
                            e['i_rifugio'] = posti.index(num)
                            percorsi_proposti.append(e)
                            break
                        
                else:
                    percorsi_proposti.append(e)

            elif difficolta == 'medio' and 'difficile' not in e['difficolta'].split('/')[1:]:
                if notte_fuori == 'y':
                    posti = e['capacita'].split('/')[1:]
                    
                    for num in posti:
                        if numero_p <= int(num):
                            controllo=False
                            e['i_rifugio'] = posti.index(num)
                            percorsi_proposti.append(e)
                            break
                        
                else:
                    percorsi_proposti.append(e)

            else:
                if notte_fuori == 'y':
                    posti = e['capacita'].split('/')[1:]
                    
                    for num in posti:
                        if numero_p <= int(num):
                            controllo=False
                            e['i_rifugio'] = posti.index(num)
                            percorsi_proposti.append(e)
                            break
                        
                else:
                    percorsi_proposti.append(e)
                    
        if controllo:
            print('\nNon ci sono rifuggi con abbastanza posti letto')

        for i in range(len(percorsi_proposti)):
            tempo = percorsi_proposti[i]['tempototale']
            tempo_str = f"Il percorso {i+1} dura {tempo} minuti"
            sentieri = percorsi_proposti[i]['descrizione'].split('/')[1:]
            punti = percorsi_proposti[i]['punti'].split('/')[1:]
            if notte_fuori == 'y':
                id_rifugio = percorsi_proposti[i]['i_rifugio']
                rifugio_notte = punti[id_rifugio]
                rifugio_notte_str = f"Potrai dormire nel {rifugio_notte}"
            inizio_str = f"{punti[0]}"
            intermezzo_str = ""
            for i in range(len(sentieri)):
                intermezzo_str += f" --> sentiero {sentieri[i]} --> {punti[i+1]} "
            if notte_fuori == 'y':
                print(
                    f"\n{tempo_str}\nPercorso:\n{inizio_str + intermezzo_str}\n{rifugio_notte_str}")
            else:
                print(f"\n{tempo_str}\nPercorso:\n{inizio_str + intermezzo_str}")
                
        while True:
            continuare=input('\nVuoi continuare? (y,n) ')
            if continuare=='y' or continuare=='n':
                break
            else:
                print('\nDevi inserire y se vuoi continuare o n se non vuoi continuare')
        if continuare=='n':
            break
    else:
        break
