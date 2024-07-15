import unittest
import os
import HTMLTestRunner
import time

# 1.指定测试用例所在的目录
case_path = os.path.join(os.getcwd(), './')

# 2.指定测试报告存放的位置
report_path = os.path.join(os.getcwd(), 'test_one')


# 3.通过discover加载测试用例
def get_all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py')
    return discover


if __name__ == '__main__':
    # 4.html测试报告文件的路径
    report_abspath = os.path.join(report_path, 'result.html')

    # 5.执行测试用例，并生成测试报告
    fp = open(report_abspath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='我的自动化测试报告',
                                           description='V1.0')
    runner.run(get_all_case())
    fp.close()

