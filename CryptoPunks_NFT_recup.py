"""
A partir de l'adresse HTTP, récup des NFT au format PNG
Auteur: Fabrice Heuvrard
Date : 24/04/2022
Entrée : Adresse HTML du de l'image qui s'incrémente automatiquement
Résultat : fichier svg des NFT avec leur numéro dans le nom
"""

# importation des modules nécessaires
import urllib.request
import time
import os
from urllib.request import Request, urlopen

adresse_generique = "https://www.larvalabs.com/public/images/cryptopunks/punk"
#https://www.larvalabs.com/public/images/cryptopunks/punk1000.png

x=271
while x <10000:
    if x>=1000:
        URL_img = str(adresse_generique)+str(x)+".png"
    elif x>=100:
        URL_img = str(adresse_generique)+str("0")+str(x)+".png"
    elif x>=10:
        URL_img = str(adresse_generique)+str("00")+str(x)+".png"
    else:
        URL_img = str(adresse_generique)+str("000")+str(x)+".png"
    print(URL_img)
    print("Image : ",x)
    print("Reste :", 10000-x)
    nom_fichier = "NFT_CryptoPunks_" + str(x) + ".png"
    f = open(nom_fichier,'wb')
    f.write(urllib.request.urlopen(Request(URL_img,headers={'User-Agent': 'Mozilla/5.0'})).read())
    f.close()
    x=x+1
    #time.sleep(1)










    
