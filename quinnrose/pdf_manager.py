import pdfkit

class PDFGenerator(object):
    
    options = {
        'quiet': ''
    }
    def get_pdf(self, from_url):
        
        retval = pdfkit.from_url(from_url, False, options=self.options)
    
        return retval
    
if __name__ == '__main__':
    
    pg = PDFGenerator()

    pdf = pg.get_pdf('http://127.0.0.1:8080/privacy')
    print(pdf)
    