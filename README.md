# wirelessSensors-Dr.Huang  
前期准备：  
树莓派3一个  
树莓派3电源一个  
网线  
键盘  
鼠标  
显示屏一个（要求有DVI接口或者HDMI接口） 
显示屏连接线（因为树莓派3的显示屏接口是HDMI，所以根据显示屏，使用双hdmi或者hdmi转dvi，注意不能用hdmi转vga）  
树莓派3 GPIO： 
![](file:///Users/lxxxxxx/Downloads/gpio.jpg) 
注意 GPIO 靠近外侧的是偶数，靠近内侧（近CPU的一侧）是奇数  
  
  
1.树莓派的安装和配置：  
http://www.cnblogs.com/rond/p/4970071.html 格式化sd卡和安装系统用的是这个教程  
http://bbs.eeworld.com.cn/thread-503614-1-1.html?_t=t 更进一步的配置，包括ssh等  
http://www.shumeipaiba.com/wanpai/jiaocheng/5.html 树莓派3安装中文输入法  
http://www.jianshu.com/p/8c474339a238 树莓派3 更改键盘设置  
在同一局域网下ssh访问树莓派：打开树莓派ssh服务和wifi服务后，ifconfig查看树莓派wlan的ip，例如树莓派hostname是pi@respberry:~$，ifconfig看到wlan是192.168.10.134，那么pc或者laptop上可以ssh pi@192.168.10.134 默认密码rsapberry 访问到树莓派了  
2.python GPIO控制树莓派 简单的demo  
http://blog.mangolovecarrot.net/2015/05/22/raspi-study07/  
3.单机使用flask建立一个web服务器  
http://www.cnblogs.com/ttssrs/p/4890635.html  
如何运行flask  
https://zhuanlan.zhihu.com/p/23339561  
可能会用的线程通信：flask-socketio：  
http://flask-socketio.readthedocs.io/en/latest/  
https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent  
flask socketio js引入  
https://cdnjs.com/libraries/socket.io  
python socket基础  
https://gist.github.com/kevinkindom/108ffd675cb9253f8f71  
在局域网中，client给定一个  
  
flask下使用redis，试试看树莓派通过socket传消息给socket server，然后socket server和flask一起共用一个redis，flask server和client通过socketio连接
http://www.ziyoubaba.com/archives/585  
redis基本操作：  
http://www.cnblogs.com/woshimrf/p/5198361.html  
  
（传感器GPIO引脚规定：  
声音：VCC：5v GND：gnd OUT：gpio 4  
超声波：VCC：5v GND：gnd Trigger：gpio23 Echo：gpio 24  
气体（MQ-2）： VCC:5V  GND：gnd  AOUT： DOUT：  
火焰： VCC：5v GND：gnd  OUT：2  
红外避障：VCC:5v  GND：gnd  OUT：  
震动传感器：VCC：3.3v GND：gnd  OUT：gpio 21 ）  
  
启动顺序：  
先启动sensorMonitor.py，之后启动flask，最后在相应的传感器开发板上启动对应的传感器脚本  
  
每个传感器针脚下方都有标注，可以根据标注来连接对应的线  
