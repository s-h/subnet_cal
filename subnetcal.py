#!/usr/bin/env python
import copy
import sys
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
    for i in range(0,4):
        boardcast.append(int(ip_list[i]) | (255-int(mask_list[i])))
    host_start=copy.deepcopy(network)
    host_start[3]=network[3]+1
    host_end=copy.deepcopy(boardcast)
    host_end[3]=boardcast[3]-1
    print ip_list
    print mask_list
    print network
    print boardcast
    print host_start
    print host_end

def switch_mask(num):
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


ip = str(sys.argv[1])
mask = switch_mask(int(sys.argv[2]))
init(ip,mask)
