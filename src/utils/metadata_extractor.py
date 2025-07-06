from PyPDF2 import PdfReader
def extract_metadata(file_path):
    try:
        reader = PdfReader(file_path)
        metadata = reader.metadata
        print("\n[+] PDF Metadata:")
        for key, value in metadata.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"[-] Error reading PDF metadata: {e}")
