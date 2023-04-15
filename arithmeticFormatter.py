#!/usr/bin/python3

import re

def arithmetic_arranger(problems, solve = False):
  if len(problems) > 5:
    return "Error: Too many problems."
  object = []

  for item in problems:
    itemSplit = item.split()
    top, sign, down = itemSplit
    try:
      t = int(itemSplit[0])
      t = int(itemSplit[2])
    except:
      return "Error: Number must only contain digits."
    if not re.search(r'[+-]', sign):
      return "Error: Operator must be '+' or '-'."
    if len(top) > 4 or len(down) > 4:
      return "Error: Numbers cannot be more than four digits."
    object.append({
      "top": top,
      "sign": sign,
      "down": down
    })

  top = [] 
  mid = [] 
  bot = []
  opres = []
  res = []
  for op in object:
    bigSpace = "    "  
    maxN = max([len(op["top"]), len(op["down"])])
    maxL = maxN + 2 # max operation length accounts for sign + space + N.len - this is the amount of space required before top N
    topLen = len(op["top"])
    botLen = len(op["down"])
    topSpace = " " * (maxL - topLen)
    botSpace = " " * (maxL - (1 + botLen))
    #top string is made of = (space * (maxL + 1 - topN.len)) + topN + space * 4 etc...
    #bottom string is made of = sign + space * (maxL - (sign + bottomN.len)) + bottomN etc...
    #bb string is made of = - * maxL + 4 spaces etc...
    top.append(topSpace + op["top"] + bigSpace)
    mid.append(op["sign"] + botSpace + op["down"] + bigSpace)
    bot.append("-" * maxL + bigSpace)
    if solve:
      r = 0
      if op["sign"] == "+":
        r = int(op["top"]) + int(op["down"])
      else:
        r = int(op["top"]) - int(op["down"])
      solveSpace = " " * (maxL - len(str(r)))
      opres.append(solveSpace + str(r) + bigSpace)

  res = "".join(top) + "\n" +  "".join(mid) + "\n" + "".join(bot)
  if solve:
    res = "".join(top) + "\n" +  "".join(mid) + "\n" + "".join(bot) + "\n" + "".join(opres)
  return res

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))


# Situations that will return an error:
#     If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
#     The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
#     Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
#     Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
# If the user supplied the correct format of problems, the conversion you return will follow these rules:
#     There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
#     Numbers should be right-aligned.
#     There should be four spaces between each problem.
#     There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
