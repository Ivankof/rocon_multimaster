#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2012, Yujin Robot, Jihoon Lee
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#    * Redistributions of source code must retain the above copyright
#        notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above
#        copyright notice, this list of conditions and the following
#        disclaimer in the documentation and/or other materials provided
#        with the distribution.
#    * Neither the name of Yujin Robot nor the names of its
#        contributors may be used to endorse or promote products derived
#        from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import roslib; roslib.load_manifest('rocon_gateway_tests')
import rospy
from rocon_gateway_helper import *
from gateway_comms.msg import *
from gateway_comms.srv import *
import argparse

"""
    add_public_topic.py 
    
    It publicize local topic to the centralised multimaster server

    Usage     :
        rosrun rocon_gateway_tests add_public_topic.py -m <topic_name,topictype,node_uri> ...
    Example :
        rosrun rocon_gateway_tests add_public_topic.py -m /chatter,std_msgs/String,<nodeuri> ...

        Lookup    local topic : 
            rostopic list
"""
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Process gateway request.')
    parser.add_argument('-m','--message',metavar='<Topic triple>',type=str,nargs='+',help='<Topic triple>="<topic name>,<topic type>,<node uri>"')
    args = parser.parse_args()

    rospy.init_node('add_public_topic')

    s = rospy.ServiceProxy('/gateway/request',PublicHandler)
    
    # all arguements are topic names
    l = args.message
    print "Topics " + str(l)

    # Form a request message
    req = PublicHandlerRequest() 
    req.command = "add_public_topic"
    req.list = l

    # Receive whether it is successful
    resp = s(req)

    print resp
