# SYMPHONYA · Data Validator
# Validazione qualità dei dati dei sensori + rilevamento anomalie + statistiche giornaliere.
# Secondo strato della pipeline SYMPHONYA, dopo sensor_classifier.py
letture_test = [
    "08:00, 22.5, 78, 80, 38",
    "10:00, 28.0, 65, 850, 35",
    "12:00, 35.2, 42, 1850, 28",
    "14:00, 99.9, 28, 2050, 22",
    "16:00, 37.0, 35, 1600, 0",
    "19:00, 30.5, 200, 450, 32",
    "20:00, 24.0, 82",
    "22:00, 24.0, 82, 0, 45",
]

def verifica_lettura(lettura):
    """
    Verifica che una lettura grezza rispetti i range tecnici dei sensori.
    Ritorna 'OK' se valida, altrimenti il motivo dell'errore.
    """
    singole_letture = lettura.split(",")
    if len(singole_letture) != 5:
        return "dati mancanti"
    if float(singole_letture[1]) > 50 or float(singole_letture[1]) < -10:
        return "temperatura fuori range"
    if int(singole_letture[2]) <0 or int(singole_letture[2]) > 100:
        return "umidità aria fuori range"
    if int(singole_letture[3]) < 0 or int(singole_letture[3]) >3000:
        return "luce fuori range"
    if int(singole_letture[4]) < 0 or int(singole_letture[4]) > 100:
        return "umidità suolo fuori range"
    return "OK"

def rileva_anomalia(singole):
    lettura = singole.split(",")
    ora_numero = int(lettura[0][:2])
    if float(lettura[1]) > 50:
        return "anomalia: temperatura estrema"
    if int(lettura[4]) == 0 and int(lettura[2]) > 25:
        return "anomalia: sensore suolo probabilmente scollegato"
    if int(lettura[3]) == 0 and ora_numero >= 8 and ora_numero <= 20:
        return "anomalia: PAR zero in pieno giorno"
    return "nessuna anomalia"

def processa_letture(lista):
    for letture in lista:
        variabile = verifica_lettura(letture)
        if variabile == "OK":
            anomalia = rileva_anomalia(letture)
            print(f'{letture} → {anomalia}')
        else:
            print(f"{letture} → dati corrotti {variabile}")

def statistica_giornata(lista_letture):
    totale = len(lista_letture)
    valide = 0
    anomale = 0
    invalide = 0
    for dati_grezzi in lista_letture:
        
        if verifica_lettura(dati_grezzi) == "OK":
            valide += 1
        
            if rileva_anomalia(dati_grezzi) != "nessuna anomalia":
                anomale += 1
        else:
            invalide += 1
    percentuale_valide = (valide*100)//totale
    print(f"\nStatistiche giornata:")
    print(f"  Totale letture: {totale}")
    print(f"  Valide: {valide}")
    print(f"  Con anomalia: {anomale}")
    print(f"  Invalide: {invalide}")
    print(f"  Utilizzabili: {percentuale_valide}%")

processa_letture(letture_test)
statistica_giornata(letture_test)

