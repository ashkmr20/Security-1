#!/usr/bin/python
# -*- coding: utf-8 -*-
goodstr = "I come in peace."
evilstr = "Prepare to be destroyed!"
blob = """
         Af�R0��[|3[����o?��-e6><blz+�����捧��N�m?_�3u(F�MwJ�ã�y(d��Yu�Jp$�2��g�f�ݑ(ɳ��`H��u����w[4hWwI����muJ�{�~ �
"""
goodhex = """
\00\00\00\00\00\00\00\00\00x\9E\C7s\CC\CBɷ)JY\86\FFS\CA4ѳ^\D0kw\A4^j|A\8A\9A\B9\FC9\E9\FF\EBn\88=\E7\EB[f\9C\F8G\82\86s/J&0߅ڇ\8A\88\8B\BC\FDZ\89$\87'\AD\E3\FD\8BĊ\E5	\BB\BE\876s\E9\F4 \DD\D7\C5XY.K^o\9C^tq\A9\AD\EF\94d&ø"\9C\A6\B3\FAu\00/ƕ\EE\B6J
"""
from hashlib import sha256
if( sha256(blob).hexdigest() == "adb93f89ab337c3a95b9cf5bb19a5cfe8285c0577d3f0cbd29a61a75ddf16930"):
	print goodstr
else:
	print evilstr
