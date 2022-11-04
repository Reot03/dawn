inFp = None
inStr = ""

inFp = open("1104.txt","r", encoding="utf-8")

while True :
    inStr = inFp.readline()
    if inStr == "":
        break;
    print(inStr,end="")

inFp.close()