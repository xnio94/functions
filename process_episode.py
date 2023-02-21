import glob
import subprocess
from importlib import import_module

from functions.create_groups import create_groups
from functions.donwload_urls import download_urls
from functions.get_clips_urls import get_clips_urls
from functions.merge_groups import merge_groups
from functions.remove_file import remove_file
from functions.save_to_drive import save_to_drive
from functions.split_to_atmic import split_to_atomic


def process_episode(request):
    tmp_functions = 'tmp_functions'  # 'a' + str(random.random())[5:10]
    mod = import_module(tmp_functions + '.create_groups')
    create_groups = getattr(mod, 'create_groups')


    # return 'test 19999942'
    print('#########>> start')
    command = "ffmpeg"
    x = subprocess.run(command, shell=True)
    # return str(x)

    #
    # request_args = request.args
    # if request_args and 'link' in request_args:
    #     link = request_args['link']
    """
    #################################
    """
    seed = 'seed_'
    episode_link = 'https://story.snapchat.com/p/52b2897c-ea49-4659-9ccd-9e9db12ccb57/1866136369958912'
    # episode_link  = 'https://story.snapchat.com/p/52b2897c-ea49-4659-9ccd-9e9db12ccb57/2548934642860032'
    print('#########>> start: get_title_urls')
    title, urls = get_clips_urls(episode_link)
    print(urls[0:3])
    print('#########>> start: download_urls')
    count = download_urls(urls[7:10], seed)
    # count = 4
    print("#########>> .mp4 : ")
    print(glob.glob('*.mp4'))
    print("#########>> all files : ")
    print(glob.glob('*'))

    clips = [seed + str(i) + '.mp4' for i in range(count)]
    print('#########>> clips: ', clips)
    print('#########>> start: split_to_atomic')
    atomic_clips = split_to_atomic(clips, seed)

    print("#########>> .mp4 : ")
    print(glob.glob('*.mp4'))
    print("#########>> all files : ")
    print(glob.glob('*'))

    print('#########>> atomic_clips : ', atomic_clips)
    print('#########>> start: create_groups3')
    try:
        groups = create_groups(atomic_clips)
        print('no problem')
    except Exception as ex:
        print('problem')
        print(ex)

    print("#########>> .mp4 : ")
    print(glob.glob('*.mp4'))
    print("#########>> all files : ")
    print(glob.glob('*'))

    print('test2')
    try:
        com = ["ffmpeg", "-sseof", "0.2", "-i", "seed_0.mp4", "-c", "copy", "out.mp4"]
        # com = "ffmpeg -sseof 0.2 -i seed_0.mp4 -c copy out.mp4"
        subprocess.run(com)
    except Exception as ex:
        print('problem')
        print(ex)

    print('test4')
    try:
        command = ["ffmpeg", "-i", "seed_0.mp4", "-c", "copy", "out.mp4"]
        subprocess.run(command, check=True)
    except Exception as ex:
        print('problem')
        print(ex)

    print("#########>> .mp4 : ")
    print(glob.glob('*.mp4'))
    print("#########>> all files : ")
    print(glob.glob('*'))

    return 'done'

    print('#########>> groups : ', groups)
    print('#########>> start: merge_groups')
    good_clips = merge_groups(groups, seed)

    print("#########>> .mp4 : ")
    print(glob.glob('*.mp4'))
    print("#########>> all files : ")
    print(glob.glob('*'))

    print('#########>> start: save_to_drive')
    for clip in good_clips:
        save_to_drive(clip)

    print('#########>> start: remove')
    # remove all atomic clips
    for clip in good_clips:
        remove_file(clip)
    for clip in atomic_clips:
        remove_file(clip)
    for clip in clips:
        remove_file(clip)
    return f'Hello'
