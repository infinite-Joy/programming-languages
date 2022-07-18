"""
this can be done using tries

first create a trie tree using the supplies
and then go through the ingredients and see if they are present in the tree
return the recipes if they are there


"""

from collections import defaultdict, deque
from typing import List
from pprint import pprint

class Dag:
    def __init__(self):
        self.g = defaultdict(list)
        self.indegree = defaultdict(int)
        self.queue = deque()
        self.cycle = False
        self.origins = set()

    def build_graph(self, recipes, ingredients, supplies):
        for recipe, ingredient_list in zip(recipes, ingredients):
            for ing in ingredient_list:
                self.g[ing].append(recipe)
                self.indegree[recipe] += 1
        for ing in supplies:
            self.indegree[ing] = 0
        pprint(self.g)
        pprint(self.indegree)
        self.origins = set(supplies)

    def topological_sort(self, target):
        output = []
        for k in self.indegree.keys():
            if k in self.origins and self.indegree.get(k) == 0:
                self.queue.append(k)
        print(f'{self.queue=}, {self.indegree=}')
        count = 0
        while self.queue:
            node = self.queue.popleft()
            if node in self.origins:
                output.append(node)
            for neighbour in self.g[node]:
                self.indegree[neighbour] -= 1
                if self.indegree[neighbour] == 0:
                    self.queue.append(neighbour)
            count += 1
        if count >= len(self.g): # cycle has been detected
            self.cycle = False
        else:
            self.cycle = True
        return output
        

class Solution:
    def findAllRecipes(
            self, recipes: List[str],
            ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        g = Dag()
        g.build_graph(recipes, ingredients)

def main(recipes, ingredients, supplies):
    g = Dag()
    g.build_graph(recipes, ingredients, supplies)
    return g.topological_sort()
        


# recipes = ["bread"]
# ingredients = [["yeast","flour"]]
# supplies = ["yeast","flour","corn"]
# print(f'{recipes=}, {ingredients=}, {supplies=}')
# print(main(recipes, ingredients, supplies))

recipes = ["bread","sandwich"]
ingredients = [["yeast","flour"],["bread","meat"]]
supplies = ["yeast","flour","meat"]
print(f'{recipes=}, {ingredients=}, {supplies=}')
print(main(recipes, ingredients, supplies))

# recipes = ["bread","sandwich","burger"]
# ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
# supplies = ["yeast","flour","meat"]
# print(f'{recipes=}, {ingredients=}, {supplies=}')
# print(main(recipes, ingredients, supplies))