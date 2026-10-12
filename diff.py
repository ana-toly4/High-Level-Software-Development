# -*- coding: utf-8 -*-
import sys

# Заголовок та вивід поточної версії інтерпретатора
print("Py2 vs Py3")
print("Current version: %s" % sys.version_info[0])

# 1. Print (у Python 2 це оператор, у Python 3 - функція)
print("1. Print syntax is evaluated differently.")

# 2. Ділення цілих чисел 
# (У Py2: 5/2 = 2 | У Py3: 5/2 = 2.5)
print("2. Division (5/2): %s" % (5 / 2))

# 3. Типи рядків 
# (У Py2 рядки байтові <type 'str'> | У Py3 - unicode <class 'str'>)
print("3. String type: %s" % type("Test"))

# 4. Введення даних та 5. Генерація діапазонів
if sys.version_info[0] >= 3:
    # Python 3 використовує input() та оптимізований range()
    print("4. Uses input() for reading strings")
    print("5. range(3) returns object: %s" % type(range(3)))
else:
    # Python 2 використовує raw_input() та окрему функцію xrange()
    print("4. Uses raw_input() for reading strings")
    print("5. xrange(3) is used for memory efficiency")

# 6. Синтаксис обробки винятків 
# (У Py2: except Exception, e | У Py3: except Exception as e)
try:
    1 / 0
except Exception as e:
    print("6. Exception syntax type: %s" % type(e))

# 7. Ітератори 
# (У Py2 використовувався метод .next(), у Py3 - вбудована функція next())
it = iter([1, 2])
print("7. Next element from iterator: %s" % next(it))

# 8. Методи словників 
# (У Py2 .keys() повертає список, у Py3 - спеціальний об'єкт view)
d = {'a': 1}
print("8. Type of dict.keys(): %s" % type(d.keys()))

# 9. Порівняння різних типів 
# (У Py2 можна порівняти рядок і число, у Py3 це викликає TypeError)
try:
    eval("'a' > 1")
    print("9. Cross-type comparison: Allowed (Py2)")
except TypeError:
    print("9. Cross-type comparison: Raises TypeError (Py3)")

# 10. Округлення 
# (У Py2 round(2.5) -> 3.0, у Py3 працює банківське округлення -> 2)
print("10. Rounding round(2.5): %s" % round(2.5))