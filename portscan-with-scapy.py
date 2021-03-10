#!/usr/bin/python3
import sys
from scapy.all import *

#don't show informations
conf.verb=0

ports = [21,22,23,25,80,110,443] #ports

#creating packet
syn = IP(dst=sys.argv[1])/TCP(dport=ports)

#sending & receveing
answ, noansw = sr(syn)

#checking SYN/ACK (SA) flags
for answer in answ:
    port = answer[1][TCP].sport
    flag = answer[1][TCP].flags

    if flag == "SA":
        print(f"[+] PORT {port} OPEN")
