import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'song_site.settings')
django.setup()

from catalog.models import Poem

fp = open("poem.json", "r", encoding="utf-8")
rawdata = fp.read()
fp.close()

data = json.loads(rawdata)

for p in data:
    target = Poem()
    target.title = p['title']
    target.author = p['author']
    target.paragraphs = "".join(p['paragraphs'])
    target.save()
    print(target.title)

