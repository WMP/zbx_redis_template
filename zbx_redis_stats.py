#!/usr/bin/env python

import redis, time, socket, argparse, os

zabbix_conf = "/etc/zabbix/zabbix_agentd.conf"  # (optional) Zabbix configuration file
redis_ip = '127.0.0.1'
redis_port = 6379

parser = argparse.ArgumentParser(description='Zabbix Redis status script')
parser.add_argument('-a','--auth',dest='redis_pass',action='store',help='Redis server pass',default=None)
parser.add_argument('-i', '--interval', required=True, type=int, help='Refresh interval in secs.')
args = parser.parse_args()

def main():
    while args.interval:
        client = redis.StrictRedis(host=redis_ip, port=redis_port, password=args.redis_pass)
        server_info = client.info()
        stats = []
        for i in server_info:
            stats.append("- redis[{0}] {1}".format(i, server_info[i]))
        llensum = 0
        for key in client.scan_iter('*'):
            if client.type(key) == 'list':
                llensum += client.llen(key)
        stats.append("- redis[llenall] {}".format(llensum))
        # Send stats to zabbix
        hostname = socket.gethostname()
        stdin,stdout = os.popen2("zabbix_sender -s {0} -c {1} -i -".format(hostname, zabbix_conf))
        stdin.write('\n'.join(stats))
        stdin.close()
        stdout.close()
        time.sleep(args.interval)

if __name__ == '__main__':
    main()
