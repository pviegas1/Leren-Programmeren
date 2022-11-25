# prijs dagje uit bij de speelhal

aantalpersonen = int (input ('met hoeveel personen?'))
ticket = 7.45
entree = aantalpersonen * ticket 
tijdper_periode = 7
zitplek_perperiode = 0.37
aantalminuten = int (input ('hoeveel minuten verblijft u?'))
zitplek_perperiode = aantalminuten / tijdper_periode
prijs_seat = (zitplek_perperiode * zitplek_perperiode) * aantalpersonen

te_betalen = round (ticket + prijs_seat, 2)
print (te_betalen)    
