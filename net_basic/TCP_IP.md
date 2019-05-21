TCP/IP网络
==============
TCP/IP：传输控制协议/互联网网络协议。TCP/IP是一种网络通信协议，它规范了网络上德所有通信设备，尤其是一个主机与另一个主机之间的数据
往来格式。  
TCP/IP是internet的基础协议，也是各种计算机数据打包和寻址的标准方法。 

计算机网络综述
------------------------------
计算机网络是指地理位置不同的，具有独立功能的多台计算机及其外部设备，通过通信线路连接起来，在网络操作系统，网络管理软件及互联网通信协议的管理和协调下，  
实现资源共享和信息传递的计算机系统。  
Internet成为世界上最大的计算机网络。  
Internet主要由主机，线路，交换，路由，调制解频器等设备组成。网络应用开发者无需具体了解Internet的架构及物理细节，可以把internet看作主机和传输设备组成。  
主机有不同的形式，主要分为两种：服务器和客户端。  

**网络分层** 
-----------------
将数据从一个主机传输到另一个主机是一个复杂的过程，包括信息*格式转换*，*分发*，*寻址*，*物理传输*等 ，在这个过程中需要加入多种**校验措施**以保证传输的正确性。  
为了使这个过程利于设计而且向开发者隐匿网络细节，计算机网路被纵向分割为不同的层，每一层表示不同的抽象程度和设计目的。
TCP/IP将网络分为四层结构，分别为应用层，传输层，网络层，接口层。  

TCP/IP层次 |
-----------|
应用层  
HTTP,SMTP等，网络应用开发|
传输层
TCP或UDP |
网络层，IP|
接口层，处理物理细节|

从上到下解释：  
应用层：，为用户的进程直接提供服务，应用层负责发送及接收什么数据，如何解释数据，如何呈现数据，如何加密数据。  
传输层：，为两个主机的不同端口之间的通信提供服务。端口是一种在不同主机内的不同通道之间进行寻址的方式。TCP提供可靠的有序传输，UDP提供非可靠的传输。  
网络层：，为两个主机之间提供通信服务。网络层定义了数据如何被封装为传送包，并且定义了不同主机之间的寻址方式。主要由IP组成，辅以ICMP,IGMP等路由协议。  
接口层：，负责相邻物理设备之间的信息传输。接口层的工作非常多且复杂，它需要完成接口层的数据组装，加入必要的控制和校验数据，并且将二进制数据流转换为物理链路上的标准电平（高电平，低电平）。针对不同
的传输介质，接口层定义了多套标准，并且这些标准随着电子技术的进步一直发展。如802.3，802.11.  

**网络设备** 
-----------------
**集线器，交换机，网桥，路由器，网关，调试解频器，无线接入点，防火墙**  

**IP地址** 
-----------------
IPV4 AND IPV6

**域名** 
-----------------
IP地址的面具  

**URL** 
-----------------
统一资源定位符，用来表示Internet上资源位置的标准。资源位置包括资源所在的主机及其在主机内的访问路径。URL标准形式：[协议]：//[主机]:[端口]/[路径]？[参数]  
其中，[协议]可以是http，ftp等应用层协议：[主机]是域名或者Ip地址；[端口]是传输层端口号；[路径]是以斜杠“/”分割的主机内的路径；[参数]是以“&"分割的若干键值对。  

TCP 和 UDP
------------------------------
**传输层为主机提供端到端的服务**  

**端口** 
-----------------
进程通过系统调用与某端口建立连接（Binding绑定）之后，传输层传给该端口的数据都被相应的进程所接收，相应的进程发给传输层的数据都从该端口输出。  
TCP和UDP可以在同一主机上使用相同的端口而互不干扰。  
**TCP** 
-----------------
TCP是一种面向连接的，可靠的，基于*字节流*的传输层通信协议。  
当应用层向TCP层发送用于网间传输的用8位字节表示的数据流时，TCP则把数据流分割成适当长度的报文段，最大传输段大小(MSS)通常受该计算机连接的网络的数据链路层的最大传输单元限制。  
之后TCP把数据包传给IP层，由它通过网络将包传送给接收端实体的TCP层。  
TCP层特性：  
有序性：为每个数据包编排序号，方便接收端判断先后到达的次序是否混乱。  
正确性：计算校验和（checksum）  
可靠性：超时重传，重发  
可控性：接收端和发送端的网络质量通常不同，TCP采用滑动窗口协议和拥塞控制算法使数据的发送速度达到合理。  
TCP采用面向连接的方式收发数据，在收发数据之前需要先建立连接。  
三次握手机制：  
建立连接时：客户端发送SYN包到服务器，并进入SYN_SENT状态，等待服务器确认。  
服务器收到SYN包：反馈给客户端一个SYN+ACK包，此时服务器进入SYN_RECV状态。
客户端收到服务器的SYN+ACK包：向服务器发送确认包ACK，客户端和服务器同时进入ESTABLISHED(TCP连接成功)状态。完成三次握手。  
建立连接后，双方可互相发送消息，消息完成后可由任意一方发起关闭连接请求。  
四次消息关闭机制：  
关闭请求方(比如客户端)向另一方发送(比如服务器)一个带有FIN附加标记的报文段。  
服务器收到这个FIN报文段之后，并不立即用FIN报文段回复主机A，而是先向主机A发送一个确认序号ACK，同时通知自己的相应的应用程序：对方要求关闭连接，使用程序作相应的清理工作。  
服务器的应用程序清理工作完成后，向客户端发送一个FIN报文段。  
客户端收到这个FIN报文段后，向服务器发送一个ACK，表示连接彻底释放。

**UDP** 
-----------------
是一种无连接的传输层协议，提供面向事务的简单的不可靠的消息传送服务。UDP的标题很短，只有8个字节，相对于TCP的额外开销很小，因此UDP能够提供更快速，轻量级的传输层控制协议。  
UDP协议特性：  
数据可以随时发送，接收，没有建立，断开连接的过程，因此主机不需要维护复杂的连接状态。 
UDP不保证数据的可靠传输，仅仅尽最大可能进行发送。  
没有拥塞控制算法控制收发速率，程序需在应用层自行控制。  
发送方的UDP对应用程序交付的报文，再添加首部就向下交付给IP层。既不拆分，也不合并。  
**UDP适用场景**：吞吐量大，可以承受信息损失。