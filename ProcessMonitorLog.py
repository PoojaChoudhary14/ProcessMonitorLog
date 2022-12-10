import os
import psutil
import time
from sys import *
import os

def ProcessDisplay(log_dir="Marvellous"):
    listprocess=[]

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator="-"*80
    log_path=os.path.join(log_dir,"MarvellousLog%s.log"%(time.ctime()))
    print(log_path)
    log_path=log_path.replace(" ","")
    log_path=log_path.replace(":","")
    print(log_path)
    #log_path=os.path.join(log_dir,"MarvellousLog.log")
    f=open(log_path,'w')
    f.write(separator+"\n")
    f.write("Marvellous Infosystems Process Logger:"+time.ctime()+"\n")
    f.write(separator+"\n")

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=["pid","name","username"])
            pinfo['vms']=proc.memory_info().vms/(1024*1024)
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n"%element)

def main():
    

    print("Application name:",argv[0])

    if(len(argv)!=2):
        print("Error: Invalid number of arguments")
        exit()

    if(argv[1]=="-h" or argv[1]=="-H"):
        print("This script is used to log record of running process")
        exit()
    
    if(argv[1]=="-u" or argv[1]=="-U"):
        print("Usage: Application Name AbsolutePath_of_Directory")
        exit()

    try:
        ProcessDisplay(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")


if __name__=="__main__":
    main()