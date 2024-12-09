import datetime
import re

import urllib3
from config import FEEDS

import pandas as pd


class Feed:
    """Arbor Feed retieval class

    :var url: URL of Arbor feed
    :vartype: str
    :var data: JSON feed from Arbor
    :vartype data: list
    :var length: Length of feed list
    :vartype length: int
    :var time_string: Time Taken to retrieve the feed
    :vartype time_str: str
    :var status: Status code
    :vartype status: int
    """

    def __init__(self, url):
        self.url = url
        self.data = []
        self.status = -1
        self.length = 0
        self.time_str = ""

    def getResponse(self):
        no_timeout = urllib3.Timeout(connect=2, read=120)
        http = urllib3.PoolManager()
        now = datetime.datetime.now()

        try:
            self.data = http.request("GET", self.url, timeout=no_timeout)
        except MaxRetryError:  # type: ignore  # noqa: F821
            print(f"GET failed")  # noqa: F541
        else:
            self.status = self.data.status
            self.data = self.data.json()
            self.length = len(self.data)

        now = (datetime.datetime.now() - now) * 60
        pattern = "(.*\:.*)\:"
        if match := re.search(pattern, f"{now}"):
            self.time_str = match.group(1)

        return self.status

    def __str__(self):
        str = f"\n\nFeed {self.url}\n"
        str += f"It took {self.time_str} sec and has {self.length} records.\n"
        str += f"Return status: {self.status}\n"
        str += f"First record is:\n{self.data[0]}"

        return str


def save_CSV(filename, data):
    """Save data to CSV file"""
    df = pd.DataFrame(data)
    df.to_csv(f"data/{filename}.csv", index=False)
    return True


def moveToOneDrive():
    """
    Move to OneDrive
    """
    print("moving")
    return True


def main():
    # get the feed using the imported class
    for k in FEEDS.keys():
        print(k)
        feed = Feed(FEEDS[k])
        feed.getResponse()

        # create the XLSX document
        if not save_CSV(k, feed.data):
            raise ValueError
        else:
            print(
                f"Check filesystem\nStatus: {feed.status}\n{feed.length} records created in {feed.time_str} mins"
            )


if __name__ == "__main__":
    main()
