import time

from caribewave.places import Places


def run():
    while True:
        places = Places()
        places.sync()
        time.sleep(60)

if __name__ == "__main__":
    run()
