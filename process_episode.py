import glob

from functions.dynamic_import import dynamic_import
from functions.logging import log_state


def process_episode(request):
    create_groups = dynamic_import('create_groups')
    download_urls = dynamic_import('download_urls')
    get_clips_urls = dynamic_import('get_clips_urls')
    merge_groups = dynamic_import('merge_groups')
    remove_file = dynamic_import('remove_file')
    save_to_drive = dynamic_import('save_to_drive')
    split_to_atomic = dynamic_import('split_to_atomic')

    clips = glob.glob('*.mp4')
    for clip in clips:
        remove_file(clip)

    # return 'test 19999942'
    print('#########>> start process_episode')

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
    count = download_urls(urls[7:11], seed)
    # count = 4

    clips = [seed + str(i) + '.mp4' for i in range(count)]
    print('#########>> clips: ', clips)
    print('#########>> start: split_to_atomic')
    atomic_clips = split_to_atomic(clips, seed)

    x = 17
    my_var = "testss"
    log_state("test",x, my_var )

    print('#########>> atomic_clips : ', atomic_clips)
    print('#########>> start: create_groups')
    groups = create_groups(atomic_clips)

    print("#########>> .mp4 : ")
    print(glob.glob('*.mp4'))
    print("#########>> all files : ")
    print(glob.glob('*'))

    print('#########>> groups : ', groups)
    print('#########>> start: merge_groups')
    good_clips = merge_groups(groups, seed)

    print("#########>> .mp4 : ")
    print(glob.glob('*.mp4'))
    print("#########>> all files : ")
    print(glob.glob('*'))

    print('#########>> start: save_to_drive')
    print('#########>> start: save_to_drive')
    print('#########>> start: save_to_drive')
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
