import json

fp = open("poem.json", "r", encoding="utf-8")
rawdata = fp.read()
fp.close()

data = json.loads(rawdata)
print("詩名：", data[0]['title'])
print("作者：", data[0]['author'])
print("內容：", "".join(data[0]['paragraphs']))