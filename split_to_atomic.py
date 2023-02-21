import glob
import os
import shutil

from functions.get_duration import get_duration
from functions.remove_file import remove_file
from functions.scene_detect import scene_detect


def split_to_atomic(clips, seed):
    index = 0
    for clip in clips:
        # split the clip into atomic_clips
        scene_detect(clip, seed=seed)

        # renaming the atomic clips using global counter index
        atomic_clips = glob.glob(clip[:-4] + '-*.mp4')
        if atomic_clips:
            for atomic_clip in atomic_clips:
                duration = get_duration(atomic_clip)
                if duration > 8:
                    file_name = seed + f'atomic_clip_{index:05d}.mp4'
                    if os.path.exists(file_name):
                        os.remove(file_name)
                    os.rename(atomic_clip, file_name)
                    index=index+1
                else:
                    remove_file(atomic_clip)
        else:
            file_name = seed + f'atomic_clip_{index:05d}.mp4'
            if os.path.exists(file_name):
                os.remove(file_name)
            shutil.copyfile(clip, file_name)
            index=index+1
    #      
    # now we have index+1 atomic clips
    atomic_clips = glob.glob(seed + 'atomic_clip_*.mp4')
    return atomic_clips
