import os

# файл содержит информацию о сотрудниках и их зарплате
# данные разделены без пробела запятой
# нет проверки на пустой файл и нулевые зарплаты.

# Алекс Корп,3000
# Никита Борисенко,2000
# Sitarama Raju,1000
# Никита Борисенко.2000 ошибка

def total_salary(path) -> tuple[int, float]:
    # фунция делает просчет общей зарплаты всех сотрудников и среднюю зп.
    total = 0
    count = 0

    with open(path, 'r', encoding='utf-8') as fh:
        for line in fh:
            line = line.strip()
            if not line or ',' not in line:
                # проверяет конец файла и отсутствие "запятой", чтобы не было
                # ошибки по разделителю "точка" и не увеличивать coutn
                continue
            try:
                salary = int (line.split(',', 1)[1])
                # разбивает строку по "запятой", один раз (по первому вхождению)
                # [1] берет второй элемент списка после разделения строки.
                # [0] это первый элемент списка до "запятой"
                total += salary
                count += 1
            except ValueError:
                continue
        return total, total/count

os.system('cls')
total, average = total_salary ('salary.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average:.2f}")

