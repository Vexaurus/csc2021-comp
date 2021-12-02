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
        makedirs(f'{URL_START}/{img_ind}.gif')

        for i in range(img.n_frames):
            img.seek(i)
            img.save(f'{URL_START}/{img_ind}/{i:0>3}.gif')



if __name__ == '__main__':
    # URL = 'http://lost_in_the_discolights.ctf.fifthdoma.in/disco'
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     for i in track(range(57)):
    #         executor.submit(pull_imgs, f'{URL}{i}.gif', './disco', i)

    # for image in range(len(listdir('./disco'))):
    #     split_frames(image)
    
    counts_w = 0
    counts_b = 0    
    for frame in sorted(listdir(f'{URL_START}/{1}')):
        with Image.open(f'{URL_START}/{1}/{frame}') as img:
            print(img.getcolors())
            # if img.convert("L").getextrema() == (255, 255):
            #     counts_w += 1
            # else:
            #     counts_b += 1

    print(counts_b, counts_w)

