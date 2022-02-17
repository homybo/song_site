import json
import os
import django
from catalog.models import poem
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'song_site.settings')
django.setup()

fp = open("poem.json", "r", encoding="utf-8")
rawdata = fp.read()
fp.close()

data = json.loads(rawdata)

poems = rawdata.objects.all()
print(poems[:10])


#print("詩名：", data[0]['title'])
#print("作者：", data[0]['author'])
#print("內容：", "".join(data[0]['paragraphs']))
#