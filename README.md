#Zabbix trap-message mode script for Reddis

In trap-message mode, script will be periodically accumulate redis's parameters and will send it to zabbix as a one message.

### Install
1. Install requirements
pip install redis

2. Run script in background with -i <interval> key:

./zbx_redis_stats.py -i 1- &

3. Import `zbx_redis_trapper_template.xml` into zabbix in Tepmplate section web gui.

