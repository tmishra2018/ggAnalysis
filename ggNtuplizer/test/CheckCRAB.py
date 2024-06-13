#os.system("ls -d crab*/* | awk '{print \"crab status -d \", $1}' >> CrabFolders.txt")
import os
import os.path
from os import path
os.system("rm CrabFolders.txt")
os.system("ls -d */* | awk '{print \"crab status -d \", $1}' >> CrabFolders.txt")
os.system("ls -d */* | awk '{print \"crab resubmit -d \", $1}' >> CrabFolders.txt")
os.system("ls -d */* | awk '{print \"crab report -d \", $1}' >> CrabFolders.txt")

lists = open("CrabFolders.txt","r")
for ij in lists:
         os.system("{}".format(ij.strip()))
#os.system("rm CrabFolders.txt")
