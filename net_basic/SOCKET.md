SOCKET编程
===============
通过Socket抽象可以控制传输层协议TCP和UDP,深圳包括部分网络层协议，例如IP和ICMP。  
Socket使用IP地址+端口+协议的三元组标识一个通信链路。  
用Socket进行网络开发需了解服务器和客户端的Socket元语，每个原语在不同的高级语言种都有相应的实现方式。  

客户端 | 服务端 |
建立Socket对象：socket() | 建立Socket对象：socket()|
连接服务器：connect()|绑定端口：bind(port)|
收发数据：send(),recv()|监听:listen()|
关闭连接：close()|等待客户端连接：accept()|
 |收发数据：recv(),send()|
  | 关闭连接：close()|  

各个函数详细解释
-------------------
socket():建立Socket对象。Socket是以类似于文件系统的模式设计的(*打开*，*读写*，*关闭*)，socket原语相当于打开。其参数通常包括使用的传输层协议类型，网络层地址类型。  
bind():绑定。在参数种需要传入要绑定的IP地址和端口。IP地址必须是主机上一个可用的地址。
listen():监听。只在服务端有用，告诉操作系统开始监听之前绑定的IP地址和端口，可以在参数中指定允许排队的最大连接数量。 
connect():在客户端连接服务器。参数中需要指定服务器的地址和端口。建立连接或者连接失败。  
accept():接收连接。只在服务端有用，从监听到的连接中取出一个，并将其包装成一个新的socket对象，可被用于和相应客户端进行通信。
send():发送数据。服务器和客户端均可调用send()向对方发送数据，返回值判断是否成功。
recv():接收数据。服务器和客户端均可调用recv()从对方接收数据。 
close():关闭连接。通信中的任何一方可以调用close()发起关闭连接请求，另一方收到后也调用close()关闭连接。
对应程序位于[服务器端](https://github.com/BigBigRadish/pyhton_high_efficiency_dev/tree/master/net_basic/tcp_server.py)，[客户端](https://github.com/BigBigRadish/pyhton_high_efficiency_dev/tree/master/net_basic/tcp_client.py)