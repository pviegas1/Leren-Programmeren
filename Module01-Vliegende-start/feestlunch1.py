print('voer hier je bestelling in ')
croissantjes = int(input('hoeveel croissantjes wilt u?'))
totaalcroissantjes = croissantjes * 0.39
stokbrood = int(input('hoeveel stokbrood wilt u?'))
stokbroodtotaal = stokbrood * 2.78
aantalkortingsbonen = int(input('hoeveel kortings bonnen heb je?'))
korting = int(input('hoeveel cent zijn ze waard?'))
kortingtotaal = aantalkortingsbonen * korting / 100

totaal= stokbroodtotaal + totaalcroissantjes - kortingtotaal
print({totaal},'euro')
