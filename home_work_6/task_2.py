t = int(input("Enter the seconds to get a date from 0 to 86400000: "))
if 0 <= t < 8640001:
    days = t//86400
    hours = (t% 86400) // 3600
    minutes = (t% 86400) % 3600 //60
    seconds = (t% 86400) % 3600 %60
    h_str = str(hours).zfill(2)
    m_str = str(minutes).zfill(2)
    s_str = str(seconds).zfill(2)
    day_word = True
    if days % 10 == 1 and days !=11:
        day_word = "День"
    elif days % 10 in [2,3,4] and days%10 not in [12,13,14]:
        day_word = "Днi"
    else:
        day_word = "Днiв"
    print(f"{days} {day_word}, {h_str}:{m_str}:{s_str}")
else :
    print("Invalid input")
