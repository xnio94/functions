from functions.is_same_video import is_same_video


def create_groups(atomic_clips, logs=False):
    print("new groups 42")
    # create groups
    groups = []
    group = [atomic_clips[0]]
    for clip in atomic_clips[1:]:
        last_clip = group[-1]
        if is_same_video(last_clip, clip):
            if logs:
                print('true')
            group.append(clip)
        else:
            groups.append(group)
            group = [clip]
        if logs:
            print(clip)
            print(group)
            print(groups)
            print('####')
    groups.append(group)
    return groups
