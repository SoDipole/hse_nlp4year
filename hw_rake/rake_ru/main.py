import rake

with open("moomins.txt", "r", encoding="utf-8") as f:
    text = f.read()
    
rake_object = rake.Rake("SmartStoplist_ru.txt", 1, 3, 1)

keywords = rake_object.run(text)

print("Keywords:")
for word in keywords:
    print(word[0], "\t", word[1])
