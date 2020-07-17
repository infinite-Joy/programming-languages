"""
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.
In a UNIX-style file system, a period refers to the current directory. Furthermore, a double period .. moves the directory up a level.
Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.

time complexity: O(n)
space complexity: O(n)
======================================================================
we can input a stack and if there is a new thing then we will push this into the stack and then pop out of the stack.
"""


def canonical_path(full_path):
    path = full_path.split("/")
    canonical_path = []
    for item in path:
        if item:
            if item == ".":
                pass
            elif item == "..":
                if canonical_path:
                    canonical_path.pop()
            else:
                canonical_path.append(item)
    canonical_path = "/".join(canonical_path)
    return "/" + canonical_path


print(canonical_path("/home/"))
print(canonical_path("/../"))
print(canonical_path("/home//foo/"))
print(canonical_path("/a/./b/../../c/"))
print(canonical_path("/a/../../b/../c//.//"))
print(canonical_path("/a//b////c/d//././/.."))
