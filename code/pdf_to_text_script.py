import logging
import sys

from PIL import Image
import pytesseract
from pdf2image import convert_from_path



logging.basicConfig(level=logging.INFO)




def main(argv):

    logging.info("\n Retrieving Pages")
    pages = convert_from_path('../primary_datasets/Williamstown_policing/Logs2019.pdf', 
                            dpi=300)

    logging.info("\n {} Pages Retrieved".format(len(pages)))


    n = 1
    for page in pages:
        
        # Write pdf to image file.
        img_file = '../data/pdf_to_jpg/out_{}.jpg'.format(n)
        page.save(img_file.format(n),"JPEG")
        
        
        # Write image file to text file.
        text_file = open('../data/Logs2019/page_{}.txt'.format(n), 'a')
        text=str(pytesseract.image_to_string(Image.open(img_file),lang='eng'))
        text=text.replace("\n","")

        text_file.write(text)
        text_file.close()

        n = n+1


if __name__ == "__main__":
    main(sys.argv[1:])
