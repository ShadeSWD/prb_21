import re
import math
R = 6371  # Earth radius


def get_data():
    path = "nmea.log"  # if the file is in the same folder
    file = open(path, 'rt')
    input_data_file = []
    data_file = []
    for line in file:
        input_data_file.append(line)
    for s in range(len(input_data_file) - 1):
        i = check_string(input_data_file[s])
        if i == 1:
            data_file.append(input_data_file[s])
    return data_file


def check_string(str_of_data):
    if len(str_of_data) == 80:
        i = 1
    else:
        i = 0
    return i


def get_time_interval(data_file):
    spot_of_interest = get_spot_of_interest()
    time_interval = 0
    for i in range(len(data_file) - 1):
        string_of_data = (data_file[i]).split(',')
        latitude = convert_nmea_to_decimal(string_of_data[2], string_of_data[3])
        longitude = convert_nmea_to_decimal(string_of_data[4], string_of_data[5])
        dist = distance(float(latitude), float(longitude), float(spot_of_interest[0]),
                        float(spot_of_interest[1])) * 1000
        if dist < int(get_distance_of_interest()):
            time_bit = get_time_bit(data_file, i)
            time_interval += time_bit
    return time_interval


def get_distance_of_interest():
    distance_of_interest = 25
    return distance_of_interest


#  https://coderoad.ru/36254363/%D0%9A%D0%B0%D0%BA-%D0%BF%D1%80%D0%B5%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C-%D1%88%D0%B8%D1%80%D0%BE%D1%82%D1%83-%D0%B8-%D0%B4%D0%BE%D0%BB%D0%B3%D0%BE%D1%82%D1%83-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B0-NMEA-%D0%B2-%D0%B4%D0%B5%D1%81%D1%8F%D1%82%D0%B8%D1%87%D0%BD%D1%83%D1%8E
def convert_nmea_to_decimal(nmea_position, nmea_quadrant):
    nmea_position_split = nmea_position.split('.')
    integer_part = (nmea_position_split[0])[:-2]
    minute_part = float((nmea_position_split[0])[-2:] + '.' + nmea_position_split[1])/60
    degree_position = round(int(integer_part) + float(minute_part), 6)
    if nmea_quadrant == 'W' or nmea_quadrant == 'S':
        degree_position = - degree_position
    return degree_position


# https://coderoad.ru/27928/%D0%92%D1%8B%D1%87%D0%B8%D1%81%D0%BB%D0%B8%D1%82%D1%8C-%D1%80%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D0%B5-%D0%BC%D0%B5%D0%B6%D0%B4%D1%83-%D0%B4%D0%B2%D1%83%D0%BC%D1%8F-%D1%82%D0%BE%D1%87%D0%BA%D0%B0%D0%BC%D0%B8-%D1%88%D0%B8%D1%80%D0%BE%D1%82%D1%8B-%D0%B8-%D0%B4%D0%BE%D0%BB%D0%B3%D0%BE%D1%82%D1%8B-%D0%A4%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D0%B0-%D0%B3%D0%B0%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%BD%D1%83%D1%81%D0%B0
def distance(lat1, lon1, lat2, lon2):  # using Haversine formula
    p = math.pi/180
    a = 0.5 - math.cos((lat2-lat1)*p)/2 + math.cos(lat1*p) * math.cos(lat2*p) * (1-math.cos((lon2-lon1)*p))/2
    return 2 * R * math.asin(math.sqrt(a))


def get_time_bit(data_file, i):  # different files can get different sampling frequency, so we calculate it
    if i == 0:
        time_bit = 0
    else:
        start_time = convert_time_to_seconds(data_file[i - 1])
        end_time = convert_time_to_seconds(data_file[i])
        time_bit = end_time - start_time
    return time_bit


def convert_time_to_seconds(str_of_data):
    spl_str_of_data = str_of_data.split(',')
    spl_time = spl_str_of_data[1]
    hours_in_sec = float(spl_time[:2]) * 3600
    min_in_sec = float(spl_time[2:4]) * 60
    sec = float(spl_time[4:])
    time_in_sec = hours_in_sec + min_in_sec + sec
    return time_in_sec


def convert_time_to_hhmmss(time_in_sec):
    hh = round(time_in_sec // 3600)
    mm = round((time_in_sec % 3600) // 60)
    ss = round((time_in_sec % 60), 2)
    time = (str(hh) + ' hours ' + str(mm) + ' min ' + str(ss) + ' sec')
    return time


def get_spot_of_interest():
    we_get = ' Lat: 60.051584° Lon: 30.300509°'  # we got it from the task
    nums = re.findall(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", we_get)  # extract numbers from the string
    spot_of_interest = nums  # I've decided to leave it in a decimal format, so I don't use commented below
    """s = 0
    while s < 2:
        split_nums = nums[s].split('.')
        degrees = split_nums[0]
        minutes = str(int(split_nums[1]) * 60)
        minutes = minutes[0:2] + '.' + minutes[1:6]
        spot_of_interest.append(degrees + str(minutes))
        s += 1"""
    return spot_of_interest


def return_data(output):
    print(convert_time_to_hhmmss(output))


def main():
    data_file = get_data()
    output = get_time_interval(data_file)
    return_data(output)


if __name__ == "__main__":
    main()
