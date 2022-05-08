import os
import os.path as path
import subprocess

curpath = path.dirname(__file__)
outpath = path.dirname(curpath)
for p in os.listdir(curpath):
    if not p.endswith('.json'):
        continue
    #subprocess.call(["jsonschema2popo2", "--translate-properties", "--use-types", "-o", path.join(outpath, p.split('.')[0] + '.py'), path.join(curpath, p)])
    print("Converting %s" % p)
    subprocess.call(["jsonschema2popo2", "--use-types", "-o", path.join(outpath, p.split('.')[0] + '.py'), path.join(curpath, p)])