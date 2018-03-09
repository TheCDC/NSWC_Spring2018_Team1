FILE=$1
ffmpeg -i $FILE -r 1 images/image-%04d.tiff