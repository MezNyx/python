#!/usr/bin/env python
import sys

ip_sections = sys.argv[1].split(".")
print("{}.{}.{}.{}".format(ip_sections[3], ip_sections[2], ip_sections[1], ip_sections[0]))
