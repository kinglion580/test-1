#!/usr/bin/env python3
import sys
import csv
from multiprocessing import Process,Queue
class Args:
    def __init__(self):
        s = sys.argv[1:]
        self.c = s[s.index('-c')+1]
        self.d = s[s.index('-d')+1]
        self.o = s[s.index('-o')+1]

args = Args()

class Config:
    def __init__(self):
        self.config = self.read_config()
    def read_config(self):
        config = {'s': 0}
        with open(args.c,'r') as file:
              for line in file.readlines():
                    key, value = line.strip().split("=")
                    key = key.strip()
                    if key == 'JiShuL' or key == 'JiShuH':
                        config[key] = float(value)
                    else:
                        config['s'] += float(value)
        return config

    
config = Config().config

def read(q):
    with open(args.d) as f:
            data = list(csv.reader(f))
    q.put(data)

def jisuan(q1, q2):
    if not q1.empty():
        newdata_1 = []
        data = q1.get()
        for a,b in data:
            salary = int(b)
            if salary < config['JiShuL']:
                shebao = config['JiShuL'] * config['s']
            elif salary > config['JiShuH']:
                shebao = config['JiShuH'] * config['s']
            else:
                shebao = salary * config['s']
            ynsdr = salary - shebao - 3500
            if ynsdr <= 0:
                shui = 0
            elif  0 < ynsdr <= 1500:
                shui = ynsdr * 0.03 
            elif 1500 < ynsdr <= 4500:
                shui = ynsdr * 0.1 - 105
            elif 4500 < ynsdr <= 9000:
                shui = ynsdr * 0.2 - 555
            elif 9000 < ynsdr <= 35000:
                shui = ynsdr * 0.25 - 1005
            elif 35000 < ynsdr <= 55000:
                shui = ynsdr * 0.3 - 2755
            elif 55000 < ynsdr <= 80000:
                shui = ynsdr * 0.35 - 5505
            else:
                shui = ynsdr * 0.45 - 13505
            shuihou = salary - shebao - shui
            newdata = [a,salary,format(shebao, '.2f'), format(shui, '.2f'), format(shuihou, '.2f')]
            newdata_1.append(newdata)
        q2.put(newdata_1)

def write(q):
        if not q.empty():
            newdata_2 = q.get()
            with open(args.o,'w')as file:
                csv.writer(file).writerows(newdata_2)

if __name__ == '__main__':
    q1, q2 = Queue(), Queue()
    pw=Process(target=read,args=(q1,))
    pr=Process(target=jisuan,args=(q1, q2))
    pp=Process(target=write,args=(q2,))
    
    pw.start()
    #pw.join()
    pr.start()
    #pr.join()
    pp.start()
    #pp.join()
