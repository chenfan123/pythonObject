"""用小尺寸 bit 数组演示 Bloom Filter 的核心行为。

真实系统应使用 Redis Bloom 或等价组件；本文件故意把 bit 数组设得很小，
以便在本地实验中更容易观察到 false positive（假阳性）。
"""

from hashlib import blake2b


class BloomFilter:
    def __init__(self, bit_count: int, hash_count: int) -> None:
        self.bits = bytearray(bit_count)
        self.bit_count = bit_count
        self.hash_count = hash_count

    def _indexes(self, value: str) -> list[int]:
        indexes: list[int] = []
        for seed in range(self.hash_count):
            digest = blake2b(f"{seed}:{value}".encode(), digest_size=8).digest()
            indexes.append(int.from_bytes(digest, "big") % self.bit_count)
        return indexes

    def add(self, value: str) -> None:
        for index in self._indexes(value):
            self.bits[index] = 1

    def might_contain(self, value: str) -> bool:
        return all(self.bits[index] == 1 for index in self._indexes(value))


def main() -> None:
    bloom = BloomFilter(bit_count=16, hash_count=3)
    existing_product_ids = {"42", "100", "500"}

    for product_id in existing_product_ids:
        bloom.add(product_id)

    print(f"有效商品 ID: {sorted(existing_product_ids)}")
    print(f"已置位 bit: {list(bloom.bits)}")

    for product_id in ("42", "999"):
        print(f"{product_id}: might_contain -> {bloom.might_contain(product_id)}")

    false_positive = next(
        product_id
        for product_id in map(str, range(1, 10_000))
        if product_id not in existing_product_ids and bloom.might_contain(product_id)
    )
    print(f"找到假阳性: {false_positive} (真实不存在，但过滤器说可能存在)")


if __name__ == "__main__":
    main()
