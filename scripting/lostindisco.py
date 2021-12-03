#!/usr/bin/env python3.10

import requests
import concurrent.futures
from rich.progress import track
from PIL import Image, ImageChops
from os import makedirs, listdir

URL_START = './disco'

def pull_imgs(url, tgt, i):
    with open(f'./{tgt}/{i}.gif', 'wb') as img_file:
        contents = requests.get(f'{url}').content
        img_file.write(contents)

def split_frames(img_ind):
    with Image.open(f'{URL_START}/img_{img_ind}.gif') as img:
        makedirs(f'{URL_START}/{img_ind}')

        for i in range(img.n_frames):
            img.seek(i)
            blk = img.convert('1')
            blk.save(f'{URL_START}/{img_ind}/{i:0>3}.gif')



if __name__ == '__main__':
    # URL = 'http://lost_in_the_discolights.ctf.fifthdoma.in/disco'
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     for i in track(range(57)):
    #         executor.submit(pull_imgs, f'{URL}{i}.gif', './disco', i)

    # for image in range(len(listdir('./disco'))):
    #     split_frames(image)
    
    # split_frames(f'{1}')

    frames = []
    for i in range(56):
        binary = []
        for frame in sorted(listdir(f'{URL_START}/{i}')):
            with Image.open(f'{URL_START}/{i}/{frame}') as img:
                if img.getcolors()[0] == (64, 255):
                    binary.append('0')
                else:
                    binary.append('1')
        print(''.join(binary))
    