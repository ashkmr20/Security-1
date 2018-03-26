import base64

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import sys
import urllib2


with open('1.2.3_ciphertext.hex') as f:
    cipher= f.read().strip()

def xor(ba1, ba2):
    return "".join(chr(ord(ba1) ^ ord(ba2)) for ba1, ba2 in zip(ba1,ba2))

cipher_blocks = list()
binary = list()
for x in range (0,7):
    range_1 = x*32
    range_2 = x*32 + 32
    cipher_blocks.append(cipher[range_1:range_2])
#    print(cipher_blocks[x])
    binary.append(cipher_blocks[x].decode('hex'))
#    print(binary[x])

# print (guess_2)
# last = xor(binary[5], binary[6]).encode("hex")
# print ( last )
# last = xor(last, guess_2)
# print ( len(last) )
# print ( last )

curr_block=1
num_byte=2

#print cipher_blocks
plaintext= '6c6c2c20756e7370656369666965642063616b652c2069742773206120736d6168697070656420637265616d206f6e206f6e206120706f7461746f206f7220774c696b6520736f757220637265616d20'
decrypt = ''
allblockdecrypt =''
correctguess= 'cf'
decryptnewtwo=''

#last = og ^ padding^ decrypt
# decrypt my guess(bruteforce) ^ x10 ^ c[-1] = plaintext of block 2
#last byte = original last byte ^ corresponding byte from padding scheme (in this case 0f) ^ decrypted byte
# ONLY NEED TO XOR THE PADDING
for curr_block in range(0,6):
    decrypt=''
    trydecrypt =[]
    for num_byte in range(1,17):
        curr_byte= num_byte*2
        found=0
        while found == 0:
            if(len(trydecrypt)>0):
                decrypt = trydecrypt.pop()
            for i in range(0,256):
 
                guess = hex(i)[2:].zfill(2) 

                guess_block=cipher_blocks[curr_block][:32- curr_byte] + guess 
                #bad_ciph = ''.join(cipher_blocks)
                padding=''
                for x in range(num_byte-1):
                    padding= padding+ hex(15-x)[2:].zfill(2)
                if num_byte>1:
                    xorprevguessandpad= xor(padding.decode('hex'),cipher_blocks[curr_block][(32-curr_byte+2):].decode('hex')).encode('hex')
                    
                    padding =xor(xorprevguessandpad.decode('hex'),decrypt.decode('hex')).encode('hex')
                   # print cipher_blocks[curr_block][(32-curr_byte):(32-curr_byte+2)]
                    # print xorprevguessandpad
                    # print cipher_blocks[curr_block][(32-curr_byte+2):]
                    # print decrypt
                    guess_block=guess_block + padding
               # print guess_block
                bad_ciph = guess_block +cipher_blocks[curr_block+1] 
                url_check="http://192.17.90.133:9996/mp1/asathis2/?"
                url_send = url_check + bad_ciph
                #print(url_send)     
                def get_status(u):
                    req = urllib2.Request(u)
                    try:
                        f = urllib2.urlopen(req)
                        print f.code
                    except urllib2.HTTPError, e:
                       
                        return e.code

                error_code= get_status(url_send)
                if error_code ==404:
                    #print guess_block
                    # print guess
                    decryptnewtwo= xor('10'.decode('hex'),guess.decode('hex')).encode('hex')
                    decryptnewtwo= xor(decryptnewtwo.decode('hex'),cipher_blocks[curr_block][(32-curr_byte):(32-curr_byte+2)].decode('hex')).encode('hex')
                    decrypt = decryptnewtwo + decrypt
                    #print decryptnewtwo
                    trydecrypt.append(decrypt)
                    found=1               
                   # print decrypt
                   # if cipher_blocks[curr_block][(32-curr_byte):(32-curr_byte+2)] != guess:
                   # break

    #print "Block Ciphertext:"
    #print decrypt           
    allblockdecrypt =allblockdecrypt + decrypt
#print "Final Ciphertext:"
#print allblockdecrypt

with open('sol_1.2.3.txt', "w") as outp:
    outp.write(allblockdecrypt.decode('hex'))