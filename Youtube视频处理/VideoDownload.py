"""
@author:Wang Xinsheng
@File:VideoDownload.py
@description:...
@time:2021-03-21 13:22
"""
from constant import *
from you_get import common as you_get
import os
from moviepy.editor import *

def download(url):
    out_dir = r'./Videos'
    you_get.any_download(url=url,output_dir=out_dir,merge=True,itag=160)




def get_info(url):
    '''
    显示资源信息
    :param utl:
    :return:
    '''
    os.system('you-get -i {}'.format(url))


def mp4Tomp3(vido_path,outdir):
    '''
    将视频转换为mp3
    :param vido_path:
    :param outdir:
    :return:
    '''
    video = VideoFileClip(vido_path)
    audio = video.audio
    audio.write_audiofile(outdir)



if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=PNyfdl7vwBI'
    # get_info(url)
    download(url)
    # mp4Tomp3('./Videos/木吉他.mp4',outdir='./Videos/木吉他.mp3'.format(out_dir))