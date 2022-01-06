# about NMEA http://wiki.amperka.ru/articles:gps:nmea


import re
import math


R = 6371  # Earth radius
Path = "nmea.log"  # if the file is in the same folder
Point_of_interest = ' Lat: 60.051584° Lon: 30.300509°'  # we got it from the task
Distance_of_interest = 25


def get_data():
    with open(Path, 'rt') as file:
        input_data_file = []
        data_file = []
        for line in file:
            input_data_file.append(line)
        for s in range(len(input_data_file)):
            if check_string(input_data_file[s]) == 'True':
                data_file.append(input_data_file[s])
    return data_file


def check_string(str_of_data):  # with the use of check sum in the end of the string
    check_sum = 0
    if str_of_data[0] != '$':
        return 'False'
    else:
        if str_of_data.find('*') == -1:
            return 'False'
        else:
            for i in range(1, str_of_data.rfind('*')):
                if check_sum == 0:
                    check_sum = ord(str_of_data[i])
                else:
                    check_sum = check_sum ^ ord(str_of_data[i])
            if str(str_of_data[str_of_data.rfind('*') + 1: -1]).lower() == str(hex(check_sum))[2:4]:
                return 'True'
            else:
                return 'False'


def get_time_interval(data_file):
    spot_of_interest = get_spot_of_interest()
    time_interval = 0
    for i in range(len(data_file) - 1):
        string_of_data = (data_file[i]).split(',')
        latitude = convert_nmea_to_decimal(string_of_data[2], string_of_data[3])
        longitude = convert_nmea_to_decimal(string_of_data[4], string_of_data[5])
        dist = distance(float(latitude), float(longitude), float(spot_of_interest[0]),
                        float(spot_of_interest[1])) * 1000
        if dist < Distance_of_interest:
            time_bit = get_time_bit(data_file, i)
            time_interval += time_bit
    return time_interval


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
    nums = re.findall(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", Point_of_interest)  # extract numbers from the string
    spot_of_interest = nums  # I've decided to leave it in a decimal format
    return spot_of_interest


def return_data(output):
    print(convert_time_to_hhmmss(output))


def main():
    data_file = get_data()
    output = get_time_interval(data_file)
    return_data(output)


if __name__ == "__main__":
    main()
