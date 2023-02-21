import cv2


def get_duration(filename):
    video = cv2.VideoCapture(filename)
    duration = video.get(cv2.CAP_PROP_POS_MSEC)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    return frame_count