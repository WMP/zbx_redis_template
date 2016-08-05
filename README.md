#Zabbix trap-message mode script for Reddis

In trap-message mode, script will be periodically accumulate redis's parameters and will send it to zabbix as a one message.

### Install
`pip install redis`

### Run
Run script in background with -i <interval> key:

zbx_redis_stats.py -i 10 &

3. Import `zbx_redis_trapper_template.xml` into zabbix in Tepmplate section web gui.

