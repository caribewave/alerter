import sys
import argparse

from services import (
    sender, listener, alerting)


if __name__ == "__main__":
    service = sys.argv[1]
    if service == "sender":
        mod = sender
    elif service == "listener":
        mod = listener
    elif service == "alerting":
        mod = alerting
    else:
        raise ValueError('Service not found')

    if hasattr(mod, "get_argparser"):
        parser = getattr(mod, "get_argparser")()
    else:
        parser = argparse.ArgumentParser(description='Run listener')

    parser.add_argument('service', type=str, help='Service name')
    kwargs = vars(parser.parse_args())
    del kwargs["service"]
    getattr(mod, 'run')(**kwargs)
