class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1

        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_front(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

        self.size += 1

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = node.next
        next_node.prev = prev_node

        self.size -= 1
    
    def remove_last(self):
        if self.size == 0:
            return None

        node = self.tail.prev
        self.remove(node)

        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        self.key_table = {}
        self.freq_table = defaultdict(DLL)
        self.min_freq = 0

    def update_freq(self, node):
        freq = node.freq

        self.freq_table[freq].remove(node)

        if freq == self.min_freq and self.freq_table[freq].size == 0:
            self.min_freq += 1

        node.freq += 1

        self.freq_table[node.freq].add_front(node)

    def get(self, key: int) -> int:
        if key not in self.key_table:
            return -1

        node = self.key_table[key]

        self.update_freq(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_table:
            node = self.key_table[key]
            node.val = value
            self.update_freq(node)
            return

        if self.size == self.capacity:
            lfu_list = self.freq_table[self.min_freq]
            node_to_remove = lfu_list.remove_last()
            del self.key_table[node_to_remove.key]
            self.size -= 1

        new_node = Node(key, value)
        self.key_table[key] = new_node
        self.freq_table[1].add_front(new_node)
        self.min_freq = 1
        self.size += 1



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
