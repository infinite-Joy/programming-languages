class LinkedListStack:

    class _Nodes:

        """Docstring for _Nodes. """

        __slots__ = ('_element', '_next')

        def __init__(self, element, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0
        self._last = None

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Nodes(e, self._head)
        self._size += 1

    def top(self):
        """Return the top element but do not remove"""
        if self._size == 0:
            return ValueError('no elements in the LinkedListStack')
        return self._head._element

    def pop(self):
        if self._size == 0:
            return ValueError("No more elements in the list")
        val = self._head._element
        self._head = self._head._next
        self._size -= 1
        return val

    def __str__(self):
        element = self._head
        final_repr = ["{}".format(element._element)]
        while element._next is not None:
            val = element._next
            final_repr.append(str(val._element))
            element = element._next
        final_repr.append("None")
        final_repr = " -> ".join(final_repr)
        final_repr = "stack size: {}, link list: {}".format(
            self._size, final_repr)
        return final_repr





class LinkedListQueue:

    class _Nodes:

        """Docstring for _Nodes. """

        __slots__ = ('_element', '_next')

        def __init__(self, element, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0
        self._tail = None

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        e = self._Nodes(e)
        if self._head is None:
            self._head = e
            self._tail = e
        else:
            self._tail._next = e
            self._tail = e
        self._size += 1

    def first(self):
        """Return the top element but do not remove"""
        if self._size == 0:
            return ValueError('no elements in the LinkedListStack')
        return self._head._element

    def last(self):
        if self._size == 0:
            return ValueError('no elements in the LinkedListStack')
        return self._tail._element

    def dequeue(self):
        if self._size == 0:
            return ValueError("No more elements in the list")
        val = self._head._element
        self._head = self._head._next
        self._size -= 1
        return val

    def __str__(self):
        element = self._head
        final_repr = ["{}".format(element._element)]
        while element._next is not None:
            val = element._next
            final_repr.append(str(val._element))
            element = element._next
        final_repr.append("None")
        final_repr = " -> ".join(final_repr)
        final_repr = "queue size: {}, link list: {}".format(
            self._size, final_repr)
        return final_repr


if __name__ == "__main__":
    print("checking for stack")
    l = LinkedListStack()
    l.push(1)
    l.push(2)
    l.push(3)
    l.push(4)
    print(l.pop())
    print(l.pop())
    print(l.top())
    l.push(5)
    print(l)
    print(len(l))



    print("below checking for queue")
    l = LinkedListQueue()
    l.enqueue(1)
    l.enqueue(2)
    l.enqueue(3)
    l.enqueue(4)
    print("dequeue", l.dequeue())
    l.enqueue(5)
    print(l)
    print("dequeue", l.dequeue())
    print(l)
    print(len(l))
