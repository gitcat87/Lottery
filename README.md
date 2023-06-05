# 로또 당첨 번호 확인

이번에는 당신이 주인공!
<br>
<br>

##  작동 목표

* 사용자는 최신회차 및 지난 게임의 당첨번호와 상금을 확인 할 수 있어야 한다.
<br>
<br>

## 개발 환경

* Python, Qt Designer, VScode, request, beautifulsoup, openpyxl
<br>
<br>

##  구동 과정

<br>

![](https://github.com/gitcat87/Lottery/blob/main/images/image1.png?raw=true)
<br>

#

```python
#program.py

class FirstClass(QWidget) :
    def __init__(self) :
        super().__init__()
        self.ui = uic.loadUi("lotto/number.ui",self) # lotto폴더 아래 number.ui 파일을 로드 합니다

        self.num1.setText("")    #textbox 안에 text값 초기화 숫자 1~6까지
        self.num2.setText("")
        self.num3.setText("")
        self.num4.setText("")
        self.num5.setText("")
        self.num6.setText("")
        self.bns1.setText("")    # 보너스 숫자

        DateTime= datetime.datetime.now() # 날짜 사용하기 위한 변수 선언

        self.date.setText('오늘 날짜: %s년 %s월 %s일' %(DateTime.year, DateTime.month, DateTime.day)) # 날짜 형식 지정
        

        self.calllottery.clicked.connect(self.doA) # 최근조회 실행
        self.numbutton.clicked.connect(self.doB) # 직접입력 조회 실행
        self.data1.clicked.connect(self.doD) # 통계조회 실행
        self.show() # 폼 실행

```

#

* QT Designer로 작성한 Form이 실행된다.

<br>
<br>

![](https://github.com/gitcat87/Lottery/blob/main/images/image2.png?raw=true)
<br>

![](https://github.com/gitcat87/Lottery/blob/main/images/image3.png?raw=true)

#
```python
#lotto4.py

import requests
from bs4 import BeautifulSoup
import time
from openpyxl import Workbook, load_workbook


def lot2(self):
    url ="https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=" #크롤링 할 주소

    req = requests.get(url) # 요청 보내기

    req.encoding="euc-kr" 

    bs = BeautifulSoup(req.text,"html.parser") #beautifulsoup 라이브러리로 html 코드 갈무리 하기

    turn =bs.select("#article > div:nth-child(2) > div > div.win_result > h4 > strong") #회차
    numbers= bs.select("#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span") #당첨번호
    bonus= bs.select("#article > div:nth-child(2) > div > div.win_result > div > div.num.bonus > p > span") #보너스 번호
    potmoney = bs.select("#article > div:nth-child(2) > div > table > tbody > tr:nth-child(1) > td:nth-child(4)") # 당첨금
    pot = potmoney[0].text 
    print("제",turn[0].text)
    print("당첨번호",numbers[0].text,numbers[1].text,numbers[2].text,numbers[3].text,numbers[4].text,numbers[5].text)
    print("보너스번호입니다.",bonus[0].text)
    print()
    if potmoney[0].text=='0원':
        print("1등 당첨자가 없었습니다")
    else:
        print("1등 당첨금",potmoney[0].text)  #확인을 위해 터미널에 출력


    wb= Workbook() #openpyxl로 추출한 데이터 저장하기
    ws= wb.active


    ws.append(['제',turn[0].text])
    ws.append([numbers[0].text,numbers[1].text,numbers[2].text,numbers[3].text,numbers[4].text,numbers[5].text,'+',bonus[0].text]) 

    if potmoney[0].text=='0원':
        ws.append(['1등 당첨자가 없었습니다'])
    else:
        ws.append(['1등 총 당첨금은',pot])

    wb.save("lotto/lotto4.xlsx")
    wb.close()

```
#
<br>

* 번호를 조회하면 request, beautifulsoup라이브러리를 활용하여 크롤링 한 raw data를 가공하여 openpyxl 라이브러리로 추출한 값을 엑셀시트에 저장한다. 

<br>
<br>

![](https://github.com/gitcat87/Lottery/blob/main/images/image4.png?raw=true)

#
```python
#program.py
    def doA(self):
        lotto4.lot2(self)
        lw = load_workbook("lotto/lotto4.xlsx")
        ws = lw.active

        self.turn.setText(str(ws["B1"].value))
        self.num1.setText(str(ws["A2"].value))
        self.num2.setText(str(ws["B2"].value))
        self.num3.setText(str(ws["C2"].value))
        self.num4.setText(str(ws["D2"].value))
        self.num5.setText(str(ws["E2"].value))
        self.num6.setText(str(ws["F2"].value))
        self.bns1.setText(str(ws["H2"].value))
        self.potmoney.setText(str(ws["B3"].value))

```
#

* 저장 했던 엑셀시트의 값을 textbox에 출력한다. 지난 회차 조회도 같은 방식으로 동작한다.
