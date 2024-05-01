# In dit deel van de code worden alle encodings van de gezichten met elkaar vergeleken.

# Importeer de volgende library: face_recognition
import face_recognition

# In de functie face_comparison met als argument encodings wordt er eerst een nieuwe lege lijst 
# percentages aangemaakt en wordt de lengte van de lijst encodings bepaalt door de functie len(). 
# Daarna wordt er gebruikt gemaakt van een nested loop, dit is een loop binnen een loop die vaak 
# gebruikt met lijsten. X en Y zijn de plaatsen in de lijst van de elementen die steeds met elkaar 
# vergeleken worden. Er word eerst een lus gevormd die alle elementen van de lijst afgaat in een bepaalde 
# range namelijk alle elementen van de lijst, behalve de laatste. In de tweede lus worden alle elementen 
# van de lijst afgegaan beginnend bij het tweede element en eindigend met het laatste. In de lijst distance 
# wordt aan de hand van de functie face_recognition.face_distance() de Xte en de Yde element vergeleken en een 
# waarde aangemaakt die weergeeft hoe gelijkaardig de 2 elementen zijn(distance). Hoe kleiner de waarde hoe meer gelijkaardig de elementen zijn. 
# X, Y en hun distance worden samen opgeslagen in een tuple genaamd result. Deze wordt dan toegevoegd op het einde van de lijst percentages
# nadat de loop gedaan is krijg je een lijst percentages die alle X waarden met alle Y waarden en hun distance bevat
def face_comparison(encodings):
    percentages = []
    n = len(encodings)
    for X in range(n-1):  
        for Y in range(X+1,n):
             distance = face_recognition.face_distance([encodings[X]], encodings[Y])
             result = (X, Y, distance)
             percentages.append(result)
    return percentages

