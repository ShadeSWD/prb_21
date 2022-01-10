import pynmeagps  # https://pypi.org/project/pynmeagps/
import pynmea2
from geopy.distance import geodesic
import re


Path = "nmea.log"  # if the file is in the same folder
Point_of_interest = ' Lat: 60.051584° Lon: 30.300509°'  # we got it from the task
Distance_of_interest = 25


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
                  + '\n' + '-' * 50)
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
    print('Reading file...' + '\n' + '+' * 50)
    with open(Path, 'rt') as file:
        data = file.readlines()
    for s in range(len(data)):
        check = 'True'
        try:
            nmr = pynmea2.parse(data[s], check=True)
        except:
            check = 'False'
        if check == 'True':
            data_file.append(data[s])
    print('Calculating...' + '\n' + '+' * 50)
    return data_file


def return_data(output):
    print(output)


def main():
    print('Welcome to nmea_explorer .-)' + '\n' + '=' * 50)
    data_file = get_data()
    start, stop = times_at_point(data_file)


if __name__ == "__main__":
    main()
