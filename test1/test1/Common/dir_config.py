#用变量替换相应的路径
import os

#返回当前文件的路径
cur_dir = os.path.split(os.path.abspath(__file__))[0]
#获取testdata文件的路径
testdata_dir = cur_dir.replace("Common","TestDatas")
#获取HtmlRepost文件的路径
htmlreport_dir = cur_dir.replace("Common","HtmlTestReport")
#获取Logs文件的路径
logs_dir = cur_dir.replace("Common","Logs")