#!/usr/bin/env python
#
ip = raw_input(":")
mask = raw_input(":")
ip_list = ip.split(".")
mask_list= mask.split(".")
print ip_list
print mask_list
for i in range(0,4):
    print int(ip_list[i]) & int(mask_list[i]),
for i in range(0,4):
    print int(ip_list[i]) | (255-int(mask_list[i])),
