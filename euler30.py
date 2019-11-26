# answer: 443839

powers = 5
final_list = []

for checked_num in range(2, 1000000):
    sumi = 0
    splited = list(map(int, str(checked_num)))
    for i in range(len(splited)):
        sumi += (splited[i] ** powers)
    if sumi == checked_num:
        final_list.append(checked_num)

print(f"answer: {sum(final_list)}")
