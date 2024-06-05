
#QUESTION NO 3:

from abc import ABC, abstractmethod

class Document(ABC):
    
    def __init__(self,file_name,file_size,content):
        
        self.file_name=file_name
        self.file_size=file_size
        self.content=content
        
        @abstractmethod
        def open(self):
            pass
        @abstractmethod
        def read(self):
            pass
        @abstractmethod
        def save(self):
            pass
        
class WordDocument(Document):
    def open(self):
        print(f"Opening word document:{self.file_name}")
        
    def read(self):
        print(f"Reading word document:{self.file_name}\nReading content:{self.content}")
        
    def save(self):
        print(f"Saving word document:{self.file_name}")
        
        
class PDFDocument(Document):
    def open(self):
        print(f"Opening PDF document:{self.file_name}")
        
    def read(self):
        print(f"Reading PDF document:{self.file_name}\nReading content:{self.content}")
        
    def save(self):
        print(f"Saving PDF document:{self.file_name}")
        
        
class ExcelDocument(Document):
    def open(self):
        print(f"Opening EXCEL document:{self.file_name}")
        
    def read(self):
        print(f"Reading EXCEL document:{self.file_name}\nReading content:{self.content}")
        
    def save(self):
        print(f"Saving EXCEL document:{self.file_name}")
        
        
class DocumentFactory:
    @staticmethod
    
    def createdoc(type_doc,file_name,file_size,content):
        
        if type_doc=="Word":
            
            return WordDocument(file_name,file_size,content)   
        
        elif type_doc=="PDF":
            
            return PDFDocument(file_name,file_size,content)   
        
        elif type_doc=="Excel":
            
            return ExcelDocument(file_name,file_size,content)
        
        else:
            print(f"Unknown document type:{self.type_doc}")
            
print("FOLLOWING ARE THE DOCUMENTS:\n") 

def main():
    
    word_doc=DocumentFactory.createdoc("Word","word.file.docx",3245,"It's a Word document!")
    
    word_doc.open()
    word_doc.read()
    word_doc.save()
    
    pdf_doc=DocumentFactory.createdoc("PDF","pdffile.docx",1125,"It's a PDF document!")
    
    pdf_doc.open()
    pdf_doc.read()
    pdf_doc.save()
    
    
    excel_doc=DocumentFactory.createdoc("Excel","excel.file.docx",6787,"It's a Excel document!")
    
    word_doc.open()
    word_doc.read()
    word_doc.save()


if __name__=="__main__":
    main()