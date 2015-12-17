#!/usr/bin/env python
#test
import copy
import sys
import re
def init(ip,mask):
#    ip = raw_input(":")
#    mask = raw_input(":")
    ip_list = ip.split(".")
    mask_list= mask.split(".")
    network=[]
    boardcast=[]
    default_mask='0'*32
    for i in range(0,4):
        network.append(int(ip_list[i]) & int(mask_list[i]))
#        print(int(ip_list[i]) & int(mask_list[i]))
#        print network
    for i in range(0,4):
        boardcast.append(int(ip_list[i]) | (255-int(mask_list[i])))
    host_start=copy.deepcopy(network)
    host_start[3]=network[3]+1
    host_end=copy.deepcopy(boardcast)
    host_end[3]=boardcast[3]-1
#print ip_list
#print mask_list
    print network
    print boardcast
    print host_start
    print host_end

def lengthTOdotint(num):
    text='0' * 32
    tag = '1'
    text=num * tag + text[num:]
    binmask=[]
    binmask.append(text[0:8])
    binmask.append(text[8:16])
    binmask.append(text[16:24])
    binmask.append(text[24:32])
    decmask=[]
    for i in range(0,4):
        decmask.append(str((int(binmask[i],2))))
    decmask='.'.join(decmask)
    return decmask
def dotintTOlength(dotint):
    text = dotint.split(".")
    m=''
    for i in range(0,4):
        n= bin(int(text[i])).strip('0b')
        print n
        m += n
    return len(m)

def helps():
    print sys.argv[0] + " ip mask"
    print "e.g " + sys.argv[0] +" 192.168.1.0 24"
    print sys.argv[0] + " 192.160.1.0 255.255.255.0"
def printList(alist):
    for i in alist:
        print i,
regexip=r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])'
if re.search(regexip,sys.argv[1]):
    ip = str(sys.argv[1])
    if re.search(regexip,sys.argv[2]):
        mask=sys.argv[2]
    elif int(sys.argv[2]) > 0 and int(sys.argv[2]) < 33:
        mask = lengthTOdotint(int(sys.argv[2]))
    else:
        helps()
        exit()
else:
    helps()
    exit()
init(ip,mask)
