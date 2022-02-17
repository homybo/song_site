import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'song_site.settings')
django.setup()

from catalog.models import poem

fp = open("poem.json", "r", encoding="utf-8")
rawdata = fp.read()
fp.close()

data = json.loads(rawdata)

for i in range(len(data)):
    {poem.objects.create(title=data[i]['title'] ,author=data[i]['author'] ,paragraphs=''.join(data[i]['paragraphs']))}


