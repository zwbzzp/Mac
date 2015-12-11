#!/usr/bin/env python
#coding=utf-8
# Created Time:    2015-01-23 16:23:02
# Modified Time:   2015-01-24 09:24:04
# Created By:      Vic <vic@libgod.com>

from optparse import OptionParser
import socket
import struct

def wake(addr, mac):
    mac_data = []
    for i in range(0, 12, 2):
        mac_data.append(int(mac[i:i+2], 16)) #16表示16进制
    # struct用于处理二进制，pack(fmt,v1,v2),按照给定的格式把数据封装成字符串，！代表对齐方式按照大端规则，B表示integer
    packet = struct.pack("!BBBBBB", 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF);
    packet_mac = struct.pack("!BBBBBB", *mac_data)
    for i in range(0, 16):
        packet += packet_mac
    #print "len: ", len(packet), "data: ", packet
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    try:
        s.sendto(packet, addr)
        print "唤醒数据包发送完成", addr, mac
    finally:
        s.close()

def main():
    usage = "%prog [options]"
    parser = OptionParser(usage = usage)
    parser.add_option("-a", "--addr", dest="addr", help="Boardcast address", metavar="255.255.255.255")
    parser.add_option("-p", "--port", dest="port", help="Port", metavar="7")
    parser.add_option("-m", "--mac", dest="mac", help="MAC address", metavar="FF-FF-FF-FF-FF-FF")
    (options, args) = parser.parse_args()
    if not options.mac:
        parser.print_help()
        return
    addr = "255.255.255.255"
    port = 7
    mac = options.mac.replace("-", "")
    if options.addr:
        addr = options.addr
    if len(mac) != 12:
        print "无效的MAC地址: %s" % options.mac
        return
    if options.port:
        port = int(options.port)
    wake((addr, port), mac)

if __name__ == "__main__":
    main()
