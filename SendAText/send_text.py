#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:50:27 2018

@author: jacobpelletier
"""
"""
I. developers often use the pip package manager to dl and install packages. 
    A. ~$ install twiloo
    B. with 'pip install twilio'
"""    

from twilio.rest import Client

account_sid = 'AC2d89ed89c9aeb97b55522c47cdaa6e4c'
auth_token = '977f235a367a9086208bb6a7f056d44c'

client = Client(account_sid, auth_token)

message = client.messages.create(
                            body='Don\'t worry about it tho',
                            from_='+18602373212',
                            to='+18609779964',
                        )

print(message.sid)

"""
# whats going on with this code?

II. from twilio.rest import TwilioRestClient
    A. what is from?:
        1. import X
            a. imports the module x, creates a reference to that module in namespace
            b. then you need to define completed module path to access a particular 
                attr or method. eg(X.name, X.attribute)
        2. from X import *
            a. imports module x
            b. but this time you use an unqualified name to refer to things in module x
"""            
            