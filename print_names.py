print("Zhalgaspayeva Ayakoz")
print("Myrzakul Bekarys")

import sys

# Проверяем, переданы ли аргументы
if len(sys.argv) > 1:
    # Выводим все переданные имена
    print("Names:", " ".join(sys.argv[1:]))
else:
    print("No names provided.")
