# Analisi giornaliera dei dati ambientali — Oliveto pugliese, agosto
# Letture orarie di temperatura, umidità aria, luce PAR e umidità suolo
# Soglie calibrate per olivo (Olea europaea) in clima mediterraneo
letture_giornata = [
    "06:00, 22.5, 78, 80, 38",
    "09:00, 28.0, 65, 850, 35",
    "12:00, 35.2, 42, 1850, 28",
    "14:00, 39.5, 28, 2050, 22",
    "16:00, 37.0, 35, 1600, 25",
    "19:00, 30.5, 55, 450, 32",
    "22:00, 24.0, 82, 0, 45"]

def presa_lettura(lettura):
    risultato = lettura.split(",")
    ora = risultato[0]
    temperatura = float(risultato[1])
    umidità_aria = int(risultato[2])
    luce = int(risultato[3])
    umidità_suolo = int(risultato[4])
    return ora, temperatura, umidità_aria, luce, umidità_suolo

def classificazione_temperatura(temp):
    if temp > 38:
        return "stress severo"
    elif temp > 32:
        return "stress caldo"
    elif temp < 10:
        return "freddo"
    else:
        return "confort"

def classificazione_umidità_aria(um_ar):
    if um_ar < 30:
        return "stress secco"
    elif um_ar > 80:
        return "rischio fungino"
    else:
        return "ottimale"

def classificazione_luce(lc):
    if lc < 100:
        return "buio"
    elif lc < 400:
        return "luce bassa"
    elif lc < 1000:
        return "luce media"
    elif lc < 1800:
        return "pieno sole"
    else:
        return "irraggiamento estremo"

def classificazione_umidità_suolo(um_suolo):
    if um_suolo < 20:
        return "stress idrico"
    elif um_suolo < 30:
        return "secco"
    elif um_suolo > 60:
        return "saturo"
    else:
        return "ottimale"

for lettura in letture_giornata:
    ora, temperatura, umidità_aria, luce, umidità_suolo = presa_lettura(lettura)
    print(f"orario: {ora}")
    print(f"  🌡  {temperatura}°C → {classificazione_temperatura(temperatura)}")
    print(f"  💧  {umidità_aria}% → {classificazione_umidità_aria(umidità_aria)}")
    print(f"  🌿  {luce} → {classificazione_luce(luce)}")
    print(f"  🌱  {umidità_suolo}% → {classificazione_umidità_suolo(umidità_suolo)}")