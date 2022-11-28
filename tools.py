import time
from datetime import datetime, timedelta

import pytz as pytz


def get_now():
    tz = pytz.timezone('Europe/Paris')
    return datetime.now(tz)


def get_sun_times():
    import requests

    url = "https://api.sunrise-sunset.org/json"
    bordeaux_location = {"lat": "44.85642", "lng": "-0.5910801", "formatted": 0}

    try:
        response = requests.request("GET", url, params=bordeaux_location).json()["results"]
        return {
            "sunrise": datetime.strptime(response["sunrise"], '%Y-%m-%dT%H:%M:%S%z') + timedelta(hours=1),
            "sunset": datetime.strptime(response["sunset"], '%Y-%m-%dT%H:%M:%S%z') + timedelta(hours=1)
        }
    except:
        return {
            "sunrise": datetime.strptime('2022-11-24T08:09:44+00:00', '%Y-%m-%dT%H:%M:%S%z'),
            "sunset": datetime.strptime('2022-11-24T17:28:19+00:00', '%Y-%m-%dT%H:%M:%S%z')
        }


class Timer:
    checkin = time.monotonic()
    counter = 0
    seconds = 0

    def update(self):
        self.counter += 1
        if time.monotonic() - self.checkin > 1.0:
            self.seconds += 1
            print("(approx)", self.seconds, "seconds have elapsed.", self.counter, "loops")
            self.checkin = time.monotonic()
            self.counter = 0


if __name__ == '__main__':
    sun_time = get_sun_times()
    print(sun_time)
