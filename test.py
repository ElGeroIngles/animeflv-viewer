import time

for i in range(10):
    print(f"\rContando: {i}", end="", flush=True)
    time.sleep(0.5)
print("\n¡Terminado!")
