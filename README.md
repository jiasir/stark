# Stark
Stark is a transparent pass through GFW proxy server

### Getting started
Using Stark server(tunnel backend current only) to build a proxy server

* First edit your stark.conf file
* Start your tunnel backend

        python tunnel.py

* Build load balancing
        
        sudo python loadbalancing.py
        
* Enable `ip_forward`

        sudo sysctl -w net.ipv4.ip_forward=1
        
        