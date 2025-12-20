txt = 'hello hi How ARE you?'
for i in txt:
    print(i)

print("hi 9 to 5".isalnum())
print("ho9to5".isalnum())


print(txt.count("lo"))
print(txt.lower().count("you"))

print(txt.lower().replace("you", "mee"))

print(txt.lower().isspace())

words = txt.split()
print(words)
print(words[0])


print(txt.lower().find("hi"))