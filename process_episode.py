import glob
import subprocess
import urllib

from flask import send_file

from functions.dynamic_import import dynamic_import


def process_episode(request):
    #
    # Cors section start
    #
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    #
    # Cors section end
    #
    log_state = dynamic_import('log_state')
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

    log_state("start: process_episode")
    #
    seed = '_'
    # episode_link = 'https://story.snapchat.com/p/52b2897c-ea49-4659-9ccd-9e9db12ccb57/1866136369958912'
    # episode_link  = 'https://story.snapchat.com/p/52b2897c-ea49-4659-9ccd-9e9db12ccb57/2548934642860032'

    request_args = request.args
    ############################################################
    ############################################################
    ############################################################
    ############################################################
    if request_args and 'anas' in request_args:
        anas_link = request_args['anas']
        urllib.request.urlretrieve(anas_link, 'filename')
        return (send_file('filename',
                         # as_attachment=True,
                         mimetype='image/jpeg',
                         ), 200, headers)
    ############################################################
    ############################################################
    ############################################################
    ############################################################


    if request_args and 'link' in request_args:
        episode_link = request_args['link']
    else:
        return ("fuck", 200, headers)



    log_state("start: get_title_urls", episode_link)

    title, urls = get_clips_urls(episode_link)
    print(urls[0:3])
    log_state("start: download_urls", urls[0:3])

    count = download_urls(urls, seed)
    # count = 4

    clips = [seed + str(i) + '.mp4' for i in range(count)]

    log_state("start: split_to_atomic", clips)

    atomic_clips = split_to_atomic(clips, seed)

    log_state("start: create_groups", atomic_clips)

    groups = create_groups(atomic_clips)

    log_state("start: merge_groups", groups)

    good_clips = merge_groups(groups, seed)

    log_state("start: save_to_drive", good_clips)

    for clip in good_clips:
        # cc = "ffmpeg -i output.mp4 -vf scale=1080:1920 -preset ultrafast -threads 4 -c:a copy output5.mp4"
        command = [
            "ffmpeg",
            "-i",
            clip,
            "-vf",
            "scale=1080:1920",
            "-preset",
            "ultrafast",
            "-threads",
            "4",
            "-c:a",
            "copy",
            'u' + clip
        ]
        x = subprocess.run(command)

    # good_clips = ['u' + clip for clip in good_clips]
    for clip in good_clips:
        save_to_drive('u' + clip, title)

    log_state("start: remove")

    # remove all atomic clips
    for clip in good_clips:
        remove_file(clip)
        remove_file('u' + clip)
    for clip in atomic_clips:
        remove_file(clip)
    for clip in clips:
        remove_file(clip)
    return ('ok', 200, headers)
