import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import pandas as pd
import numpy as np 
import datetime


#열차별 운행시각표

#■ 요청 URL
#http://openapi.kric.go.kr/openapi/trainUseInfo/subwayTimetable?요청변수=값

#서울역 평일 운행시각표 [ dayCd(요일코드) : 7(토요일), 8(평일), 9(휴일) ]
#http://openapi.kric.go.kr/openapi/trainUseInfo/subwayTimetable?serviceKey=[서비스키값]&format=xml&railOprIsttCd=S1&dayCd=8&lnCd=1&stinCd=133

def gettable(time,day,loca,upd) :
    # time = "hh:mm:ss"
    # day = 요일 int
    #출력 : [ [ 열번, 행선지, 도착시간,출발시간] , [] ]


    output = [["K1111","일산","11:11","11:12"],["K1113","문산","11:15","11:19"]]
    return output


def gettable_xl(time,day,loca,stnname,upd) :
    # time = "hh:mm:ss"
    # day = 요일 int
    #출력 : [ [ 열번, 행선지, 도착시간,출발시간] , [] ]
    diagr = pd.read_excel('Dia.xlsx')
    diagr=diagr.drop([diagr.columns[0]],axis=1)
    #역의 y축 좌표
    stndialoc = diagr.index[diagr['시발역']==stnname][0]
    stndialoc_start = stndialoc+1
    #열번 차출
    number = []
    for i in diagr.loc[1] :
      number.append(i)
    #시간 처리
    timelist = time.split(":")
    timed = datetime.time(int(timelist[0]),int(timelist[1]),int(timelist[2]))
    timez = datetime.timedelta(hours=int(timelist[0]),minutes =int(timelist[1]),seconds=int(timelist[2]))

    #결선 처리
    for i in range(len(diagr.loc[diagr['시발역']==stnname].transpose())) :
      arrtime = diagr.iloc[stndialoc,i]
      steptime = diagr.iloc[stndialoc_start,i]
      if (arrtime=='        ') and (steptime =='        ') :
        diagr.iloc[[stndialoc],[i]] = "당역 미정차"
        diagr.iloc[[stndialoc+1],[i]] = "당역 미정차"
      elif arrtime!= '        ' and steptime == '        ' :
        diagr.iloc[[stndialoc],[i]] = "당역 출발"
      elif arrtime== '        ' and steptime != '        ' :
        diagr.iloc[[stndialoc_start],[i]] = "당역 종착"
    #목표 리스트 가공
    output =[]
    output2 = []
    for k in range(len(diagr[diagr['시발역']==stnname].transpose())):
      output.append([number[k], diagr.iloc[0,k], diagr.iloc[stndialoc,k],diagr.iloc[stndialoc+1,k]])
    for t in output :
        
        if t[0] == "열차번호" or t[3] =='        'or t[2] =='        ' :
            pass
        else :  

            if (type(t[2]) is not datetime.time) or (type(t[3]) is not datetime.time) :
                if (t[2] != "당역 미정차") or (t[2] != "당역 출발") or (t[3] != "당역 미정차") or (t[3] != "당역 종착") :
                    output2.append(t)
                else : pass
            elif (t[2].hour*3600+t[2].minute*60+t[2].second-timed.hour*3600-timed.minute*60-timed.second)>0 :
                output2.append(t)
            else : pass
            
    return output2
