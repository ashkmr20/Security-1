#!/usr/bin/python2.7
import dpkt
import sys
import socket

def main():
    if (len(sys.argv) < 2):
        print "error: need argument"
        sys.exit(1)
    filename = sys.argv[1]
    print "input filename: " + filename
    SYN={}
    ACK={}
    f = open(filename)
    pcap = dpkt.pcap.Reader(f)
    for ts, buf in pcap:
    	try:
    		eth= dpkt.ethernet.Ethernet(buf)
    	except (dpkt.dpkt.NeedData):
    		continue
    	if not isinstance(eth.data, dpkt.ip.IP):
    		continue
    	ip=eth.data
    	if not isinstance(ip.data, dpkt.tcp.TCP):
    		continue
    	tcp=ip.data
    	try:
    		source= socket.inet_ntop(socket.AF_INET, ip.src)
    	except AttributeError:
    		continue
    	try:
    		dest= socket.inet_ntop(socket.AF_INET, ip.dst)
    	except AttributeError:
    		continue
    	syn_flag= (tcp.flags & dpkt.tcp.TH_SYN) != 0
    	ack_flag =( tcp.flags & dpkt.tcp.TH_ACK ) != 0
    	if syn_flag and ack_flag:
    		if dest not in ACK:
    			ACK[dest]=0
    		if dest not in SYN:
    			SYN[dest]=0
    		ACK[dest]+=1
    	if syn_flag and not ack_flag:
    		if source not in SYN:
    			SYN[source]=0
    		if source not in ACK:
    			ACK[source]=0
    		SYN[source]+=1
    for ips in SYN:
    	if (SYN[ips]-ACK[ips]*3) >0:
    		print ips
    	

if __name__ == '__main__':
	main()

	        # try:
	        #     request = dpkt.http.Request(tcp.data)
	        # except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
	        #     continue
    	# except dpkt.dpkt.NeedData: 
    	# 	print "fail"
    	# 	continue
    	# if not isinstance(eth.data, dpkt.ip.IP):
     #    	#print 'Non IP Packet type not supported %s\n' % eth.data.__class__.__name__
     #    	print "fail"
     #    	continue