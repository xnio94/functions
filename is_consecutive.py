import glob
import random
import string
import subprocess

from functions.dynamic_import import dynamic_import
from functions.logging import log_state


def is_consecutive(video1, video2):
    merge_videos = dynamic_import('merge_videos')
    remove_file = dynamic_import('remove_file')
    scene_detect = dynamic_import('scene_detect')

    log_state("start: is_consecutive")

    video1_end = video1[:-4] + ''.join(
        random.choices(string.ascii_letters + string.digits, k=16)) + '.mp4'
    video2_start = video2[:-4] + ''.join(
        random.choices(string.ascii_letters + string.digits, k=16)) + '.mp4'
    merged_result = video1[:-4] + ''.join(
        random.choices(string.ascii_letters + string.digits, k=16)) + '.mp4'
    duration = "0.2"

    log_state("start: is_consecutive", video1_end, video2_start, merged_result)
    command = ["ffmpeg", "-sseof", f"-{duration}", "-i", video1, "-c", "copy", video1_end]
    log_state("", command)
    subprocess.run(command)

    log_state("start: second video", video1_end, video2_start, merged_result)

    command = ["ffmpeg", "-t", f"{duration}", "-i", video2, "-c", "copy", video2_start]
    log_state("", command)
    subprocess.run(command)

    log_state("start: merge_videos")

    merge_videos([video1_end, video2_start], merged_result)

    log_state("start: ok")

    scenes = scene_detect(merged_result, split=False)
    remove_file(video1_end)
    remove_file(video2_start)
    remove_file(merged_result)
    return len(scenes) < 2
