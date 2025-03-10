import os
import sys
from PIL import Image
from colorama import Fore, Back, Style, init

init(autoreset=True)

ascii_title = """
  ██▓ ▄████▄   ██▓    ▓█████ ▄▄▄      ███▄    █  ▓█████ ██▀███  
▒▓██▒▒██▀ ▀█  ▓██▒    ▓█   ▀▒████▄    ██ ▀█   █  ▓█   ▀▓██ ▒ ██▒
▒▒██▒▒▓█    ▄ ▒██░    ▒███  ▒██  ▀█▄ ▓██  ▀█ ██▒ ▒███  ▓██ ░▄█ ▒
░░██░▒▓▓▄ ▄██ ▒██░    ▒▓█  ▄░██▄▄▄▄██▓██▒  ▐▌██▒ ▒▓█  ▄▒██▀▀█▄  
░░██░▒ ▓███▀ ▒░██████▒░▒████▒▓█   ▓██▒██░   ▓██░▒░▒████░██▓ ▒██▒
 ░▓  ░ ░▒ ▒  ░░ ▒░▓  ░░░ ▒░ ░▒▒   ▓▒█░ ▒░   ▒ ▒ ░░░ ▒░ ░ ▒▓ ░▒▓░
░ ▒ ░  ░  ▒  ░░ ░ ▒  ░ ░ ░  ░ ░   ▒▒ ░ ░░   ░ ▒░░ ░ ░    ░▒ ░ ▒ 
░ ▒ ░░          ░ ░      ░    ░   ▒     ░   ░ ░     ░    ░░   ░ 
  ░  ░ ░     ░    ░  ░   ░        ░           ░ ░   ░     ░     
"""

print(Fore.BLUE + ascii_title + Style.RESET_ALL)
print(f"{Fore.BLUE}{Style.BRIGHT}[AUTHOR] {Fore.WHITE}Kap0ne{Style.RESET_ALL}\n")
print(f"{Fore.BLUE}{Style.BRIGHT}[INFO] {Fore.WHITE}Welcome to iCleaner, an extremely simple Python script to remove EXIF metadata from image files.{Style.RESET_ALL}\n")
print(f"{Fore.BLUE}{Style.BRIGHT}[USAGE] {Fore.WHITE}python iCleaner.py <input_folder or image_file> <output_folder>{Style.RESET_ALL}\n")

def create_output_folder(func):
    def wrapper(*args, **kwargs):
        output_folder = kwargs.get("output_folder")
        if output_folder is None:
            input_path = args[0]
            if os.path.isfile(input_path):
                base_dir = os.path.dirname(input_path)
                name = os.path.splitext(os.path.basename(input_path))[0]
                output_folder = os.path.join(base_dir, f"{name}_cleaned")
            else:
                output_folder = f"{input_path}_cleaned"
            os.makedirs(output_folder, exist_ok=True)
            kwargs["output_folder"] = output_folder
        return func(*args, **kwargs)
    return wrapper

@create_output_folder
def clean_image_metadata(image_path, output_folder):
    try:
        with Image.open(image_path) as img:
            img_without_exif = Image.new(img.mode, img.size)
            img_without_exif.putdata(list(img.getdata()))
            filename = os.path.basename(image_path)
            output_path = os.path.join(output_folder, filename)
            img_without_exif.save(output_path)
            print(f"{Fore.GREEN}{Style.BRIGHT}[SUCCESS] {Fore.WHITE}Cleaned metadata from '{image_path}' and saved to '{output_path}'!{Style.RESET_ALL}\n")
    except Exception as e:
        print(f"{Fore.RED}{Style.BRIGHT}[ERROR] {Fore.WHITE}Failed to process '{image_path}'! Additional information: {e}{Style.RESET_ALL}\n")

def process_folder(input_folder, output_folder):
    supported_extensions = (".jpg", ".jpeg", ".png")
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(supported_extensions):
            image_path = os.path.join(input_folder, filename)
            clean_image_metadata(image_path, output_folder=output_folder)

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(f"{Fore.RED}{Style.BRIGHT}[ERROR] {Fore.WHITE}Invalid number of arguments!{Style.RESET_ALL}\n")
        sys.exit(1)
    input_path = sys.argv[1]
    print(f"{Fore.BLUE}{Style.BRIGHT}[INFO] {Fore.WHITE}Processing {input_path}{Style.RESET_ALL}...\n")
    if len(sys.argv) == 2:
        if os.path.isdir(input_path):
            for filename in os.listdir(input_path):
                if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                    image_path = os.path.join(input_path, filename)
                    clean_image_metadata(image_path)
        elif os.path.isfile(input_path):
            clean_image_metadata(input_path)
        else:
            print(f"{Fore.RED}{Style.BRIGHT}[ERROR] {Fore.WHITE}'{input_path}' is not a valid file or directory!{Style.RESET_ALL}\n")
            sys.exit(1)
    else:
        output_folder = sys.argv[2]
        if os.path.isdir(input_path):
            process_folder(input_path, output_folder)
        elif os.path.isfile(input_path):
            clean_image_metadata(input_path, output_folder=output_folder)
        else:
            print(f"{Fore.RED}{Style.BRIGHT}[ERROR] {Fore.WHITE}'{input_path}' is not a valid file or directory!{Style.RESET_ALL}\n")
            sys.exit(1)

if __name__ == '__main__':
    main()
