#!/bin/bash
sr_baidu_aip_app=$(ps aux | grep "python sr_baidu_aip_app.cpython-35.pyc" | grep -v grep | awk '{print $2}')
kill -9 $sr_baidu_aip_app
python sr_baidu_aip_app.cpython-35.pyc &
