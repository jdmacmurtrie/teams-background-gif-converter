import os
import shutil

root = '/Users/<username>'
# origin_path is wherever you store your gifs once you download them.
# I recommend having a dedicated folder, as the script affects all files in the folder
origin_path = f'{root}/<folder where you download your gifs>' 
for folder,sub_folders,files in os.walk(origin_path):
    for f in files:
        if f[0] == '.':
            continue
        
        # shallow clone of original file
        main_pic = f[:]
        thumbnail = f[:]

        # get the extension of the file
        ext_index = f.index('.')
        file_ext = f[(ext_index):]

        # change the extension, create a thumbnail file
        # Teams will recognize the _thumb.png automatically
        file_name_with_png_ext = main_pic.replace(file_ext, '.png')
        file_thumb_name_with_png_ext = thumbnail.replace(file_ext, '_thumb.png')

        # copy both files with changed extensions
        new_background_file = shutil.copy(f'{origin_path}/{f}', f'{origin_path}/{file_name_with_png_ext}')
        new_thumbnail_file = shutil.copy(f'{origin_path}/{f}', f'{origin_path}/{file_thumb_name_with_png_ext}')

        # move both copied files
        shutil.move(new_background_file, f'{root}/Library/Application Support/Microsoft/Teams/Backgrounds/Uploads')
        shutil.move(new_thumbnail_file, f'{root}/Library/Application Support/Microsoft/Teams/Backgrounds/Uploads')

        # delete the original
        os.remove(f'{origin_path}/{f}')

