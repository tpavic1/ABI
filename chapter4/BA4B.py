def Complement(letter):
  if(letter=="A"):
    return "T"
  elif(letter=="C"):
    return "G"
  elif(letter=="G"):
    return "C"
  else:
    return "A"
  
def ReverseComplement(pattern):
  complement=[]
  for n in pattern[::-1]:
    complement.append(Complement(n))

  return "".join(complement)


def RnaToDna(rna):
    dna_list=[]
    for i in range(len(rna)):
        if(rna[i]=="U"):
            dna_list.append("T")
        else:
            dna_list.append(rna[i])

    return "".join(dna_list)

def DnaToRna(rna):
    dna_list=[]
    for i in range(len(rna)):
        if(rna[i]=="T"):
            dna_list.append("U")
        else:
            dna_list.append(rna[i])

    return "".join(dna_list)


def PeptideEncoding(dna,peptide):

    genetic_code = {
        "AAA": "K",
        "AAC": "N",
        "AAG": "K",
        "AAU": "N",
        "ACA": "T",
        "ACC": "T",
        "ACG": "T",
        "ACU": "T",
        "AGA": "R",
        "AGC": "S",
        "AGG": "R",
        "AGU": "S",
        "AUA": "I",
        "AUC": "I",
        "AUG": "M",
        "AUU": "I",
        "CAA": "Q",
        "CAC": "H",
        "CAG": "Q",
        "CAU": "H",
        "CCA": "P",
        "CCC": "P",
        "CCG": "P",
        "CCU": "P",
        "CGA": "R",
        "CGC": "R",
        "CGG": "R",
        "CGU": "R",
        "CUA": "L",
        "CUC": "L",
        "CUG": "L",
        "CUU": "L",
        "GAA": "E",
        "GAC": "D",
        "GAG": "E",
        "GAU": "D",
        "GCA": "A",
        "GCC": "A",
        "GCG": "A",
        "GCU": "A",
        "GGA": "G",
        "GGC": "G",
        "GGG": "G",
        "GGU": "G",
        "GUA": "V",
        "GUC": "V",
        "GUG": "V",
        "GUU": "V",
        "UAA": "*",
        "UAC": "Y",
        "UAG": "*",
        "UAU": "Y",
        "UCA": "S",
        "UCC": "S",
        "UCG": "S",
        "UCU": "S",
        "UGA": "*",
        "UGC": "C",
        "UGG": "W",
        "UGU": "C",
        "UUA": "L",
        "UUC": "F",
        "UUG": "L",
        "UUU": "F",
    }

    substring_len=len(peptide)*3
    res=[]
    
    rna=DnaToRna(dna)

    for i in range(len(dna)-substring_len+1):
        substring1=rna[i:i+substring_len]
        substring2=DnaToRna(ReverseComplement(dna[i:i+substring_len]))

        peptide1=""
        peptide2=""
        for j in range(0,substring_len,3):
            codon1=substring1[j:j+3]
            codon2=substring2[j:j+3]

            peptide1+=genetic_code[codon1]
            peptide2+=genetic_code[codon2]

        if(peptide1==peptide):
            res.append(RnaToDna(substring1))
        if(peptide2==peptide):
            res.append(RnaToDna(substring1))
    
    return res
  
  
### ispis
  
sample_=''''''
sample=sample_.splitlines()
dna=sample[0]
peptide=sample[1]

res=PeptideEncoding(dna,peptide)

for r in res:
    print(r)
    
    
    
    
