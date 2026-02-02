from pathlib import Path
from PIL import Image

imoldpath = Path.home() / "images"  #create a path object for where the old images are originally stored
imnewpath = Path("/opt/icons")      #create a path object to store the new manipulated images

imnewpath.mkdir(parents=True, exist_ok=True)    #make sure the folder exists

for im in imoldpath.iterdir():
    if im.is_file() and not im.name.startswith("."):
        #use try except block to avoid any hidden files 
        try:
            newim_path = imnewpath / im.with_suffix(".jpeg").name   #change extension to jpeg
            with Image.open(im) as img:
                finalimage = img.convert("RGB").rotate(90).resize((128,128))    #convert image to RGB for jpeg, rotate and resize
                finalimage.save(newim_path, "JPEG")     #save the new image
        except Exception as e:
            print(f"Could not process {im.name}: {e}")