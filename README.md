# Vmesno poročilo o upravljenem delu 
## Iowa podatki o prometnih nesrečah in o prodaji alkohola

Naša skupina poskuša iz dveh podatkovnih množic o prometnih nesrečah v zvezni državi Iowi, in eni večji podatkovni množici o prodaji alkohola v zvezni državi Iowi, najti korelacijo zvišane prodaje alkohola in večji pogostosti prometnih nesreč.

## Opažanja

Ugotovili smo da je v podatkih veliko atributov, ki jih nebomo uporabljali (razni IDji, in neznane kategorije.

### Priprava podatkov

Ker sta dve od treh podatkovnih množic bistveno pre velike (tudi za github), smo se prvo lotili podatke filtrirati, da zmanjšamo velikost, in število vnosov.


### Pomembnejši atributi

Crash1: ID,Crash date, Crash day, time string, city name, drug alcohol, weather, paved road, fatalities, injuries, property damage, x in y koordinati.__

Crash2: ID,Driver age, x in y koordinati,drug result, alcohol result,damage, crash severity, drug or alcohol related, fatalities, crash year. ; problem ker ni datum, ampak samo leto.__
Liquor: Date, Invoice number (kot id),city,sale (dollars), volume sold (litres)
