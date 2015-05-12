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

logger = logging.getLogger('stark-tunnel')
logging.basicConfig(filename=configFile.get('LOGGING', 'path'), level=configFile.get('LOGGING', 'level'),
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

hosts = configFile.get('TUNNEL', 'hosts')
ports = configFile.get('TUNNEL', 'ports')

portsRange = str(ports).split(',')


def startTunnel(host, port):
    commands = ['ssh', '-qTfnN', '-D', port, host]
    subprocess.call(commands)
    logger.info('Create tunnel [{0}] on local port [{1}]'.format(host, port))


hosts = str(hosts).split(',')
ports = range(int(portsRange[0]), int(portsRange[1]) + 1)
portsIndex = 0
for h in hosts:
    host = str(h).strip()
    port = str(ports[portsIndex]).strip()

    startTunnel(host, port)
    portsIndex += 1









