disks = 5
from_tower = "A"
to_tower = "B"
using_tower = "C"


def move_tower(N, from_tower, to_tower, using_tower):
    if N > 0:
        move_tower(N-1, from_tower, using_tower, to_tower)
        print("move disk {} from {} to {}".format(N, from_tower, to_tower))
        move_tower(N-1, using_tower, to_tower, from_tower)


move_tower(disks, from_tower, to_tower, using_tower)
