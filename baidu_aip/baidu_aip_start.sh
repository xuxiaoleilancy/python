#!/bin/bash
sr_baidu_aip_app=$(ps aux | grep "python app.py" | grep -v grep | awk '{print $2}')
kill -9 $sr_baidu_aip_app
. venv/bin/activate
python app.py &
