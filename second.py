import os
cmd="tshark -r capture1.pcapng -T fields -e ip.dst ip.src| sort |uniq "
os.system(cmd)
