from functions.dynamic_import import dynamic_import


def is_same_video(video1, video2):
    is_consecutive = dynamic_import('is_consecutive')
    return is_consecutive(video1, video2)
