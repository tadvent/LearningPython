import os,sys

def readcategory():
    category = []
    cfg = open("config.ini")
    for cat,path in (line.split("=",1) for line in cfg if (line[0]!=";" and line[0]!="\n")):
        if path[-1] == "\n":
            path = path[:-1]
        category.append((cat,path,))
    return category

def calsize(path):
    return sum( sum(os.path.getsize(os.path.join(dirpath,name)) for name in filenames) for dirpath,dirnames,filenames in os.walk(path) )

def makeinput(path):
    file = open(os.path.join(path,"input.txt"),"w")
    file.write("4480 10\n\n")
    for dirname in (dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path,dir))):
        file.write(dirname.replace(" ","")+"\t"+( "%.3f" % (1.0*calsize(os.path.join(path,dirname))/1024/1024) )+"\n")
    file.close()

if __name__ == "__main__":
    for cat,path in readcategory():
        if calsize(path)>4483*1024*1024:
            makeinput(path)
            print (cat, "is larger than 4.38GB")
    print
    os.system("pause")
