#! /usr/bin/python
import os
import sys
import shutil
try:
    cwd = sys.argv[1]
except:
    cwd=os.getcwd()
for i in os.listdir(cwd):
    filename=str(i)
    filepath=cwd+"/"+filename
    if filepath.lower().endswith("pdf") or filepath.lower().endswith("doc") or filepath.lower().endswith("docx") or filepath.lower().endswith("xls") or filepath.lower().endswith("xlsx") or filepath.lower().endswith("odt"):
        print "Document - "+filename
        shutil.move(filepath,"/home/balasankarc/Documents/"+filename)
    elif filepath.lower().endswith("jpg") or filepath.lower().endswith("png") or filepath.lower().endswith("tif") or filepath.lower().endswith("tiff") or filepath.lower().endswith("svg"):
        shutil.move(filepath,"/home/balasankarc/Pictures/"+filename)
        print "Picture - "+filename
    elif filepath.lower().endswith("mp3") or filepath.lower().endswith("wav"):
        shutil.move(filepath,"/home/balasankarc/Music/"+filename)
        print "Music  - "+filename
    elif filepath.lower().endswith("rar") or filepath.lower().endswith("zip") or filepath.lower().endswith("gz") or filepath.lower().endswith("xz"):
        shutil.move(filepath,"/home/balasankarc/Downloads/Compressed/"+filename)
        print "Compressed  - "+filename
    elif filepath.lower().endswith("torrent"):
        shutil.move(filepath,"/home/balasankarc/Downloads/Torrents/"+filename)
        print "Torrent - "+filename
    elif filepath.lower().endswith("deb"):
        shutil.move(filepath,"/home/balasankarc/Downloads/Torrents/"+filename)
        print "Setup FIle  - "+filename
