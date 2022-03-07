def Fja(k,text):
  d={}
  for i in range(((len(text)-k)+1)):
    k_ric=text[i:i+k]
    if(k_ric in d.keys()):
      d[k_ric]=d[k_ric]+1
    else:
      d[k_ric]=1
  
  all_values = d.values()
  max_value = max(all_values)

  for key in d.keys():
    if(d[key]==max_value):
      print(key)
