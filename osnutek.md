Člana skupine sva Žan Žagar in David Zagoršek.
Problem, ki se ga boma lotila je stopnja korelacije med prodajo
alkoholnih pijač v zvezni državi Iowa, in številom prometnih nesreč v zvezni dražvi Iowa.
Glavni nabor podatkov za prodajo pijač v zvezni državi Iowa je:
https://www.kaggle.com/residentmario/iowa-liquor-sales
Podatki so v obliki .csv in sicer
|item number|date|store number|store name|adress|city|zip_code|store_location
|county_number|county|category|category_name|vendor_number|vendor_name|
item_num|item_description|pack|bottle_volume|state_bottle_cost|state_bottle_retail|
bottles_sold|sale|volume_sold_liters|volume_sold_gallons

Tukaj je kar precej podatkov, večina neuporabnih. V glavnem nameravava uporabljati podatke o lokaciji, času, količini, in ceni alkohola.

Glavni nabori podatkov za prometne nesreče v Iowa je:
https://catalog.data.gov/dataset/crash-data
Čeprav piše da je .csv povezava ne delujoča, to ni res, kajti na računalnik,
sem lahko preprosto spravil ta file.
http://data.iowadot.gov/datasets/crash-data-1?geometry=-112.267%2C38.981%2C-92.404%2C44.704
http://data.iowadot.gov/datasets/crash-vehicle-unit-data?geometry=-112.267%2C38.981%2C-92.404%2C44.704

Na veliko srečo so vsi ti dataseti podani v .csv obliki, se pa razlikujejo po atributih, podobno je kot zgoraj, le da so tukaj tudi diskretni, recimo nekatere podatkovne strukture imajo gender_male in je potem 1 če je moški in 0 če ni moški, ter crash severity high, 1 če je bila velika nesreča itd.

Trenutno se še odločama katero od teh treh množic uporabiti, ker imajo različne atribute.

Cilj celotne naloge pa bo najti neke zanimivosti med visoko prodajo alkohola in dogajanjem na cesti.
