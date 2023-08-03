import requests
import numpy as np
from bs4 import BeautifulSoup, Tag
import threading
def result(begin):
    for idx in range(begin, (begin+10000000)):
        sbd=idx
        page = requests.get("https://vietnamnet.vn/giao-duc/diem-thi/tra-cuu-diem-thi-tot-nghiep-thpt/2023/{}.html".format(idx))
        try:
            if page.status_code is not 404:
                print("[GET] {}/99999999".format(idx))
                soup = BeautifulSoup(page.text, "html.parser")
                parent = soup.find_all("div", {"class": "resultSearch__right"})
                elements = soup.find_all("td")
                n = 2
                elements = [elements[i:i+n] for i in range(0, len(elements), n)]
                subjects = {'sbd':'',
                            'Toán': '',
                            'Lí': '',
                            'Hóa': '',
                            'Sinh': '',
                            'Ngoại ngữ': '',
                            'A0': '',
                            'A1': '',
                            'B0': '',
                            'D07': '',
                            }
                for element in elements:
                    for key, value in subjects.items():
                        if element[0].text == key:
                            subjects[key] = element[1].text
                subjects['sbd']=str(sbd)
                
                try:subjects['A0']= str(np.sum([float(subjects['Toán']),float(subjects['Lí']),float(subjects['Hóa'])]))
                except ValueError:pass
                try:subjects['A1']= str(np.sum([float(subjects['Toán']),float(subjects['Lí']),float(subjects['Ngoại ngữ'])]))
                except ValueError:pass
                try:subjects['B0']= str(np.sum([float(subjects['Toán']),float(subjects['Sinh']),float(subjects['Hóa'])]))
                except ValueError:pass             
                try: subjects['D07']= str(np.sum([float(subjects['Toán']),float(subjects['Ngoại ngữ']),float(subjects['Hóa'])]))
                except ValueError:pass
                line = ','.join([v for v in subjects.values()])
                if line[-4:]==',,,,': continue
                
                w.write(line + '\n')
        
            else:
                print("[INFO] {}/99999999: no data".format(idx))
        except: continue
path_name='/Users/khangphan/Desktop/thpt_valid_df.csv'
with open(path_name, 'w', encoding='utf-8') as w:
    w.write('sbd,TO,VL,HH,SH,NN,A0,A1,B0,D07\n')


    # thread
    if __name__ =="__main__":
        t1=threading.Thread(target=result,args=(10000000,))
        t2=threading.Thread(target=result,args=(30000000,))
        t3=threading.Thread(target=result,args=(40000000,))
        t4=threading.Thread(target=result,args=(50000000,))
        t5=threading.Thread(target=result,args=(60000000,))
        t6=threading.Thread(target=result,args=(70000000,))
        t7=threading.Thread(target=result,args=(80000000,))
        t8=threading.Thread(target=result,args=(20000000,))
        t9=threading.Thread(target=result,args=(90000000,))
        # start threads
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        # join threads
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        t9.join()
        # done check
        print('done!')