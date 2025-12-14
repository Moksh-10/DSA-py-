class hm:
    def __init__(self, capacity):
        self.cp = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def __len__(self):
        return self.size

    def __contains__(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return True

    def put(self, key, value):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):


    def get(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError('key not found')

    def remove(self, key):
        pass

    def keys(self):
        pass

    def values(self):
        pass

    def items(self):
        pass

    def _hash_function(self, key):
        key_str = str(key)
        hr = 0
        for c in key_str:
            hr = (hr * 31 + orc(c)) % self.cp
