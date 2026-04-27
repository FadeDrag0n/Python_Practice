#Блок 4. Регулярні вирази (Module re)
import re

#4.1. Пошук та валідація:

res1 = re.match(r"\d+", "123abc")
res2 = re.match(r"\d+", "abc123")
res3 = re.search(r"\d+", "abc123")

print(res1.group())
print(res2 or None)
print(res3.group())

#4.1.2.

res4 = re.split(r"\s+", "Hello   world  test")
print(res4)

#4.2. Оптимізація:

pattern = re.compile(r"\d+")
print(pattern.match("123abc").group())
print(pattern.match("abc123") or None)

#4.3. Обробка текстових шаблонів:
res5 = re.findall(r'\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print(res5)

#4.3.2. Робота з Email:
email_str = "abc.test@gmail.com, fifa@chmnu.edu, qwerty@ukr.net"
res6 = re.findall(r"@(.+)", email_str)
print(res6)

res7= re.findall(r"@(\w+)\.(\w+)", email_str)
print(res7)