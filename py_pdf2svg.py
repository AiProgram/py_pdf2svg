#%%
from pathlib import PurePosixPath
from pathlib import Path
import os
import time

name2id={}
id2name={}
id=0
poppler_bin_path="D:/projects/others/poppler-20.12.1/Library/bin"
os.popen("cd "+poppler_bin_path)
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
    out=os.popen(r"pdftocairo -svg "+p.resolve().name+" "+new_p.resolve().name)
    time.sleep(0.3)
for id in id2name:
    p=Path("##"+str(id)+".pdf")
    p.rename(id2name[id]+".pdf")
    p=Path("##"+str(id)+".svg")
    p.rename(id2name[id]+".svg")

print("conversion completed!")
# %%
