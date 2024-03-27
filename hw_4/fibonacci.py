import threading
import multiprocessing
import time

# Функция для вычисления n-го числа Фибоначчи
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Функция для исполнения фибоначчи и замера времени
def run_fibonacci(n, method_name):
    start_time = time.time()
    fibonacci(n)
    end_time = time.time()
    print(f"{method_name} execution time: {end_time - start_time:.5f} seconds")

def main():
    n = 35  # Большое число для наглядности
    num_executions = 10  # Количество запусков функции

    # Синхронный запуск
    print("Synchronous:")
    for _ in range(num_executions):
        run_fibonacci(n, "Synchronous")

    # Многопоточный запуск
    print("\nThreading:")
    threads = [threading.Thread(target=run_fibonacci, args=(n, "Threading")) for _ in range(num_executions)]
    [t.start() for t in threads]
    [t.join() for t in threads]

    # Многопроцессный запуск
    print("\nMultiprocessing:")
    processes = [multiprocessing.Process(target=run_fibonacci, args=(n, "Multiprocessing")) for _ in range(num_executions)]
    [p.start() for p in processes]
    [p.join() for p in processes]

if __name__ == "__main__":
    main()
