#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
s = input()
#= map(int, input().split())
#= list(map(int, input().split()))
#= [input(), input()]
#= [list(map(int, input().split())) for _ in range(N)]
#= [int(input()) for _ in range(N)]
#= {i:[] for i in range(N)}

if s[-1] == "s":
    print(s + "es")
else:
    print(s + "s")