# pytest�ӿ��Զ�������
֪ʶ�㣺
ҵ��ֲ㡢���ý�����conftest��fixture���������������ݿ⡢��־��allure����

����ֱ�����У�
`python run.py`

���壺
1���ֲ㣬���ӿڵ�����װ�����������������Զ�ε��ýӿ�
2�����ã�config.ini��Ϊ�����ļ���configUtil.py��Ϊ��������
3����־������־ģ�鵥����װ
4��conftest.py���ڲ�������Ŀ¼�£���Ӹ��ļ�����������ǰ�����ȼ��ظ��ļ�,���ã�
��1����дfixture��ʵ������tearUp��tearDown����������ͨ��@pytest.mark.usefixtures("func_name")������
��2��������־�������ڲ��������������־���޷�������־��¼����������conftest.py�ȼ���
��3���ն���־��ʾ���Խ�������pytest_terminal_summary������
{'passed': 0, 'failed': 2, 'error': 0, 'skipped': 0, 'xfailed': 0, 'xpassed': 0, 'rerun': 0, 'time': 0, 'total': 2, 'passrate': '0.0%'}
5�����ݿ⣬�漰����⣬��⣬�Ŀ���������ԵĶ�������װsqlUtil.py
6���������ݣ�����û�в���excel����yaml����json���ļ�������������ݣ�ֱ�Ӳ���py�ļ����ŵ�
��1���������������
��2�����ֲ������ݣ�����ֱ��ͨ����py�ļ���ͨ����д����������
7��ʹ��@pytest.mark.parametrize��ʵ��������������
8�����Ա���
��1��allure���Ա���
��2���л���allure����Ŀ¼��ִ����������鿴����
`allure -serve ./reports/allure`
9��Jenkins��ˮ��
��1����Jenkins�а�װallure���
��2����дJenkins Job�����нű���ֻ����Job�У�����shell�ű����ɣ������������
`python -m pytest ./testCases --alluredir=./reports/allure`
