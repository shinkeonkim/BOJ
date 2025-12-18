# [34466: Positioning Peter’s Paintings](https://www.acmicpc.net/problem/34466)
# Tier: Bronze 3
# Category: math, implementation, geometry, arithmetic

# frozen_string_literal: true

a,b,x,y=gets.split.map(&:to_i)
p (a+b+x+y-[[a,x].min,[b,y].min].max)*2
