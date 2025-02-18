words = {}
counter = 0

with open("sample.txt","r+") as file:
    top = int(input("Enter how many top words you wanna see: "))
    while True:
        if not line:
            break
        line = file.readline()
        for word in line.split():
            counter+=1
            word = word.lower().strip(".,!?()[]{}'\"")
            if word in words:
                words[word]+=1
            else:
                words[word]=1

sorted_by_values = dict(sorted(words.items(), key=lambda item: item[1],reverse=True))
print_key,print_value = zip(*sorted_by_values.items())
print(f"Total words: {counter}")
for i in range(0,top):
    print(f"{print_key[i]}:{print_value[i]}")
     