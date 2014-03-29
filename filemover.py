import os
import shutil
cwd=os.getcwd()
for i in os.listdir(cwd):
    filename=str(i)
    if filename.lower().endswith("pdf") or filename.lower().endswith("doc") or filename.lower().endswith("docx") or filename.lower().endswith("xls") or filename.lower().endswith("xlsx"):
        print "Document - "+filename
        shutil.move(filename,"/home/balasankarc/Documents/"+filename)
    elif filename.lower().endswith("jpg") or filename.lower().endswith("png") or filename.lower().endswith("tif") or filename.lower().endswith("tiff"):
        shutil.move(filename,"/home/balasankarc/Pictures/"+filename)
        print "Picture - "+filename
    elif filename.lower().endswith("mp3") or filename.lower().endswith("wav"):
        shutil.move(filename,"/home/balasankarc/Music/"+filename)
        print "Music  - "+filename
    elif filename.lower().endswith("rar") or filename.lower().endswith("zip") or filename.lower().endswith("gz"):
        shutil.move(filename,"/home/balasankarc/Downloads/Compressed/"+filename)
        print "Compressed  - "+filename
    elif filename.lower().endswith("torrent"):
        shutil.move(filename,"/home/balasankarc/Downloads/Torrents/"+filename)
        print "Compressed  - "+filename
