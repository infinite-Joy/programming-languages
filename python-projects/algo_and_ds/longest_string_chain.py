"""

this is basically a graph problem

first sorting based on length is done
using two forloop wwe find which words are connected to which other word
that way we have the graph.
then we apply a dfs and find the greatest height


"""

def predecessor(word, uniqwords):
    js = []
    for i, ch in enumerate(word):
        consider = word[:i] + word[i+1:]
        if consider in uniqwords:
            js.append(uniqwords[consider])
    return js
    
def find_connections(words):
    graph = {}
    uniqwords = {w: i for i, w in enumerate(words)}
    print(uniqwords)
    for i in range(len(words)):
        js = predecessor(words[i], uniqwords)
        for j in js:
            if j not in graph:
                graph[j] = [i]
            else:
                graph[j].append(i)
    return graph

def paths(graph, i, memo):
    if i in memo: return memo[i]
    maxheight = 1
    for nextword in graph.get(i, []):
        height = paths(graph, nextword, memo) + 1
        maxheight = max(maxheight, height)
    memo[i] = maxheight
    return maxheight

def find_paths(words, graph):
    memo = {}
    # maxval = 0
    # for i in range(len(words)):
    #     maxval = max(maxval, paths(graph, i, memo))
    #     print(memo, i)
    # return maxval

    return max(paths(graph, i, memo) for i in range(len(words)))

def main(words):
    words = sorted(words, key=len)
    # print(words)
    graph = find_connections(words)
    # print(graph)
    return find_paths(words, graph)

words = ["a","b","ba","bca","bda","bdca"]
print(main(words))

words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
print(main(words))


# ==============================

"""

this is basically a graph problem

first sorting based on length is done
using two forloop wwe find which words are connected to which other word
that way we have the graph.
then we apply a dfs and find the greatest height


"""

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def predecessor(word, uniqwords):
            js = []
            for i, ch in enumerate(word):
                consider = word[:i] + word[i+1:]
                if consider in uniqwords:
                    js.append(uniqwords[consider])
            return js

        def find_connections(words):
            graph = {}
            uniqwords = {w: i for i, w in enumerate(words)}
            # print(uniqwords)
            for i in range(len(words)):
                js = predecessor(words[i], uniqwords)
                for j in js:
                    if j not in graph:
                        graph[j] = [i]
                    else:
                        graph[j].append(i)
            return graph

        def paths(graph, i, memo):
            if i in memo: return memo[i]
            maxheight = 1
            for nextword in graph.get(i, []):
                height = paths(graph, nextword, memo) + 1
                maxheight = max(maxheight, height)
            memo[i] = maxheight
            return maxheight

        def find_paths(words, graph):
            memo = {}
            # maxval = 0
            # for i in range(len(words)):
            #     maxval = max(maxval, paths(graph, i, memo))
            #     print(memo, i)
            # return maxval

            return max(paths(graph, i, memo) for i in range(len(words)))
        
        def main(words):
            words = sorted(words, key=len)
            # print(words)
            graph = find_connections(words)
            # print(graph)
            return find_paths(words, graph)
        
        return main(words)