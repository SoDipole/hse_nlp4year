import rake

with open("moomins.txt", "r", encoding="utf-8") as f:
    text = f.read()
    
rake_object = rake.Rake("SmartStoplist.txt", 1, 3)

keywords = rake_object.run(text)

# 3. print results
print("Keywords:")
for word in keywords:
    print(word)