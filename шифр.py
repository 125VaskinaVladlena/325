import hashlib

def simple_hash(input_bytes: bytes) -> bytes:
    hasher = hashlib.sha256()
    hasher.update(input_bytes)
    return hasher.digest()

if __name__ == "__main__":
    data = "Пример входных данных для хеширования".encode("utf-8")
    hash_bytes = simple_hash(data)
    print("Входные данные:", data)
    print("Хеш (в байтах):", hash_bytes)
    print("Хеш (в hex):", hash_bytes.hex())