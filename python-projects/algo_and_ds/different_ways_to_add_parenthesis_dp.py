from itertools import product
import operator
from typing import List

# class Solution:
#     def diffWaysToCompute(self, expression: str) -> List[int]:
        
#         # def get_nums_and_exps(string):
#         #     nums = ['']
#         #     exps = []
#         #     echars = '+-*'
#         #     for ch in string:
#         #         if ch in echars:
#         #             exps.append(ch)
#         #             nums.append('')
#         #         else:
#         #             nums[-1] += ch
#         #     return nums, exps
        
#         # def get_exps(string, exps, start, end):
#         #     subexps = []
#         #     for exp in exps:
#         #         if start <= exp <= end:
#         #             subexps.append(exp)
#         #     return subexps
        
#         # def resolve(num1, num2, exp):
#         #     exps = {
#         #         '+': operator.add, '-': operator.sub, '*': operator.mul
#         #     }
#         #     return exps[exp](int(num1), int(num2))
        
#         # def build_expression_trees(string, exps, start, end):
#         #     subexps = get_exps(string, exps, start, end)
#         #     if len(subexps) == 1:
#         #         return resolve(, num2, exp)
#         #     values = []
#         #     for se in subexps:
#         #         for leftval, rightval in product(
#         #             build_expression_trees(string, exps, start, exp),
#         #             build_expression_trees(string, exps, exp, right),
#         #         ):
#         #             left_num = build_expression_trees(string, exps, start, left)
#         #             right_num = build_expression_trees(string, exps, right, end)
#         #             values.append(resolve(left_num, right_num, se))
#         #     return values
        
#         # def main(expression):
#         #     nums, exps = get_nums_and_exps(expression)
#         #     return build_expression_trees(nums, exps, 0, len(exps)-1)
        
#         return main(expression)


# def get_nums_and_exps(string):
#     nums = ['']
#     exps = []
#     echars = '+-*'
#     for ch in string:
#         if ch in echars:
#             exps.append(ch)
#             nums.append('')
#         else:
#             nums[-1] += ch
#     return nums, exps

# def get_exps(nums, exps, start, end):
#     subexps = []
#     for i, exp in enumerate(exps):
#         if start <= i <= end:
#             subexps.append(exp)
#     return subexps

# def resolve(num1, num2, exp):
#     print('num1, num2, exp', num1, num2, exp)
#     exps = {
#         '+': operator.add, '-': operator.sub, '*': operator.mul
#     }
#     return exps[exp](int(num1), int(num2))

# def build_expression_trees(nums, exps, start, end):
#     print(nums, exps, start, end)
#     subexps = get_exps(nums, exps, start, end)
#     print(subexps, nums, exps, start, end)
#     if len(subexps) == 0:
#         return [0]
#     if len(subexps) == 1:
#         return [resolve(nums[start], nums[end+1], subexps[0])]
#     else:
#         values = []
#         for i, se in enumerate(subexps):
#             leftvals = build_expression_trees(nums, exps, start, i-1)
#             rightvals = build_expression_trees(nums, exps, i+1, end)
#             print('leftvals, rightvals, i', leftvals, rightvals, i, subexps)
#             for leftval, rightval in product(
#                 build_expression_trees(nums, exps, start, i-1),
#                 build_expression_trees(nums, exps, i+1, end),
#             ):
#                 values.append(resolve(leftval, rightval, se))
#         return values

# def main(expression):
#     nums, exps = get_nums_and_exps(expression)
#     return build_expression_trees(nums, exps, 0, len(exps)-1)


# print('answer', main('2-1-1'))

# ================================================================================

# complete within 8

import operator
from itertools import product

exps = {
        '+': operator.add, '-': operator.sub, '*': operator.mul
    }

def get_operators(expression, start, end):
    for i in range(start, end+1):
        if expression[i] in exps:
            yield i

def resolve(num1, num2, exp):
    # print('num1, num2, exp', num1, num2, exp)
    return exps[exp](int(num1), int(num2))


def build_expression_trees(expression, start, end):
    notthere = True
    for iexp in get_operators(expression, start, end):
        notthere = False
        leftvals = build_expression_trees(expression, start, iexp-1)
        rightvals = build_expression_trees(expression, iexp+1, end)
        for left, right in product(leftvals, rightvals):
            yield resolve(left, right, expression[iexp])

    # base case when there is no exp
    if notthere is True:
        yield int(expression[start:end+1])


def main(expression):
    return list(build_expression_trees(expression, 0, len(expression)-1))

print('answer', main('2-1-1'))

expression = "2*3-4*5"
print('answer', main(expression))