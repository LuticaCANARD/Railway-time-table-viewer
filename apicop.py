import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


#열차별 운행시각표

#■ 요청 URL
#http://openapi.kric.go.kr/openapi/trainUseInfo/subwayTimetable?요청변수=값

#서울역 평일 운행시각표 [ dayCd(요일코드) : 7(토요일), 8(평일), 9(휴일) ]
#http://openapi.kric.go.kr/openapi/trainUseInfo/subwayTimetable?serviceKey=[서비스키값]&format=xml&railOprIsttCd=S1&dayCd=8&lnCd=1&stinCd=133

def gettable(time,day,loca) :
    # time = "hh:mm:ss"
    # day = 요일 int
    #출력 : [ [ 열번, 행선지, 도착시간,출발시간] , [] ]

    output = [["K1111","일산","11:11","11:12"],["K1113","문산","11:15","11:19"]]
    return output
