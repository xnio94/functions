import random
import string
import subprocess

from functions.merge_videos import merge_videos
from functions.remove_file import remove_file
from functions.scene_detect import scene_detect


def is_consecutive(video1, video2):
    print("#########>>is_consecutive start : ")
    video1_end = video1[:-4] + ''.join(
        random.choices(string.ascii_letters + string.digits, k=16)) + '.mp4'
    video2_start = video2[:-4] + ''.join(
        random.choices(string.ascii_letters + string.digits, k=16)) + '.mp4'
    merged_result = video1[:-4] + ''.join(
        random.choices(string.ascii_letters + string.digits, k=16)) + '.mp4'
    duration = "0.2"

    print("#########>>" + video1_end + " start : ")
    # command = f'ffmpeg -sseof -{duration} -i "{video1}" -c copy "{video1_end}"'
    command = ["ffmpeg", "-sseof", f"-{duration}", "-i", video1, "-c", "copy", video1_end]
    print("#########>>" + str(command))
    subprocess.run(command)

    print("#########>>" + video2_start + " start : ")
    # command = f'ffmpeg -t {duration} -i "{video2}" -c copy "{video2_start}"'
    command = ["ffmpeg", "-t", f"{duration}", "-i", video2, "-c", "copy", video2_start]
    print("#########>>" + str(command))
    subprocess.run(command)

    print("#########>>merge_videos start : ")
    merge_videos([video1_end, video2_start], merged_result)

    print("#########>>ok")
    scenes = scene_detect(merged_result, split=False)
    remove_file(video1_end)
    remove_file(video2_start)
    remove_file(merged_result)
    return len(scenes) < 2
