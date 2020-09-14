we will use arr of arrs.

class SnapshotArray:
def __init__(self, length: int):
    self.data = [{} for _ in range(length))
    self.snap_id = 0
    def set(self, index: int, val: int) -> None:
        self.data[index][self.snap_id] = val
    def snap(self) -> int:
        val = self.snap_id
        self.snap_id += 1
        return val
    def get(self, index: int, snap_id: int) -> int:
        return self.data[index][snap_id]
# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

                 this porbably needs to be done using binary search according to the answers.
