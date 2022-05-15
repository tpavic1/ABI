def Rekurzija(mass,masses,counter):

    if (mass in counter):  
        return counter[mass]

    if mass < 0: # znaci 
        return 0

    if mass == 0:
        return 1

    counter[mass]=0
    for mass_ in masses:
        counter[mass]+=Rekurzija(mass-mass_,masses,counter)
    
    return counter[mass]


def GivenMassProblem(mass):

    mass_dict = {
        "G": 57,
        "A": 71,
        "S": 87,
        "P": 97,
        "V": 99,
        "T": 101,
        "C": 103,
        "I": 113,
        "L": 113,
        "N": 114,
        "D": 115,
        "K": 128,
        "Q": 128,
        "E": 129,
        "M": 131,
        "H": 137,
        "F": 147,
        "R": 156,
        "Y": 163,
        "W": 186,
    }

    counter={}

    return Rekurzija(mass,set(mass_dict.values()),counter)  # pazi,ovde ide set jer dva imaju isto
  
  
  ### ispis
  
  print(GivenMassProblem(1272))
  
  
 
  
  
  
  
  
  
  
  
