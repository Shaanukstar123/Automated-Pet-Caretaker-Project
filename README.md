# Objectives

## Week 1:
- Basic Website Layout
- Working Backend
- 3D model printed 

## Useful Commands for firewall port exceptions on Pi
- sudo apt install iptables
- sudo iptables -I INPUT -p tcp -m tcp --dport 8883 -j ACCEPT
- sudo ufw allow 8884

## Domains
- MQTT: http://petsitter.ddnsgeek.com/ :35.177.203.22

##Streaming commands

raspivid -t 0 -vf -hf -fps 30 -b 6000000 -o - | ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/[your-secret-key-here]

with key: raspivid -t 0 -vf -hf -fps 30 -b 6000000 -o - | ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/0wda-qyx9-pdjj-gy1h-bj8v

youtube key: 0wda-qyx9-pdjj-gy1h-bj8v
