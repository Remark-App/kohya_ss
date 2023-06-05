import requests
import argparse
import os


def parse_args(input_args=None):
    parser = argparse.ArgumentParser(description="downloads images from urls")
    parser.add_argument(
        "--dir",
        type=str,
        default=None,
        required=True,
        help="Path to save output images",
    )
    parser.add_argument(
        "--images",
        type=str,
        default=None,
        required=True,
        action='append',
        help="List of images to download",
    )
    return parser.parse_args(input_args)


if __name__ == "__main__":
    args = parse_args()
    path = args.dir
    if path[-1] != '/':
        path += '/'
    os.makedirs(path)
    i = 0
    for image in args.images:
        try:
            r = requests.get(image, timeout=3)
            if not r.headers['Content-Type'].startswith('image'):
                continue
            # get image format
            image_format = r.headers['Content-Type'].split('/')[-1]

            with open(path + f"{i}.{image_format}", "wb") as f:
                f.write(r.content)
            i += 1
        except:
            pass
