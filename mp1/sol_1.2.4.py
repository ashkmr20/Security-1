#Use code for product tree from https://facthacks.cr.yp.to/product.html
import urllib2
from numpy import prod
from math import floor
from fractions import gcd 
import gmpy
import pbp
from Crypto.PublicKey import RSA
PBPciph= "gAAAAEhySxtWbjagvG9rlmbBmUW+XXmW7m+BLu1t+mykByE50gw3smic5uBPMhAGBexDQFYGtUb8bbgJ5G5Wm1clfuFQssBUYf2pLS9hwet1yCMgFo1+WNErZQa8IxwrAFem/GpkPOAP3BzPD6kxr5basHzwOgNGeTMO2a+6RbioFOKWC35Wi/VvjlbA1Tss9RzQLroOBGiZhxLXhGfk1baSEPnsr+EEQIV3399ibZM6UEzKSdGNndMyQyIMjVS7OMfWqMfuwKpnY0dc7upyn8Z99eM0wle8TqFZ+OXVUBOXv9aqSpqtKnU2N+5iF8j4woo4/Q=="
exp=65537

def producttree(X):
   result = [X]
   while len(X) > 1:
		X = [prod(X[i*2:(i+1)*2]) for i in range((len(X)+1)/2)]
		result.append(X)
   return result


def remaindertree(n,t,originaldata):
	result=[n]
	newtemp=[]
	tot= len(t)
	for k in range(len(t)-1):
		abovelen= len(t[tot-k-1])
		aboveind = tot-k-1
		# print ("here's what you're modin:") 
		# print(result)
		# print("by:")
		# print (t[tot-2-k])

		for j in range(abovelen):
			newtemp.append(result[j] % (t[aboveind-1][j*2] **2))
			if j*2+1 < len(t[tot-2-k]):
				newtemp.append(result[j] % (t[aboveind-1][(j*2)+1] ** 2))
		result = newtemp
		newtemp=[]
	return [gcd(r/n,n) for r,n in zip(result,originaldata)]
	#return result


with open('moduli.hex') as f:
	modata=f.readlines()
modata = [x.strip() for x in modata] 
modata = [int(x,16) for x in modata]


testdata=modata
prodtree = producttree(testdata)
gcdlist = remaindertree(prodtree[-1][0],prodtree,testdata)
# print "Done with remainderlist"
# thefile = open('remlist.txt', 'w')
# for item in gcdlist:
#  thefile.write("%s\n" % item)
# with open('remlist.txt') as f:
# 	remdata=f.readlines()
# remdata = [x.strip() for x in remdata] 
# remdata = [int(x) for x in remdata]
remdata = gcdlist
indexofgcd= []
gcdarraywithoutones=[]
for x in range(len(remdata)):
	if remdata[x]!=1:
		gcdarraywithoutones.append(remdata[x])
		indexofgcd.append(x)
#remdata= [x for x in remdata if x!=1]
# thefile = open('indexesofgcd.txt', 'w')
# for item in indexofgcd:
#  thefile.write("%s\n" % item)
#print len(gcdarraywithoutones)
# thefile = open('remlistfactored.txt', 'w')
# for item in gcdarraywithoutones:
#  thefile.write("%s\n" % item)


psandqs =[]
#print len(gcdarraywithoutones)
#print len(indexofgcd)
for indexofindex in range(len(indexofgcd)):
	modulfound= testdata[indexofgcd[indexofindex]]
	psandqs.append( modulfound/ gcdarraywithoutones[indexofindex]) 
privkeys=[]
RSAkeys =[]
constructKeys=[]
for i in range(len(psandqs)):
	totient= gmpy.lcm(psandqs[i]-1,gcdarraywithoutones[i]-1)
	privkeys.append(gmpy.invert(exp,totient))

# thefile = open('privkeys.txt', 'w')
# for item in privkeys:
#  thefile.write("%s\n" % item)

for indexofindex in range(len(indexofgcd)):
	constructKeys.append([long(testdata[indexofgcd[indexofindex]]),long(exp),long(privkeys[indexofindex])])

for key in constructKeys:
	RSAkeys.append(RSA.construct(key))

for key in RSAkeys:
	try:
		result=	pbp.decrypt(key, open('1.2.4_ciphertext.enc.asc').read())
	except ValueError:
    		pass 
with open('sol_1.2.4.txt', "w") as outp:
    outp.write(result)
# for i in range(len(testdata)):
# 	gcdlist[i]=gcdlist[i]/testdata[i]
#print gcdlist

#with open('remlistfactored.txt','r') as g:
# 	gcdwoones=g.readlines()
# print(len(gcdwoones))
# gcdwoones = [x.strip() for x in gcdwoones] 
# gcdwoones = [int(x) for x in gcdwoones]