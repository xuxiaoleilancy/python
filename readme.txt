1.下载 服务zip（svn&scp等）

2.解压 
unzip baidu_aip.zip

3. 修改脚本权限及文件格式

cd baidu_aip
chmod a+x baidu_aip_start.sh
vi baidu_aip_start.sh
:set ff=unix

4. 初始化运行环境
virtualenv env
. env/bin/activate

5. 安装依赖包（首次安装需要）
pip install Flask
pip install baidu_aip

6. 启动服务
./baidu_aip_start.sh