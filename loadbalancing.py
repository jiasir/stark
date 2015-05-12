"""
The MIT License (MIT)

Copyright (c) 2015 Taio Jia (jiasir) <jiasir@icloud.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import subprocess
import ConfigParser
import logging

configFile = ConfigParser.RawConfigParser(allow_no_value=False)
configFile.read('stark.conf')

logger = logging.getLogger('stark-loadbalancing')
logging.basicConfig(filename=configFile.get('LOGGING', 'path'), level=configFile.get('LOGGING', 'level'),
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

nic = configFile.get('LOADBALANCING', 'nic')
ip = configFile.get('LOADBALANCING', 'ip')

hosts = configFile.get('TUNNEL', 'hosts')
ports = configFile.get('TUNNEL', 'ports')
hosts = str(hosts).split(',')
portsRange = str(ports).split(',')
every = len(hosts)
actPorts = range(int(portsRange[0]), int(portsRange[0]) + len(hosts))
packet = 0


def start_balancing(nic, ip, port, every, packet):
    commands = 'iptables -t nat -A PREROUTING -p tcp -i {0} --dport 7000 -j DNAT --to-destination {1}:{2} -m statistic --mode nth --every {3} --packet {4}'.format(nic, ip, port, every, packet)
    cmd = subprocess.Popen(args=commands, shell=True)
    cmd.wait()
    logger.info('Add [{port}] to Load Balancing using every: [{every} packet:[{packet}]]')


for port in actPorts:
    if packet <= every:
        start_balancing(nic, ip, port, every, packet)
        packet += 1
