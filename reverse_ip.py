#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('ip', help='ip to be reversed')
args = parser.parse_args()
ipd = args.ip.split('.')
print("%s.%s.%s.%s" % (ipd[3], ipd[2], ipd[1], ipd[0]))
