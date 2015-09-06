pi-rover
========

Streaming from pi:
from receiving pc:
```
nc -l 2222 | mplayer -fps 200 -demuxer h264es -
```
from RPI:
```
/opt/vc/bin/raspivid -t 0 -w 1280 -h 720 -fps 5 -ex night -o - | nc PC_IP 2222
```
Or try rtspserver https://github.com/mpromonet/h264_v4l2_rtspserver
