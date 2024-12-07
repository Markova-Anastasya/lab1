def find_common_participants (a, b, spl=','):
    surnames1 = a.split(spl)
    surnames2 = b.split(spl)
    common_participants = list(set(surnames1).intersection(surnames2))
    common_participants.sort()
    return(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants_int = find_common_participants(participants_first_group, participants_second_group, "|")
print(participants_int)