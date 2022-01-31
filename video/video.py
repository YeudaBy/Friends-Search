from typing import Union
import os.path
from moviepy.editor import VideoFileClip
from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

# original_files_path = "/root/downloads/Friends.Complete.Series.720p.BluRay.2CH.x265.HEVC-PSA"
original_files_path = "/home/david/Documents/PythonProjects/Friends-Sentences/video/files/originals"
edited_videos_files_path = "/home/david/Documents/PythonProjects/Friends-Sentences/video/files/tmp/videos"
edited_images_files_path = "/home/david/Documents/PythonProjects/Friends-Sentences/video/files/tmp/images"
friends_logo_path = "/home/david/Documents/PythonProjects/Friends-Sentences/video/friends-logo-base.png"


def get_video_clip(season: int, episode: int, sentence_id: int, start: str, end: str) -> Union[str, bool]:
    season = f"0{season}" if len(str(season)) == 1 else season
    episode = f"0{episode}" if len(str(episode)) == 1 else episode
    video_file = f"{original_files_path}/S{season}/S{season}E{episode}.mkv"
    clip_file = f"{edited_videos_files_path}/{sentence_id}.mp4"
    if os.path.isfile(clip_file):
        return clip_file
    elif os.path.isfile(video_file):
        # TODO Up and down 3 (?) seconds from start&end
        clip = VideoFileClip(video_file).subclip(start, end)
        logo = (ImageClip("friends-logo-base.png")
                .set_duration(clip.duration)
                .resize(height=80)  # if you need to resize...
                .margin(right=8, top=8, opacity=0)  # (optional) logo-border padding
                .set_pos(("right", "top")))
        final = CompositeVideoClip([clip, logo])
        final.write_videofile(clip_file)
        if os.path.isfile(clip_file):
            return clip_file
    return False


print(get_video_clip(5, 16, 123, "20:50", "21:05"))


def get_video_img(season: int, episode: int, sentence_id: int, start: str, end: str):
    season = f"0{season}" if len(str(season)) == 1 else season
    episode = f"0{episode}" if len(str(episode)) == 1 else episode
    video_file = f"{original_files_path}/S{season}/S{season}E{episode}.mkv"
    img_file = f"{edited_images_files_path}/{sentence_id}.png"
    if os.path.isfile(img_file):
        return img_file
    video = VideoFileClip(video_file)
    logo = (ImageClip("friends-logo-base.png")
            .set_duration(video.duration)
            .resize(height=80)  # if you need to resize...
            .margin(right=8, top=8, opacity=0)  # (optional) logo-border padding
            .set_pos(("right", "top")))
    final = CompositeVideoClip([video, logo])
    final.save_frame(img_file, t=start)
    if os.path.isfile(img_file):
        return img_file
    return False


print(get_video_img(5, 16, 123, "20:50", "21:05"))
