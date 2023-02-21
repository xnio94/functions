import os
import urllib


def download_urls(urls, seed):
    count = len(urls) - 1
    valid_count = 0

    for i in range(count):
        filename = seed + str(valid_count) + ".mp4"
        if os.path.exists(filename):
            os.remove(filename)
        try:
            urllib.request.urlretrieve(urls[i], filename)
            valid_count = valid_count + 1
        except:
            print("An exception occurred")

    return valid_count
