import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook,load_workbook

def lot3(self):
    url = "https://www.dhlottery.co.kr/gameResult.do?method=statByNumber"
    url1 = "https://dhlottery.co.kr/gameResult.do?method=statGroupNum"
    url2 = "https://dhlottery.co.kr/gameResult.do?method=noViewNumber"

    req = requests.get(url)
    req1 = requests.get(url1)
    req2 = requests.get(url2)

    req.encoding="euc-kr"
    req1.encoding="euc-kr"
    req2.encoding="euc-kr"

    bs =BeautifulSoup(req.text,"html.parser")
    bs1 = BeautifulSoup(req1.text,"html.parser")
    bs2 = BeautifulSoup(req2.text,"html.parser")


    numbers = bs.select("#printTarget > tbody > tr > td:nth-child(3)")
    numbers1= bs1.select("#article > div:nth-child(2) > div > table > tbody > tr > td:nth-child(3)")
    numbers2= bs1.select("#article > div:nth-child(2) > div > table > tbody > tr > td:nth-child(1)")
    mynonappear = []
    mylist = []

    mylist1 = []
    mylist2 = []
    mynumlist1 = []
    mynumlist2 = []
    mynumlist3 = []
    mynumlist4 = []
    mynumlist5 = []
    mytitle = []

    tenth = bs2.select("#article > div:nth-child(2) > div > table > tbody > tr:nth-child(1) > td.ta_left > span")
    twentieth = bs2.select("#article > div:nth-child(2) > div > table > tbody > tr:nth-child(2) > td.ta_left > span")
    thirthieth = bs2.select("#article > div:nth-child(2) > div > table > tbody > tr:nth-child(3) > td.ta_left > span")
    fortieth = bs2.select("#article > div:nth-child(2) > div > table > tbody > tr:nth-child(4) > td.ta_left > span")
    fifieth = bs2.select("#article > div:nth-child(2) > div > table > tbody > tr:nth-child(5) > td.ta_left > span")

    for i in tenth:
        mynumlist1.append(i.text)
    for i in twentieth:
        mynumlist2.append(i.text)
    for i in thirthieth:
        mynumlist3.append(i.text)
    for i in fortieth:
        mynumlist4.append(i.text)
    for i in fifieth:
        mynumlist5.append(i.text)






    for i in numbers2:
        mytitle.append(i.text.strip())

    # for i in numbers3:
    #     mynonappear.append(i.text)




    mylist1 = list(numbers1)
    for i in mylist1:
        mylist2.append(i.text)



    for tenth in range(0,10):
        mylist.append(str(numbers[tenth].text)+"회"+"/"+str(tenth+1)+"번")

    for twentieth in range(10,20):
        mylist.append(numbers[twentieth].text+"회"+"/"+str(twentieth+1)+"번")

    for thirthieth in range(20,30):
        mylist.append(numbers[thirthieth].text+"회"+"/"+str(thirthieth+1)+"번")

    for fortieth in range(30,40):
        mylist.append(numbers[fortieth].text+"회"+"/"+str(fortieth+1)+"번")

    for fifieth in range(40,45):
        mylist.append(numbers[fifieth].text+"회"+"/"+str(fifieth+1)+"번")


    wb = Workbook()
    ws = wb.active

    ws.append(mylist)
    a= min(mylist)
    b= max(mylist)
    # print(a)
    # print(b)
    ws.append([a])
    ws.append([b])
    ws.append(mylist2)
    ws.append(mytitle)
    ws.append(mynumlist1)
    ws.append(mynumlist2)
    ws.append(mynumlist3)
    ws.append(mynumlist4)
    ws.append(mynumlist5)




    wb.save('lotto/totalnum.xlsx')
    wb.close()







