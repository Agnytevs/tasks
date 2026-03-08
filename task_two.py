s = input()
stack = []        
now = ''
num = 0

for i in range(len(s)):
    if s[i].isdigit():
        num = int(str(num) + str(s[i])) # составляем число
    elif s[i] == '[':
        stack.append([now, num]) # добавляем в список предыдущую строку и число - кол-ва раз, сколько надо будет повторить следующую
        now = '' # очищаем now и num, чтобы после положить в них следующую скобочку
        num = 0
    elif s[i] == ']':
        now = stack[-1][0] + now * stack[-1][1]
        stack.pop()
    else:
        now += s[i]
print(now)