class LLList:
    class Node:
        def __init__(self, val, next):
            self.val = val
            self.next = next

    def __init__(self):
        self.num_items = 0
        self.head = None

    # return the node at index i
    def __get_node(self, i):
        trav = self.head
        trav_index = 0
        while trav_index < i:
            trav_index += 1
            trav = trav.next
        return trav

    def get_item(self, i):
        if i < 0 or i >= self.num_items:
            return None

        node = self.__get_node(i)
        return node.val

    def add_item(self, item, i):
        if i < 0 or i > self.num_items:
            return False

        new_node = LLList.Node(item, None)

        if i == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev = self.__get_node(i - 1)
            new_node.next = prev.next
            prev.next = new_node

        self.num_items += 1
        return True

    def remove_item(self, i):
        if i < 0 or i >= self.num_items:
            return None

        if i == 0:
            removed = self.head.val
            self.head = self.head.next
        else:
            prev = self.__get_node(i - 1)
            removed = prev.next.val
            prev.next = prev.next.next

        self.num_items -= 1
        return removed

    def length(self):
        return self.num_items

    def is_full(self):
        return False

    def to_string(self):
        s = '['
        trav = self.head
        if trav is not None:
            while trav.next is not None:
                s += str(trav.val) + ', '
                trav = trav.next
            s += str(trav.val)
        s += ']'
        return s

    class LLListIterator:
        def __init__(self, head):
            self.cur = head

        def has_next(self):
            return self.cur is not None

        def next(self):
            item = self.cur.val
            self.cur = self.cur.next
            return item

    def iterator(self):
        return LLList.LLListIterator(self.head)
