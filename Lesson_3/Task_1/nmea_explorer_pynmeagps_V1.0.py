import pynmeagps  # https://pypi.org/project/pynmeagps/
from geopy.distance import geodesic
import re


Path = "nmea.log"  # if the file is in the same folder
Point_of_interest = ' Lat: 60.051584° Lon: 30.300509°'  # we got it from the task
Distance_of_interest = 25


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


def times_at_point(datafile):
    start = []
    stop = []
    check = 1
    for i in range(len(datafile)):
        if distance(datafile[i]) < Distance_of_interest and check == 1:
            start.append(pynmea_msg(datafile[i]).time)
            print('time of entry in range of ' + str(Distance_of_interest) + ' m = ' +
                  str(pynmea_msg(datafile[i]).time))
            check = 0
        if distance(datafile[i]) >= Distance_of_interest and check == 0:
            stop.append(pynmea_msg(datafile[i]).time)
            print('time of exit of range of ' + str(Distance_of_interest) + ' m = ' + str(pynmea_msg(datafile[i]).time)
                  + '\n' + '-' * 30)
            check = 1
    return start, stop


def distance(string):
    dist = geodesic((get_spot_of_interest()[0], get_spot_of_interest()[1]),
                    (pynmea_msg(string).lat, pynmea_msg(string).lon)).meters
    return dist


def pynmea_msg(string):
    msg = pynmeagps.NMEAReader.parse(string)
    return msg


def get_spot_of_interest():
    nums = re.findall(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", Point_of_interest)  # extract numbers from the string
    spot_of_interest = nums  # I've decided to leave it in a decimal format
    return spot_of_interest


def get_data():
    data_file = []
    with open(Path, 'rt') as file:
        data = file.readlines()
    for s in range(len(data)):
        if check_string(data[s]) == 'True':
            data_file.append(data[s])
    return data_file


def return_data(output):
    print(output)


def main():
    data_file = get_data()
    start, stop = times_at_point(data_file)


if __name__ == "__main__":
    main()
