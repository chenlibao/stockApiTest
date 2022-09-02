# pytest接口自动化测试
知识点：
业务分层、配置解析、conftest、fixture、数据驱动、数据库、日志、allure报告

本地直接运行：
`python run.py`

具体：
1、分层，将接口单独封装，这样单个用例可以多次调用接口
2、配置，config.ini作为配置文件，configUtil.py作为解析工具
3、日志，将日志模块单独封装
4、conftest.py，在测试用例目录下，添加该文件，运行用例前，会先加载该文件,作用：
（1）编写fixture，实现类似tearUp与tearDown，在用例中通过@pytest.mark.usefixtures("func_name")来调用
（2）导入日志，由于在测试用例中添加日志，无法产生日志记录器，可以在conftest.py先加载
（3）终端日志显示测试结果情况：pytest_terminal_summary，如下
{'passed': 0, 'failed': 2, 'error': 0, 'skipped': 0, 'xfailed': 0, 'xpassed': 0, 'rerun': 0, 'time': 0, 'total': 2, 'passrate': '0.0%'}
5、数据库，涉及到清库，查库，改库来适配测试的动作，封装sqlUtil.py
6、测试数据，这里没有采用excel或者yaml或者json等文件来管理测试数据，直接采用py文件，优点
（1）无需解析，方便
（2）部分测试数据，可以直接通过在py文件中通过编写函数来构造
7、使用@pytest.mark.parametrize，实现数据驱动测试
8、测试报告
（1）allure测试报告
（2）切换到allure所在目录，执行以下命令查看报告
`allure -serve ./reports/allure`
9、Jenkins流水线
（1）在Jenkins中安装allure插件
（2）编写Jenkins Job来运行脚本，只需在Job中，增加shell脚本即可，添加以下命令
`python -m pytest ./testCases --alluredir=./reports/allure`
