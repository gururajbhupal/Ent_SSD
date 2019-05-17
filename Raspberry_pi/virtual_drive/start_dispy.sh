#!/bin/bash

# start dispy on virtual drive

sleep 30

_IP=$(hostname -I)
/usr/local/bin/dispynode.py -i "$_IP" --daemon 

