FILE=$1
ffmpeg -i videos/$FILE -r 1 -t 20 images/image-%04d.tiff
