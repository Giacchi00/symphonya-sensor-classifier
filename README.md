# symphonya-sensor-classifier
Primo strato della pipeline SYMPHONYA: parsing e classificazione agronomica di dati ambientali simulati. 
# SYMPHONYA · Sensor Classifier

> Primo strato della pipeline **SYMPHONYA**, installazione artistica che converte dati ambientali da sensori in musica generativa.

Questo modulo gestisce il **parsing** e la **classificazione agronomica** delle letture dei sensori. Le soglie sono calibrate per **olivicoltura in clima mediterraneo** (Puglia, sud Italia).

---

## Cosa fa

- Legge stringhe simulate dei sensori (temperatura, umidità aria, luce PAR, umidità suolo)
- Esegue il parsing in valori tipizzati (`float`, `int`)
- Classifica ogni parametro secondo soglie agronomiche
- Produce un report giornaliero leggibile

## Parametri monitorati

| Parametro | Sensore previsto | Classificazioni |
|---|---|---|
| Temperatura | DHT22 | freddo · confort · stress caldo · stress severo |
| Umidità aria | DHT22 | stress secco · ottimale · rischio fungino |
| Luce PAR | BH1750 | buio · luce bassa · luce media · pieno sole · estremo |
| Umidità suolo | Sensore capacitivo | stress idrico · secco · ottimale · saturo |

## Come usarlo

```bash
python sensor_classifier.py
```

Output di esempio (giornata di agosto in oliveto pugliese):
orario: 14:00
🌡  39.5°C → stress severo
💧  28%   → stress secco
🌿  2050  → irraggiamento estremo
🌱  22%   → stress idrico

## Prossimi step

- [ ] Lettura da file CSV invece che da lista hardcoded
- [ ] Integrazione con dati reali da ESP32 + sensori fisici (DHT22, BH1750, soil moisture)
- [ ] Persistenza in database SQLite
- [ ] Pipeline verso sintesi audio generativa
- [ ] Aggiunta dati satellitari (NDVI/NDMI da Sentinel-2)

## Contesto

SYMPHONYA è un progetto a lungo termine che mira a tradurre lo stato fisiologico delle piante in musica generativa in tempo reale, attraverso sensori IoT e AI. Questo repository documenta il **primo strato** della pipeline.

Le soglie agronomiche sono basate su:
- Letteratura su stress termico/idrico dell'olivo in clima mediterraneo
- Range di funzionamento dei sensori previsti
- Esperienza agronomica diretta sul campo

## Autore

**Giacomo** — Agronomo (laurea in Scienze Agrarie) con percorso in formazione come AI Engineer specializzato in AgriTech.
Lecce, Puglia.

## Licenza

MIT — vedi il file [LICENSE](LICENSE) per i dettagli.
