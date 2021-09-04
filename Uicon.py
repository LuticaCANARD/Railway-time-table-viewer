from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5 import uic
import time
import sys
import apicop

form = uic.loadUiType("uiofpy.ui")[0]
class windowCl (QMainWindow, form) :
    def __init__ (self) :
        super().__init__()
        self.setupUi(self)

        #
        self.find_start.clicked.connect(self.finding)


    def finding (self) : 
        linename = self.Line_nam.text()
        linename = self.Line_nam.text()
        stacode = self.sta_code.value()
        timing_eta_Qt = self.sta_eta_time.time()
        timing_eta_str = timing_eta_Qt.toString("hh:mm:ss")
        days_int = self.day_input.value()
        stnnam = self.Sta_name.text()
        print(timing_eta_str)
        #days
        nomaldays=1
        satd = 2
        vac = 3
        #-
        day_di = {0: nomaldays,
                  1: satd,
                  2: vac}

        daycode = day_di.get(days_int)
        #��� : [ [����, �༱��, �����ð�,��߽ð�] , [] ]
        table = apicop.gettable_xl(timing_eta_str,daycode,stacode,stnnam,'u')
        print(table)
        self.sta_timetable2.setRowCount(len(table))
        self.sta_timetable2.setColumnCount(4)
        self.sta_timetable2.setHorizontalHeaderLabels(['열번', '행선지', '도착시간','출발시간'])
        for i,u in zip(table,range(len(table))) :
            self.sta_timetable2.setItem(u,0,QTableWidgetItem(i[0]))
            self.sta_timetable2.setItem(u,1,QTableWidgetItem(i[1]))
            self.sta_timetable2.setItem(u,2,QTableWidgetItem(str(i[2])))
            self.sta_timetable2.setItem(u,3,QTableWidgetItem(str(i[3])))


if __name__=="__main__" :
    app = app = QApplication(sys.argv)
    myApp = windowCl()
    myApp.show()
    app.exec_()





        





