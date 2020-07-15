"""
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation:
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].

what can be done is that people can be grouped if there are the same group size. and if both left and right groups  have not exceeded their groupings.
so for all the new ids, try joining with one of the previous components. if am able to join then there its fine. else will create a new set out of this

===================================

time complexity with path compression: O((m+n)(logn)) so there is an additional n component here for the forloop
    this would be n2logn and for the amortised case it would be n2
space complexity is O(n)
"""
class UnionFind:

    def __init__(self, size):
        self.size = size
        self.sz = [1 for _ in range(size)]
        self.root_pointer = [i for i in range(size)]
        self.num_components = size
        self.comps = {i: [i] for i in range(size)}

    def __repr__(self):
        return "UF size: {}, sz: {}, root_pointer: {}, num_components: {}, comps: {}".format(self.size, self.sz, self.root_pointer, self.num_components, self.comps)

    def __str__(self):
        return repr(self)

    def find(self, p, rps):
        if rps is None:
            rps = self.root_pointer
        if rps[p] == p:
            return p
        rps[p] = self.find(rps[p], rps)
        return rps[p]

    def connected(self, p, q):
        return self.root_pointer[p] == self.root_pointer[q]

    def union(self, p, q, group_sizes):
        if self.connected(p, q) is True:
            return
        root1 = self.root_pointer[p]
        root2 = self.root_pointer[q]
        component_lost = None
        if (
            group_sizes[p] > self.sz[root1] and
            group_sizes[q] > self.sz[root2] and
            group_sizes[p] == group_sizes[q] and
            group_sizes[p] >= self.sz[root1] + self.sz[root2]
        ):
            if self.sz[root1] < self.sz[root2]:
                component_lost = root1
                self.sz[root2] += self.sz[root1]
                self.comps[root2].extend(self.comps[root1])
                self.root_pointer[root1] = root2
            else:
                component_lost = root2
                self.sz[root1] += self.sz[root2]
                self.comps[root1].extend(self.comps[root2])
                self.root_pointer[root2] = root1
            self.num_components -= 1
            if component_lost is not None:
                del self.comps[component_lost]
        return True


def main(group_sizes):
    size = len(group_sizes)
    disjoint_sets = UnionFind(size)
    #__import__('pdb').set_trace()
    for i in range(size):
        curr_comp_size = disjoint_sets.num_components
        new_comp_size  = disjoint_sets.num_components
        j = 0
        components = list(disjoint_sets.comps.keys())
        while curr_comp_size == new_comp_size and j < len(components):
            q = components[j]
            disjoint_sets.union(i, q, group_sizes)
            j += 1
            new_comp_size = disjoint_sets.num_components
        print(disjoint_sets)
    return [list(v) for _, v in disjoint_sets.comps.items()]


print(main([3,3,3,3,3,1,3]))

