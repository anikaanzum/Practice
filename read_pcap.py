import os
import pcapy as p
from scapy.all import *
a = " "
os.system("tshark  -T fields  -e frame.time -e  data.data -w capture1.pcap > capture1.txt -F pcap -c 1000")

data = "capture1.pcap"
a = rdpcap(data)
