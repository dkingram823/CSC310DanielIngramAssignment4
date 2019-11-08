class LinkedQueue:
  """FIFO queue implementation using a singly linked list for storage."""

  #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'         # streamline memory usage

    def __init__(self, element, next):
      self._element = element
      self._next = next

  #------------------------------- queue methods -------------------------------
  def __init__(self):
    """Create an empty queue."""
    self._head = None
    self._tail = None
    self._size = 0                          # number of queue elements

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Exception('Queue is empty')
    return self._head._element              # front aligned with head of list

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Exception('Queue is empty')
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    if self.is_empty():                     # special case as queue is empty
      self._tail = None                     # removed head had been the tail
    return answer

  def enqueue(self, e):
    """Add an element to the back of queue."""
    newest = self._Node(e, None)            # node will be new tail node
    if self.is_empty():
      self._head = newest                   # special case: previously empty
    else:
      self._tail._next = newest
    self._tail = newest                     # update reference to tail node
    self._size += 1

if __name__ == '__main__':
  Q = LinkedQueue()    # contents: [ ]
  Q.enqueue(5)         # contents: [5]
  Q.enqueue(3)         # contents: [5, 3]; inserting at the tail
  print(Q.first())     # Return 5; output 5
  print(len(Q))        # contents: [5, 3];    outputs 2
  print(Q.dequeue())   # Return 5; output 5; deleting at the head
  print(Q.is_empty())  # Return False; output False
  Q.dequeue()          # Return 3
  print(Q.is_empty())  # Return True; output True
  #Q.dequeue()         # Return "Error"
  Q.enqueue(7)         # contents: [7]
  Q.enqueue(9)         # contents: [7,9]
  Q.enqueue(4)         # contents: [7,9,4]
  print(len(Q))        # contents: [7,9,4];    outputs 3
  print(Q.dequeue())   # Return: 7; output 7
  print(Q.first())     # Return 9; output 9