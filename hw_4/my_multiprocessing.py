import multiprocessing
import time
import codecs

def process_a(queue_from_main, conn_to_b):
    while True:
        if not queue_from_main.empty():
            msg = queue_from_main.get()  # Получаем сообщение из основной очереди
            processed_msg = msg.lower()  # Применяем .lower()
            conn_to_b.send(processed_msg)  # Отправляем обработанное сообщение в процесс B
            time.sleep(5)  # Ждем 5 секунд перед обработкой следующего сообщения

def process_b(conn_from_a):
    while True:
        if conn_from_a.poll():  # Проверяем, есть ли что-то для чтения
            msg = conn_from_a.recv()  # Получаем сообщение из процесса A
            encoded_msg = codecs.encode(msg, 'rot_13')  # Применяем кодирование rot13
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Encoded message: {encoded_msg}")

def main():
    queue_from_main = multiprocessing.Queue()  # Очередь для сообщений от главного процесса к A
    a_to_b, b_from_a = multiprocessing.Pipe()  # Каналы для связи между A и B

    # Запуск процессов
    process_a_proc = multiprocessing.Process(target=process_a, args=(queue_from_main, a_to_b))
    process_b_proc = multiprocessing.Process(target=process_b, args=(b_from_a,))

    process_a_proc.start()
    process_b_proc.start()

    try:
        while True:
            message = input("Enter a message (type 'exit' to stop): ")
            if message == 'exit':
                break
            queue_from_main.put(message)  # Отправляем сообщение в очередь для процесса A
    finally:
        process_a_proc.terminate()  # Останавливаем процессы
        process_b_proc.terminate()

if __name__ == "__main__":
    main()

