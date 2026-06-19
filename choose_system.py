import hashlib

name = "Ольга Зырянова"

systems = [
    "Ubuntu 18.04",
    "Ubuntu 20.04", 
    "Debian 10",
    "Debian 11",
    "Fedora 34",
    "Fedora 35"
]

hash_value = int(hashlib.sha256(name.encode('utf-8')).hexdigest(), 16)
selected = systems[hash_value % len(systems)]

print(f"Для {name} рекомендуется система: {selected}")
