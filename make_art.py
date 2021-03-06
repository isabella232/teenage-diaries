#!/usr/bin/env python

from glob import glob
import os
from shutil import rmtree

from PIL import Image

output_dir = 'www/img/profiles'
widths = [300, 480, 980]

rmtree(output_dir)
os.mkdir(output_dir)

for path in glob('profiles/*'):
    filename = os.path.split(path)[-1]
    name = os.path.splitext(filename)[0]

    original = Image.open(path)

    if original.mode == 'LA':
        original = original.convert('L')

    for width in widths:
        output_path = os.path.join(output_dir, '%s_%i.jpg' % (name, width)) 

        width_pct = width / float(original.size[0])
        height = int(float(original.size[1] * width_pct))

        print 'Cutting %s at %ix%i' % (name, width, height)
        img = original.resize((width, height), Image.ANTIALIAS)
        img.save(output_path)
