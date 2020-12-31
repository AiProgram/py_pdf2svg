#%%
from pathlib import PurePosixPath
from pathlib import Path
import os
import time
import subprocess

name2id={}
id2name={}
id=0
poppler_bin_path="./poppler-20.12.1/Library/bin"
subprocess.Popen("cd "+poppler_bin_path, stdout=subprocess.PIPE, shell=True)
pdf_file_path=Path("./")
for p in pdf_file_path.iterdir():
    if p.is_file() and p.suffix==".pdf":
        name2id[p.stem]=id
        id2name[id]=p.stem
        id+=1
for id in id2name:
    p=Path(id2name[id]+".pdf")
    new_name="##"+str(id)+".pdf"
    out_name="##"+str(id)+".svg"
    p.rename(new_name)
    p=Path(new_name)
    new_p=Path(out_name)
    subprocess.Popen(r"pdftocairo -svg "+p.resolve().name+" "+new_p.resolve().name, stdout=subprocess.PIPE, shell=True).wait()
for id in id2name:
    p=Path("##"+str(id)+".pdf")
    p.rename(id2name[id]+".pdf")
    p=Path("##"+str(id)+".svg")
    p.rename(id2name[id]+".svg")

print("conversion completed!")
# %%
