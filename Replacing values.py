txt1 = "hello how are you are? are you okay? are you coming today?"

pos_1= txt1.lower().find("are")
print(pos_1)                  #14
txt2 = txt1[pos_1 + 1:]    
print(txt2)                   #o

txt2= txt1[:pos_1 +1]
print(txt2)  


txt3 = txt1[:pos_1 +1] + txt1[pos_1 + 1:].lower().replace("are","we",2)
print(txt3)



new = "ABABABCABCUC"
    #  0123456789
pos = new.find("C")   #6
print(pos)

txt = new[:pos + 1] + new[pos +1:].replace("C","G",1)
print(txt)