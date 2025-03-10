# iCleaner:
An extremely simple Python script to remove EXIF metadata from image files. I saw other scripts similar to this so I decided to create my own implementation. This script uses the Pillow library to process images, removing any embedded EXIF data and saving the cleaned images to a new folder.

---

### Features:
- **Metadata Removal**: Strips out EXIF data from .JPG, .JPEG, and .PNG files.
- **Dynamic Output Folder:** Automatically creates an output folder based on the input file or directory.
- **Batch Processing:** Supports cleaning a single image file or all images in a specified directory.
- **Error Handling:** Handles errors during processing so that one bad file doesn’t interrupt the entire process.

#

### Requirements:
- Python 3.x
- [Pillow](https://python-pillow.org/)
- [Colorama](https://pypi.org/project/colorama/)

#

### Installation:
**Step 1:** Clone the repository:
   ```bash
   git clone https://github.com/kap0nedotexe/iCleaner.git
   cd iCleaner
   ```
**Step 2:** Install required dependencies (if needed):
   ```python3
   pip3 install Pillow
   pip3 install colorama
   ```

#

### Usage:
#### **Example for a single image file:**
   ```python3
   python3 iCleaner.py <image_file>
   ```
If no output folder is provided, the script creates one named '<image_name>_cleaned' in the same directory as the image.
#### **Example for a folder of images:**
   ```python3
   python3 iCleaner.py <input_folder> <output_folder>
   ```
The script will process all .JPG, .JPEG, and .PNG files in the input folder and save the cleaned images to the specified output folder.
