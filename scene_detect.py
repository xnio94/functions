from scenedetect import detect, split_video_ffmpeg, AdaptiveDetector


def scene_detect(video, split=True, detector=None, seed=''):
    if detector is None:
        detector = AdaptiveDetector(min_scene_len=4)
    scene_list = detect(video, detector, show_progress=True)
    if split:
        split_video_ffmpeg(
            video,
            scene_list,
            output_file_template=seed + '$VIDEO_NAME-$SCENE_NUMBER.mp4',
        )
    return scene_list
