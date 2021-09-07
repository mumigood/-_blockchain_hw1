#!/usr/bin/env python
# coding: utf-8

# In[23]:


get_ipython().run_cell_magic('file', 'test.py', 'import argparse\nimport time\nimport hashlib\nimport binascii\nimport pickle\nimport os\n\n\n\n\n\n\n\ndef p_o_w(a,b):\n    bb = 2**(256-b)\n    aa = int(a, 16)\n    if aa<bb:\n        return 1\n    else:\n        return 0\nclass block(object):\n    def __init__(self,trans,prevhash=""):\n        self.time = str(time.time())\n        self.bits = 10\n        self.nouce = None\n        self.trans = trans\n        self.hash = None\n        self.prevhash = prevhash\n        self.height = None\n    def sethash(self):\n        tohash = self.time+self.trans+self.prevhash\n        h = hashlib.sha256()\n        tohash = tohash.encode()\n        h.update(tohash)\n        myhash = h.hexdigest()\n        self.hash = myhash\n    def newblock(trans):\n        print("mi")\n\n        \nclass blockchains(object):\n    def __init__(self):\n        self.blocks = []\n        self.name = "titan"\n        self.hash = None\n        self.length = -1\n        self.bits = 5\n    def addblock(self,newblock):\n        self.blocks.append(newblock)\n        self.length+=1\n    def addnew_block(self,trans):\n        t=0\n        l = self.length\n        while t <6553500:\n            tempblock = block(trans,self.blocks[l].hash)\n            tempblock.sethash()\n            if p_o_w(tempblock.hash,self.bits) == 1:\n                self.addblock(tempblock)\n                break\n            else:\n                t+=1     \n    def sethash(self):\n        print(a)\n    def showblockchains(self):\n        for i in self.blocks:\n            print(i.hash)\n\n            \n##############################CLI設置           \nparser = argparse.ArgumentParser()\nparser.add_argument("arg1",\n                    nargs=1,\n                    help = "該做什麼，請輸入一個字串 addblock,printchain,printblock"\n                   )\n\nparser.add_argument("--height",\n                    nargs=\'?\',\n                    type=int,\n                    default = 1,\n                    help = "高度的參數，請輸入一個整數"\n                   )\n\nparser.add_argument("--transaction",\n                    nargs=\'?\',\n                    type=str,\n                    default = "none trans",\n                    help = "交易的參數，請輸入一個字串，若不輸入則填入none trans"\n                   )\n\nargs = parser.parse_args()\n\n\nprint(args)\n\n#####################CLI設置結束###############\n\n######################哼哼#################\nisdata_notexist = 0       \nfilepath = "data.pkl"\nif os.path.isfile(filepath):\n    print("檔案存在。")\nelse:\n    isdata_notexist = 1  \n    print("檔案不存在。")\n    \n######################\n###處理各個CLI########\n#####################\n\nif args.arg1!="addblock" and isdata_notexist == 1:\n    print("請先創立一個blockchains")\n    os._exit()\n    \nelif isdata_notexist == 1 and args.arg1=="addblock" :\n    print("創立創世區塊")\n    titan = blockchains()\n    eren = block("aaaa","45874")\n    eren.sethash()\n    titan.addblock(eren)\n    print(eren.time)\n    armin = block(eren.trans,eren.hash)\n    armin.sethash()\n    titan.addblock(armin)\n    titan.length = 1\n    with open(\'data.pkl\', \'wb\') as f:\n        pickle.dump(titan,f)\n    os._exit()\n\n                    \nelse:\n    if args.arg1=="addblock":\n        print("當前難度換算為16進位")\n        print (hex(2**(251)))\n        with open(\'data.pkl\', \'rb\') as f:\n            azula = pickle.load(f)\n            print("aa")\n            azula.addnew_block(transaction)\n    elif args.arg1=="printchain":\n        with open(\'data.pkl\', \'rb\') as f:\n            azula.showblockchains()\n    elif args.arg1=="printblock":\n        with open(\'data.pkl\', \'rb\') as f:\n            if height<azula.blocks.len():  \n                print(azula.blocks[height].hash)\n            else:\n                print("輸入的高度大於鍊長")\n\nwith open(\'data.pkl\', \'wb\') as f:\n    pickle.dump(azula,f)   ')


# In[26]:


get_ipython().run_cell_magic('!', '', 'python ex.py printchain')


# In[ ]:





# In[ ]:





# In[ ]:




