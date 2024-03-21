from abc import ABC, abstractmethod

# Step 1: Document Interface
class Document(ABC):
    @abstractmethod
    def open(self):
        pass
    
    @abstractmethod
    def save(self):
        pass
    
    @abstractmethod
    def close(self):
        pass

# Step 2: Concrete Document Classes
class Letter(Document):
    def open(self):
        print("Opening letter document")
    
    def save(self):
        print("Saving letter document")
    
    def close(self):
        print("Closing letter document")

class Report(Document):
    def open(self):
        print("Opening report document")
    
    def save(self):
        print("Saving report document")
    
    def close(self):
        print("Closing report document")

class Spreadsheet(Document):
    def open(self):
        print("Opening spreadsheet document")
    
    def save(self):
        print("Saving spreadsheet document")
    
    def close(self):
        print("Closing spreadsheet document")

# Step 3: Document Factory
class DocumentFactory:
    @staticmethod
    def create_document(doc_type):
        if doc_type == "letter":
            return Letter()
        elif doc_type == "report":
            return Report()
        elif doc_type == "spreadsheet":
            return Spreadsheet()
        else:
            raise ValueError("Invalid document type")

# Step 4: Client Code
if __name__ == "__main__":
    document_type = input("Enter document type (letter, report, spreadsheet): ")
    document = DocumentFactory.create_document(document_type)
    document.open()
    document.save()
    document.close()
