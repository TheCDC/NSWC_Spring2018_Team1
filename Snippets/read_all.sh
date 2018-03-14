OUTFILE=output/tesseract-batch-output.txt
> $OUTFILE; for file in `ls images/*.tiff`; do  echo $file >> $OUTFILE; python3.6 ocr.py --quiet --image $file | grep '[A-Z]\{3\}[0-9]\{2\}[A-Z]\{1\}[0-9]\{3\}-[0-9]\{3\}' >> $OUTFILE; done
