import glob

from functions.merge_videos import merge_videos


def merge_groups(groups, seed):
    good_count = 0
    for group in groups:
        group_name = seed + f'good_{good_count}.mp4'
        merge_videos(group, group_name)
        good_count = good_count + 1

    good_clips = glob.glob(seed + 'good_*.mp4')
    return good_clips
