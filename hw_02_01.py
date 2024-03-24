import queue
import time
import random
import sys
import select

def generate_request(request_queue, request_id):
    """Генерує нову заявку з унікальним ідентифікатором та додає її до черги."""
    print(f"Генеруємо заявку з ID: {request_id}")
    request_queue.put(request_id)
    time.sleep(random.uniform(1, 2))  # Імітація випадкової затримки

def process_request(request_queue):
    """Обробляє першу заявку в черзі, якщо черга не пуста."""
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Обробляємо заявку з ID: {request_id}")
        time.sleep(random.uniform(1, 3))# Затримка для імітації часу на обробку
    else:
        print("Черга пуста, немає заявок для обробки.")
        time.sleep(2)

def main():
    request_queue = queue.Queue()
    request_id = 1

    print("Програма запущена. Натисніть ctrl+c для виходу...")

    try:
        while True:
            # Перевірка наявності вводу від користувача
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                line = input()
                break

            # Генерація та обробка заявок
            generate_request(request_queue, request_id)
            request_id += 1
            process_request(request_queue)

    except KeyboardInterrupt:
        pass

    print("Програма завершена.")

if __name__ == "__main__":
    main()
