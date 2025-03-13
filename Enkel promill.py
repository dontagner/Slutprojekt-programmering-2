# Tar in användarens input
storlek = float(input("Hur mycket har du druckit i ml: "))
procent = float(input("Hur många procent var den: "))
vikt = float(input("Hur mycket väger du?: "))

# Funktion för att räkna ut alkohol i gram
def alkohol_gram(storlek, procent):
    alk = storlek * (procent / 100) * 0.8
    return alk

# Beräknar alkoholmängden
alkoholmängd = alkohol_gram(storlek, procent)

# Widmarks formel för att räkna promille
def räkna_promille(alkoholmängd, vikt, kön):
    if kön.lower() == "man":
        vattendel = 0.7
    else:
        vattendel = 0.6
    promille = alkoholmängd / (vikt * vattendel)
    return promille

# Frågar om kön
kön = input("Är du man eller kvinna? (man/kvinna): ")

# Beräknar promille
promillehalt = räkna_promille(alkoholmängd, vikt, kön)
print(f"Din uppskattade promillehalt är {promillehalt:.2f} ‰")

# Förbränning över tid
tid = float(input("Hur många timmar har gått sedan du började dricka?: "))
förbränt = tid * 0.15  # Förbränner ca 0.15 promille per timme
slutlig_promille = max(promillehalt - förbränt, 0)

print(f"Efter {tid} timmar är din beräknade promillehalt {slutlig_promille:.2f} ‰")
