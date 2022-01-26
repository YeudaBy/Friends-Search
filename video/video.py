from typing import Union
import os.path
from moviepy.editor import VideoFileClip
from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip


def get_video_clip(season: int, episode: int, sentence_id: int, start: str, end: str) -> Union[str, bool]:
    video_file = f"./files/originals/s{season}/e{episode}.mkv"
    print(os.path.abspath("."))
    print(video_file)
    if os.path.isfile(video_file):
        # TODO Up and down 3 (?) seconds from start&end
        clip = VideoFileClip(video_file).subclip(start, end)
        logo = (ImageClip("friends-logo-base.png")
                .set_duration(clip.duration)
                .resize(height=80)  # if you need to resize...
                .margin(right=8, top=8, opacity=0)  # (optional) logo-border padding
                .set_pos(("right", "top")))
        final = CompositeVideoClip([clip, logo])
        clip_file = f"files/tmp/{sentence_id}.mp4"
        final.write_videofile(clip_file)
        if os.path.isfile(clip_file):
            return clip_file
    return False


print(get_video_clip(3, 7, 123, "0:00:02.836000", "0:00:05.045000"))
