import io, os, sys
from docxtpl import DocxTemplate
from subprocess import  Popen
from django.http import HttpResponse, StreamingHttpResponse,FileResponse
import tempfile

class StreamingConvertedPdf:

    def __init__(self, dock_obj, download=True):
        self.doc = dock_obj
        print("yg masuk", self.doc)
        self.download = download
        self.tmp_path = "/Users/pipeline-dev/"

    def validate_document(self):
        if not self.doc.name.split('.')[-1] in ('doc', 'docm', 'docx'):
            raise Exception('The input file must have one format from this: doc, docm, docx')

    def check_tmp_folder(self):
        if not os.path.exists(self.tmp_path):
            os.makedirs(self.tmp_path)

    def convert_to_pdf(self):
        self.validate_document()
        self.check_tmp_folder()
        with tempfile.NamedTemporaryFile(prefix=self.tmp_path, delete=False) as tmp:
            tmp.write(self.doc.read())

            print("Name:"+tmp.name)
            print("PAth TMP:"+self.tmp_path)

            try:
                with open(tmp.name):
                    print('file_existttt')
            except Exception:
                print('nooooott_existttt')
            if os.name == 'nt':
                process = Popen(['C:\\Program Files\\LibreOffice\\program\\soffice', '--convert-to', 'pdf', tmp.name, '--outdir', self.tmp_path])
                process.wait()

            elif sys.platform == 'darwin':
                print("darwin")
                process = Popen(['/Applications/LibreOffice.app/Contents/MacOS/soffice', '--convert-to', 'pdf', tmp.name, '--outdir', self.tmp_path])
                process.wait()

            else:
                process = Popen(['soffice', '--convert-to', 'pdf', tmp.name, '--outdir', self.tmp_path])
                process.wait()
            self.tmp_path = tmp.name + '.pdf'

    def get_file_name(self):
        return self.doc.name.split('.')[0] + '.pdf'

    def stream_content(self):
        self.convert_to_pdf()
        response = StreamingHttpResponse(open(self.tmp_path, 'rb'), content_type='application/pdf')
        return response
    
    def file_content(self):
        self.convert_to_pdf()
        res = open(self.tmp_path, 'rb')
        return res

    def __del__(self):
        try:
            if os.path.exists(self.tmp_path):
                os.remove(self.tmp_path)
        except IOError:
            print('Error deleting file')


class borangRenderer:
    def __init__(self, directory_borang, content_borang):
        self.directory_borang = directory_borang
        self.content_borang = content_borang 

    def cetak(self):
        doc = DocxTemplate(self.directory_borang)
        doc.render(self.content_borang, autoescape=True)

        doc_io = io.BytesIO() # create a file-like object
        doc.save(doc_io) # save data to file-like object
        doc_io.seek(0) # go to the beginning of the file-like object
        doc_io.name = "test.docx"
        doc_io.content_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        
        inst = StreamingConvertedPdf(doc_io, download=True)
        
        return inst.file_content()

    

                                                                                                                                                                                                        
                         
