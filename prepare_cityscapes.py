import os
import glob
from PIL import Image


def load_resized_img(path):
    return Image.open(path).convert('RGB').resize((512, 256))


def process_cityscapes(leftImg8bit_dir, output_dir, phase):
    save_phase = 'test' if phase == 'val' else 'train'
    savedir = os.path.join(output_dir, save_phase)
    os.makedirs(savedir + 'B', exist_ok=True)
    print("Directory structure prepared at %s" % output_dir)

    photo_expr = os.path.join(leftImg8bit_dir, phase) + "/*/*_leftImg8bit.png"
    photo_paths = glob.glob(photo_expr)
    photo_paths = sorted(photo_paths)

    for i, photo_path in enumerate(photo_paths):
        photo = load_resized_img(photo_path)
        savepath = os.path.join(savedir + 'B', "%d_B.jpg" % i)
        photo.save(savepath, format='JPEG', subsampling=0, quality=100)

        if i % (len(photo_paths) // 10) == 0:
            print("%d / %d: last image saved at %s, " % (i, len(photo_paths), savepath))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--cityscapes_extra', type=str, required=True,
                        default='./datasets/cityscapes_extra/leftImg8bit',
                        help='Path to the Cityscapes leftImg8bit_trainextra directory.')
    parser.add_argument('--cityscapes_fine', type=str, required=True,
                        default='./datasets/cityscapes_fine/leftImg8bit',
                        help='Path to the Cityscapes leftImg8bit_trainvaltest directory.')
    parser.add_argument('--output_dir', type=str, required=True,
                        default='./datasets/gtav2cityscapes',
                        help='Directory the output images will be written to.')
    opt = parser.parse_args()

    print('Preparing Cityscapes Dataset for test phase')
    process_cityscapes(opt.cityscapes_fine, opt.output_dir, "val")
    print('Preparing Cityscapes Dataset for train phase')
    process_cityscapes(opt.cityscapes_extra, opt.output_dir, "train")

    print('Done')
