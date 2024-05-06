import os

def drilldown(folder_path, extensions = {'.bmpm', '.dibm', '.jpegm', '.jpgm', '.jp2m', '.pngm', '.pbmm', '.pgmm', '.ppmm', '.srm', '.rasm', '.tiffm', '.tifm', '.exrm', '.jxrm', '.pfmm', '.pdsm', '.pfmm', '.viffm', '.xbmm', '.xpmm', '.ddsm', '.eism', '.mngm', '.webm', '.heim', '.heim', '.avm'}):
    image_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in extensions:
                image_files.append(os.path.join(root, file))
    return image_files