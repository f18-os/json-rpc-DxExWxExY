#!/usr/bin/env python3
# minimalistic server example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket, ast
from node import *
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)


# Class providing functions for the client to use:
@service_class
class ServerServices(object):

  @request
  def swapper(self, txt):
    return ''.join(reversed(list(txt)))

  @request
  def nop(self, txt):
    print(txt)
    obj = inc(txt)
    return obj.jsone()

def inc(data):
  graph = jsond(data)
  graph.val += 1;
  for c in graph.children:
      inc(c)
  graph.show()
  return graph

def jsond(data):
  obj = ast.literal_eval(data)
  print(obj)
  # return node("Root")
  children = []
  for child in obj['children']:
      children.append(jsond(child))
  return node(obj['name'], children, obj['val'])

# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
  s, _ = ss.accept()
  # JSONRpc object spawns internal thread to serve the connection.
  JSONRpc(s, ServerServices(),framing_cls=JSONFramingNone)
