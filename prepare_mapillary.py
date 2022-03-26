import os
import glob
from PIL import Image


def load_resized_img(path):
    baseheight = 256
    img = Image.open(path).convert('RGB')

    # crop to reduce sky volume (height=width/2)
    if img.size[1] > img.size[0]/2:
        # img = img.crop((left, top, right, bottom))
        img = img.crop((0, img.size[1] - img.size[0]/2, img.size[0], img.size[1]))
        # resize
        hpercent = (baseheight / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, baseheight))

    return img


def process_mapillary(images_dir, output_dir, phase):
    save_phase = 'test' if phase == 'validation' else 'train'
    savedir = os.path.join(output_dir, save_phase)
    os.makedirs(savedir + 'B', exist_ok=True)
    print("Directory structure prepared at %s" % output_dir)

    photo_expr = os.path.join(images_dir, phase) + "/images/*.jpg"
    photo_paths = glob.glob(photo_expr)
    photo_paths = sorted(photo_paths)

    for i, photo_path in enumerate(photo_paths):
        photo = load_resized_img(photo_path)
        savepath = os.path.join(savedir + 'B', "%d_b.jpg" % i)
        photo.save(savepath, format='JPEG', subsampling=0, quality=100)

        if i % (len(photo_paths) // 10) == 0:
            print("%d / %d: last image saved at %s, " % (i, len(photo_paths), savepath))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--images_dir', type=str, required=True,
                        default='./datasets/mapillary',
                        help='Path to the Mapillary trainvaltest directory.')
    parser.add_argument('--output_dir', type=str, required=True,
                        default='./datasets/gtav2mapillary',
                        help='Directory the output images will be written to.')
    opt = parser.parse_args()

    print('Preparing Mapillary Vistas Dataset for test phase')
    process_mapillary(opt.images_dir, opt.output_dir, "validation")
    print('Preparing Mapillary Vistas Dataset for train phase')
    process_mapillary(opt.images_dir, opt.output_dir, "training")

    print('Done')
