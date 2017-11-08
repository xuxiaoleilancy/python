1.下载 服务zip（svn&scp等）

2.解压 
unzip baidu_aip.zip

3. 修改脚本权限及文件格式
cd baidu_aip
chmod a+x baidu_aip_start.sh
vi baidu_aip_start.sh
:set ff=unix
:wq

4. 启动服务
./baidu_aip_start.sh
