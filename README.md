Anonymize Yourself with Tor

Updated 2025

To make it work completely, disable ipv6 in your router then do nano /etc/tor/torrc Remove the # in front of ControlPort9050 or 9051 Then systemctl restart tor then configure the socks proxy server in your web browser 127.0.0.1:9050