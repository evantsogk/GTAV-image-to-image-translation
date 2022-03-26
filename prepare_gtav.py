import os
import glob
from pathlib import Path
import scipy.io
from PIL import Image


def load_resized_img(path):
    return Image.open(path).convert('RGB').resize((468, 256))


def process_gtav(images_dir, output_dir, split):
    test_ids = set(list(scipy.io.loadmat(split)['testIds'].flatten()))
    savedir_train = os.path.join(output_dir, "train")
    savedir_test = os.path.join(output_dir, "test")
    os.makedirs(savedir_train + 'A', exist_ok=True)
    os.makedirs(savedir_test + 'A', exist_ok=True)
    print("Directory structure prepared at %s" % output_dir)

    photo_expr = os.path.join(images_dir) + "/*.png"
    photo_paths = glob.glob(photo_expr)
    photo_paths = sorted(photo_paths)

    for i, photo_path in enumerate(photo_paths):
        photo = load_resized_img(photo_path)
        photo_id = int(Path(photo_path).stem)

        if photo_id in test_ids:
            savepath = os.path.join(savedir_test + 'A', "%d_A.jpg" % i)
        else:
            savepath = os.path.join(savedir_train + 'A', "%d_A.jpg" % i)

        photo.save(savepath, format='JPEG', subsampling=0, quality=100)

        if i % (len(photo_paths) // 10) == 0:
            print("%d / %d: last image saved at %s, " % (i, len(photo_paths), savepath))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--images_dir', type=str, required=True,
                        default='./datasets/gtav/images',
                        help='Path to the GTA V images directory.')
    parser.add_argument('--split', type=str, required=True,
                        default='./datasets/split.mat',
                        help='Path to GTA V split.mat.')
    parser.add_argument('--output_dir', type=str, required=True,
                        default='./datasets/gtav2cityscapes',
                        help='Directory the output images will be written to.')
    opt = parser.parse_args()

    print('Preparing GTA V Dataset')
    process_gtav(opt.images_dir, opt.output_dir, opt.split)

    print('Done')
