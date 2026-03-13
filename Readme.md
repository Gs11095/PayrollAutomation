# Calcolatore Stipendio Netto
Breve web app demo per calcolare lo stipendio netto annuale e mensile a partire dalla RAL, con dettaglio di contributi INPS, IRPEF, addizionali regionali e comunali.  
Realizzato in **Python 3 + Flask**, pronto per il deploy anche su Docker.

Provalo a questo [link](INSERIRE LINK)!

---

## Logiche payroll semplificate 
1. Il dipendente è un impiegato a tempo indeterminato
2. Il dipendente vive a Milano
3. Il dipendente non ha nessun tipo di agevolazione particolare
4. Lo stipendio mensile è calcolato su 12 mensilità
 
---

## Possibili scalabilità predisposte
1. Regioni aggiuntive
2. Comuni aggiuntivi
3. Calcolo su 13 o 14 mensilità

---

## Funzionalità 
Inserisci la RAL e clicca su "calcola" per ottenere:
  - Contributi INPS a carico del lavoratore
  - Reddito imponibile
  - IRPEF
  - Addizionale regionale (solo Lombardia)
  - Addizionale comunale (solo Milano)
  - Stipendio netto annuale e mensile

![Schermata d'esempio](images/screenshot.png)

---

## Tecnologie
- Python 3.11
- Flask 3.1.3
- Docker 
- HTML/CSS

---

