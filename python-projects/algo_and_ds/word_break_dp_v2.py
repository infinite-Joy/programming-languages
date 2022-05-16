


def dp(string, wordDict):
    if string=="":
        return True
    else:
        for word in wordDict:
            if string.startswith(word) and dp(string[len(word):], wordDict):
                print(string, word)
                return True
            if string.endswith(word) and dp(string[:len(string)-len(word)], wordDict):
                print(string, word)
                return True
        print(string, word)        
        return False


string = "catsandog"
words = ["cats","dog","sand","and","cat"]
print(dp(string, words))



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dp(string, wordDict, memo=None):
            memo = {} if memo is None else memo
            if string in memo: return memo[string]
            
            if string=="":
                return True
            else:
                for word in wordDict:
                    if string.startswith(word) and dp(string[len(word):], wordDict, memo):
                        memo[string] = True
                        return True
                    if string.endswith(word) and dp(string[:len(string)-len(word)], wordDict, memo):
                        memo[string] = True
                        return True
                memo[string] = False
                return False
                    
        return dp(s, wordDict)