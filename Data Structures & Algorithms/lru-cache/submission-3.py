class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hash = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        self.hash.move_to_end(key)
        return self.hash[key]


    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.hash.move_to_end(key)
        self.hash[key] = value

        if len(self.hash) > self.cap:
            self.hash.popitem(last = False)
        
        
