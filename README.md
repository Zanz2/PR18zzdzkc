# Vmesno poročilo o upravljenem delu 
## Iowa podatki o prometnih nesrečah in prodaji alkohola

Naša skupina poskuša iz dveh podatkovnih množic o prometnih nesrečah v zvezni državi Iowi, in eni podatkovni množici o prodaji alkohola v zvezni državi Iowi, najti korelacijo zvišane prodaje alkohola in večji pogostosti prometnih nesreč.

## Opažanja

Ugotovili smo da je v podatkih veliko atributov, ki jih nebomo uporabljali (razni IDji, in neznane kategorije).

### Priprava podatkov

Ker sta dve od treh podatkovnih množic bistveno pre velike (tudi za github), smo se prvo lotili podatke filtrirati, da zmanjšamo velikost, in število vnosov.


### Pomembnejši atributi

Iz podatkovnih množic bomo upoštevali naslednje atribute:

Crash1: ID,Crash date, Crash day, time string, drug alcohol (stopnje), weather (stopnje 0-10, 10 najhuje), paved road (0 ali 1), fatalities, injuries, property damage, x in y koordinati.
<br />

Crash2: ID,Driver age, x in y koordinati,drug result (0-100), alcohol result(0-100),drugtest (0 ali 1), alctest (0 ali 1), damage ($), crash severity (0-10), fatalities, crash year. ; problem ker ni datum, ampak samo leto.
<br />
Liquor: Date, Invoice number (kot id),city,sale (dollars), volume sold (litres) ; Iz sale, in volume sold bomo poskušali predvidevati ali gre za žgane pijače ali ne.

### Zastavljena vprašanja

Glede na to, da je možno veliko število kombinacij atributov, smo si za začetek zastavili vprašanja (vezana samo na zvezno državo Iowa), ki so mogoče malo bolj osnovna, in sicer nas zanima:
- Če obstaja korelacija z visoko prodajo alkohola, in številom prometnih nesreč v določenih mesecih.
- Koliko od vseh prometnih nesreč na mesec je povezanih z alkoholom, in koliko od teh je resnejših (velika škoda).
- V katerem področju se zgodi največ nesreč, in kje se zgodi največ nesreč povezanih z alkoholom.
- V katerem delu dneva se zgodi večina prometnih nesreč, in v katerem delu dneva se zgodi večina povezanih z alkoholom.
- V povprečju, koliko je poškodb, ali žrtev v prometnih nesrečah, in če je to število povečano v nesrečah povezanih z alkoholom.
