"""
this can be done using tries

first create a trie tree using the supplies
and then go through the ingredients and see if they are present in the tree
return the recipes if they are there


"""
from typing import List


class TrieNode:
    def __init__(self, ch):
        self.ch = ch
        self.children = {}


class Solution:
    def findAllRecipes(
            self, recipes: List[str],
            ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        def build_tree(supplies):
            root = TrieNode('*')
            for ing in supplies:
                node = root
                for ch in ing:
                    if ch in node.children:
                        node_ = node.children[ch]
                    else:
                        node_ = TrieNode(ch)
                        node.children[ch] = node_
                    node = node_
            return root   
        
        def present(ing, tree):
            for ch in ing:
                if ch in tree.children:
                    tree = tree.children[ch]
                else:
                    return False
            return True
        
        tree = build_tree(supplies)
        poss_recipes = []
        for recipe, ingredient_list in zip(recipes, ingredients):
            if all(present(ing, tree) for ing in ingredient_list):
                poss_recipes.append(recipe)
        return poss_recipes
                
        
def build_tree(supplies):
    root = TrieNode('*')
    for ing in supplies:
        node = root
        for ch in ing:
            if ch in node.children:
                node_ = node.children[ch]
            else:
                node_ = TrieNode(ch)
                node.children[ch] = node_
            node = node_
    return root   

def present(ing, tree, recipes_mapping, ingredients):
    if ing in recipes_mapping:
        if recipes_mapping[ing][1] is True or recipes_mapping[ing][1] is False:
            return recipes_mapping[ing][1]
        else:
            recipes_mapping[ing][1] = all(present(ing_, tree, recipes_mapping, ingredients) for ing_ in ingredients[recipes_mapping[ing][0]])
            return recipes_mapping[ing][1]
    for ch in ing:
        if ch in tree.children:
            tree = tree.children[ch]
        else:
            return False
    return True

def main(recipes, ingredients, supplies):
    # default output is done so that we are able to distinguish between the 
    # results and when the output has not been computed.
    default_output = None
    recipes_mapping = {r: [idx, default_output] for idx, r in enumerate(recipes)}
    tree = build_tree(supplies)
    poss_recipes = []
    for recipe, ingredient_list in zip(recipes, ingredients):
        if all(present(ing, tree, recipes_mapping, ingredients) for ing in ingredient_list):
            poss_recipes.append(recipe)

        print([(present(ing, tree, recipes_mapping, ingredients), ing) for ing in ingredient_list])
    return poss_recipes


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

recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]
print(f'{recipes=}, {ingredients=}, {supplies=}')
print(main(recipes, ingredients, supplies))