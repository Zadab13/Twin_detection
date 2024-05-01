
# in deze fucntie wordt het 'beste' gekozen uit de lijst percentages, 
# dit is dus de X en Y met de laagste distance, want deze lijken het meest op elkaar, de laagste distance wordt gevonden door de fucntie min
# min pakt het kleinste element van de derde elementen in de lijst percentages
# key = lambda deifinieert een soort 'mini-functie' met argument t waarvoor dan t[2] oftewel het derde element wordt gepakt van de lijst perventages
# je krijgt de dan tuple best terug


def find_best(percentages):
    best = min(percentages, key = lambda t: t[2])
    return best
