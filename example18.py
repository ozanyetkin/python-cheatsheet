# 10000 metre uzaklikta iki arac, 80 km/sa ile giden bir arac 60 km/sa ile giden diger araci kac saat kac dakika kac saniye sonra yakalar?
def inter_time(distance, speed_1, speed_2):
    distance = distance / 1000
    total_time =  (distance / abs(speed_1 - speed_2)) * 3600
    formatted_time = format_time(total_time)
    return formatted_time

def format_time(total_time):
    time_seconds = total_time % 60
    time_minutes = (total_time // 60) % 60
    time_hours = (total_time // 3600) % 60
    return f"{int(time_hours)}:{int(time_minutes)}:{int(time_seconds)}"

print(inter_time(10000, 60, 55))
print(format_time(4500))
