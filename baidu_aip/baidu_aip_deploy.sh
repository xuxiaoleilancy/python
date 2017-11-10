#!/bin/bash
rm baidu_aip_deploy.tar.gz
rm -rf baidu_aip_deploy
python -m compileall .
mkdir baidu_aip_deploy
cd baidu_aip_deploy
cp -avf ../*.pyc ./
cp ../baidu_aip_start.sh ./
mkdir baidu
cp -avf ../baidu/*.pyc ./baidu
mkdir rglobal
cp -avf ../rglobal/*.pyc ./rglobal
mkdir ./rglobal/files
mkdir ./rglobal/files/result_img
cp -avf ../rglobal/files/result_img/* ./rglobal/files/result_img

cd ..
tar -czvf baidu_aip_deploy.tar.gz baidu_aip_deploy
