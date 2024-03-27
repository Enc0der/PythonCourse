import math
import time
import concurrent.futures
import logging

# Настройка логирования
logging.basicConfig(filename='integrate_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Функция для подсчета интеграла на отрезке
def integrate_part(f, start, end, num_points):
    logging.info(f"Task for interval {start} to {end} started")
    step = (end - start) / num_points
    result = 0.5 * (f(start) + f(end))
    for i in range(1, num_points):
        result += f(start + i * step)
    result *= step
    logging.info(f"Task for interval {start} to {end} finished")
    return result

# Функция для распараллеленного вычисления интеграла
def integrate(f, start, end, n_jobs=1, executor_type='thread'):
    num_points = 10000  # Общее число точек для интегрирования
    points_per_job = num_points // n_jobs  # Число точек на задачу

    # Разбиение интервала на подинтервалы для каждого задания
    intervals = [(start + i * (end - start) / n_jobs, start + (i + 1) * (end - start) / n_jobs) for i in range(n_jobs)]

    # Выбор исполнителя: потоки или процессы
    if executor_type == 'thread':
        executor_class = concurrent.futures.ThreadPoolExecutor
    else:
        executor_class = concurrent.futures.ProcessPoolExecutor

    # Выполнение заданий в параллель
    start_time = time.time()
    with executor_class(max_workers=n_jobs) as executor:
        futures = [executor.submit(integrate_part, f, start, end, points_per_job) for start, end in intervals]
        result = sum(f.result() for f in concurrent.futures.as_completed(futures))
    end_time = time.time()

    logging.info(f"Integrate with {n_jobs} jobs and {executor_type}: {end_time - start_time} seconds")
    return result, end_time - start_time

def main():
    cpu_num = 4  # Замените на число ядер вашего CPU
    results = []

    for executor_type in ['thread', 'process']:
        for n_jobs in range(1, cpu_num * 2 + 1):
            _, time_taken = integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, executor_type=executor_type)
            results.append((executor_type, n_jobs, time_taken))

    # Запись результатов в файл
    with open('integrate_times.txt', 'w') as f:
        for executor_type, n_jobs, time_taken in results:
            f.write(f"{executor_type}, {n_jobs} jobs: {time_taken} seconds\n")

if __name__ == "__main__":
    main()
