1.���� ����zip��svn&scp�ȣ�

2.��ѹ 
unzip baidu_aip.zip

3. �޸Ľű�Ȩ�޼��ļ���ʽ

cd baidu_aip
chmod a+x baidu_aip_start.sh
vi baidu_aip_start.sh
:set ff=unix

4. ��ʼ�����л���
virtualenv env
. env/bin/activate

5. ��װ���������״ΰ�װ��Ҫ��
pip install Flask
pip install baidu_aip

6. ��������
./baidu_aip_start.sh