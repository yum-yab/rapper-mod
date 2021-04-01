from app import app
import os, sys


if __name__ == "__main__":

    # check if rapper is even installed
    from shutil import which

    if which("rapper") is None:
        print("ERROR: rapper is not installed!")
        sys.exit(1)

    app.run()