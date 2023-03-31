import rawpy
import imageio

path = 'DSC02878.ARW'
with rawpy.imread(path) as raw:
    rgb = raw.postprocess()
imageio.imsave('1.tiff', rgb)
with rawpy.imread(path) as raw:
    # raises rawpy.LibRawNoThumbnailError if thumbnail missing
    # raises rawpy.LibRawUnsupportedThumbnailError if unsupported format
    thumb = raw.extract_thumb()
if thumb.format == rawpy.ThumbFormat.JPEG:
    # thumb.data is already in JPEG format, save as-is
    with open('1.jpeg', 'wb') as f:
        f.write(thumb.data)
elif thumb.format == rawpy.ThumbFormat.BITMAP:
    # thumb.data is an RGB numpy array, convert with imageio
    imageio.imsave('1.jpeg', thumb.data)