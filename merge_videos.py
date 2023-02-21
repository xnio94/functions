import os
import random
import string
import subprocess


def merge_videos(videos, output_name):
    list_file = ''.join(random.choices(string.ascii_letters + string.digits, k=32)) + '.txt'
    if os.path.exists(output_name):
        os.remove(output_name)
    with open(list_file, "w") as f:
        for video in videos:
            f.write(f"file {video}\n")

    # command = "ffmpeg -f concat -i " + list_file + " -c copy " + output_name
    command = ["ffmpeg", "-f", "concat", "-i", list_file, "-c", "copy", output_name]

    # time.sleep(2)
    x = subprocess.run(command)
    # time.sleep(2)
    os.remove(list_file)
