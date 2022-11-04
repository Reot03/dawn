inFp = None
inStr = ""

inFp = open("1104.txt","r", encoding="utf-8")

inStr = inFp.readline()
print(inStr,end="")

inStr=inFp.readline()
print(inStr,end="")

inStr=inFp.readline()
print(inStr,end="")

inFp.close()