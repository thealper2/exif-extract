import colorama
from colorama import Fore, Back, Style
from PIL import Image
from PIL.ExifTags import TAGS
import argparse

colorama.init(autoreset=True)

def metadata(image_file):
	image = Image.open(image_file)
	info_dict = {
		"Filename": image.filename,
		"Image Size": image.size,
		"Image Height": image.height,
		"Image Format": image.format,
		"Image Mode": image.mode,
		"Image is Animated": getattr(image, "is_animated", False),
		"Frames in Image": getattr(image, "n_frames", 1)
	}
	exifdata = image.getexif()
	for tag_id in exifdata:
		tag = TAGS.get(tag_id, tag_id)
		data = exifdata.get(tag_id)
		if isinstance(data, bytes):
			data = data.decode()
		info_dict[tag] = data

	for key, value in info_dict.items():
		print(f"[+] {Fore.GREEN}{key}{Fore.RESET} : {Fore.YELLOW}{value}{Fore.RESET}")

argument_parser = argparse.ArgumentParser(description='')
argument_parser.add_argument('--image', help='')
args = argument_parser.parse_args()

metadata(args.image)

