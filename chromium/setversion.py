#!/usr/bin/env python2.7
import json
from datetime import date

# Set the version in manifest.json to one based on today's date.

t = date.today()
f = open('chromium/manifest.json')
manifest = json.loads(f.read())
f.close()
manifest['version'] = `t.year` +'.'+ `t.month` +'.'+ `t.day`
f = open('chromium/manifest.json','w')
f.write(json.dumps(manifest,indent=4,sort_keys=True))
