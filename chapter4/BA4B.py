def Complement(letter):
  if(letter=="A"):
    return "T"
  elif(letter=="C"):
    return "G"
  elif(letter=="G"):
    return "C"
  else:
    return "A"

def ReverseComplement(dna):
    complement=[Complement(n) for n in dna]
    return "".join(complement[::-1])

def DnaToRna(dna):
    rna=""
    for n in dna:
        if n=="T":
            rna+="U"
        else:
            rna+=n
    return rna

def ProteinTranslation(pattern):
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
    peptide=""
    for i in range(0,len(pattern)-3+1,3):
        codon=pattern[i:i+3]
        if(codon=="UAA" or codon=="UAG" or codon=="UGA"):
            break
        peptide+=genetic_code[codon]
    return peptide

def PeptideEncoding(dna, peptide):
    substrings=[]
    lenSubstring=len(peptide)*3
    
    for i in range(len(dna)-lenSubstring+1):
        substring=dna[i:i+lenSubstring]
        complement=ReverseComplement(substring)
        
        substringRna=DnaToRna(substring)
        complementRna=DnaToRna(complement)
        
        substringProtein=ProteinTranslation(substringRna)
        complementProtein=ProteinTranslation(complementRna)
        
        if (substringProtein==peptide or complementProtein==peptide):
            substrings.append(substring)
            
    return substrings

### ispis

sample_=''''''
sample=sample_.splitlines()
dna=sample[0]
peptide=sample[1]

res=PeptideEncoding(dna, peptide)
for r in res:
    print(r)
    
