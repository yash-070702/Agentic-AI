with open("sample.txt", "r", encoding="utf-8", errors="replace") as f:
 content=f.read()


for line in content:
    print(line)

f.close()
