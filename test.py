import argparse
import time
import hashlib
import binascii
import pickle
import os
import sys







def p_o_w(a,b):
    bb = 2**(256-b)
    aa = int(a, 16)
    if aa<bb:
        return 1
    else:
        return 0
class block(object):
    def __init__(self,trans,prevhash=""):
        self.time = str(time.time())
        self.bits = 10
        self.nouce = None
        self.trans = trans
        self.hash = None
        self.prevhash = prevhash
        self.height = None
    def sethash(self):
        tohash = self.time+self.trans+self.prevhash
        h = hashlib.sha256()
        tohash = tohash.encode()
        h.update(tohash)
        myhash = h.hexdigest()
        self.hash = myhash
    def newblock(trans):
        print("mi")

        
class blockchains(object):
    def __init__(self):
        self.blocks = []
        self.name = "titan"
        self.hash = None
        self.length = -1
        self.bits = 5
    def addblock(self,newblock):
        self.blocks.append(newblock)
        self.length+=1
    def addnew_block(self,trans):
        t=0
        l = self.length
        while t <6553500:
            tempblock = block(trans,self.blocks[l].hash)
            tempblock.sethash()
            if p_o_w(tempblock.hash,self.bits) == 1:
                print("成功挖到礦了，hash值為"+tempblock.hash)
                self.addblock(tempblock)
                break
            else:
                t+=1     
    def showblockchains(self):
        for i in self.blocks:
            print(i.hash)

            
##############################CLI設置           
parser = argparse.ArgumentParser()
parser.add_argument("arg1",
                    nargs=1,
                    type=str,
                    help = "該做什麼，請輸入一個字串 addblock,printchain,printblock"
                   )

parser.add_argument("--height",
                    nargs='?',
                    type=int,
                    default = 1,
                    help = "高度的參數，請輸入一個整數"
                   )

parser.add_argument("--transaction",
                    nargs='?',
                    type=str,
                    default = "none trans",
                    help = "交易的參數，請輸入一個字串，若不輸入則填入none trans"
                   )

args = parser.parse_args()



wtodo = args.arg1[0] 
print("執行 "+wtodo)

#####################CLI設置結束###############
print("目前難度設置為5")
######################哼哼#################
isdata_notexist = 0       
filepath = "data.pkl"
if os.path.isfile(filepath):
    print("區塊鍊檔案存在。")
else:
    isdata_notexist = 1  
    print("區塊鍊檔案不存在。")
    
######################
###處理各個CLI########
#####################

if wtodo!="addblock" and isdata_notexist == 1:
    print("請先創立一個blockchains")
    sys.exit()
    
elif isdata_notexist == 1 and wtodo=="addblock" :
    print("創立創世區塊")
    titan = blockchains()
    eren = block("aaaa","45874")
    eren.sethash()
    titan.addblock(eren)
    print(eren.time)
    armin = block(eren.trans,eren.hash)
    armin.sethash()
    titan.addblock(armin)
    titan.length = 1
    with open('data.pkl', 'wb') as f:
        pickle.dump(titan,f)
    sys.exit()

                    
else:
    print("成功讀取區塊鍊檔案")
    if wtodo=="addblock":
        print("當前難度換算為16進位為"+str(hex(2**(251))))

        with open('data.pkl', 'rb') as f:
            azula = pickle.load(f)
            azula.addnew_block(args.transaction)
        with open('data.pkl', 'wb') as f:
            pickle.dump(azula,f)   
            
    elif wtodo=="printchain":
        with open('data.pkl', 'rb') as f:
            azula = pickle.load(f)
            azula.showblockchains()
            
    elif wtodo=="printblock":
        with open('data.pkl', 'rb') as f:
            azula = pickle.load(f)
            if args.height<len(azula.blocks):
                print("輸出第"+str(args.height)+"個塊")
                print(azula.blocks[args.height].hash)
            else:
                print("輸入的高度大於鍊長")
    else:
        print("沒有對應的指令")


