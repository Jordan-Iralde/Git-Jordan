import time
import random

def reaction_test():
    print("Preparate...")
    time.sleep(random.randint(2, 5))  # Espera entre 2 a 5 segundos
    print("¡YA!")
    start_time = time.time()
    input("Presiona Enter lo más rápido posible...")
    reaction_time = time.time() - start_time
    print(f"Tu tiempo de reacción es: {reaction_time:.3f} segundos")

if __name__ == "__main__":
    while True:
        reaction_test()
        again = input("¿Quieres intentarlo de nuevo? (s/n): ").strip().lower()
        if again != 's':
            break

