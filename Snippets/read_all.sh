OUTFILE=output/tesseract-batch-output.txt
> $OUTFILE; for file in `ls images/*.tiff`; do  echo $file | tee $OUTFILE --append; python ocr.py --quiet --image $file | tee $OUTFILE --append; done
