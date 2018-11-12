#!/usr/bin/env python3

import socket
from node import *
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)

# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))
rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()

# Create object 
leaf1 = node("leaf1")
leaf2 = node("leaf2")
root = node("root", [leaf1, leaf1, leaf2])
print("Before request...")
print(root.jsone())
# do this increment remotely:
print("After request...")
print(server.nop(root.jsone()))
s.close()