import HTMLTestRunnerNew#测试报告生成的库模板
import unittest#单元测试框架
from TestCases import test_add#用例导入
from Common import dir_config
import time
from Common import myLogger2

s = unittest.TestSuite()#测试套件
ul = unittest.TestLoader()#加载testcase到testsuite中
s.addTests(ul.loadTestsFromModule(test_add))#将测试用例实例增加到测试套件
curTime = time.strftime("%Y-%m-%d %H%M",time.localtime())#设置测试报告的时间格式
fp = open(dir_config.htmlreport_dir + '/API_autoTest_{0}.html'.format(curTime), 'wb')#设置测试报告的文件名称格式
runner = HTMLTestRunnerNew.HTMLTestRunner(
            stream=fp,
            title='交易猫接口测试报告',
            description='交易猫接口测试报告',
            tester="yihong"
            )
runner.run(s)#执行测试用例