> output.txt; for file in `ls images/*.tiff`; do  echo $file | tee output.txt --append; python ocr.py --quiet --image $file | tee output.txt --append; done