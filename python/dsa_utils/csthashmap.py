from typing import Any

class CustomHashMap:

    def __init__(self, initial_capacity: int = 16):
        self.capacity = initial_capacity
        self.size = 0

        self.buckets = [[] for _ in range(self.capacity)]

    def _get_bucket_index(self, key) -> int:
        return abs(hash(key)) % self.capacity

    def __setitem__(self, key, value) -> None:
        bucket = self.buckets[self._get_bucket_index(key)]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])
        self.size += 1

    def __getitem__(self, key):

        bucket = self.buckets[self._get_bucket_index(key)]

        for existing_key, value in bucket:
            if existing_key == key:
                return value

        raise KeyError(key)

    def __delitem__(self, key: Any) -> Any:

        bucket = self.buckets[self._get_bucket_index(key)]

        for pair in bucket:
            if pair[0] == key:
                bucket.remove(pair)
                self.size -= 1
                return

        raise KeyError(key)

    def __contains__(self, key) -> bool:

        bucket = self.buckets[self._get_bucket_index(key)]
        return any(existing_key == key for existing_key, _ in bucket)

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:

        items = []
        for bucket in self.buckets:
            for key, value in bucket:
                items.append(f"{repr(key)}: {repr(value)}")
        return "{" + ", ".join(items) + "}"
