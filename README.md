To make it work completely, disable ipv6 in your router then do nano /etc/tor/torrc Remove the # in front of ControlPort9050 or 9051 Then systemctl restart tor then configure the socks proxy server in your web browser 127.0.0.1:9050

![d7f7c7f4-b36a-4689-9b77-a57b3d035504(1)](https://github.com/user-attachments/assets/d39467e5-1180-4169-a9b2-36b6e6c4559f)
