from utils.keyword_scanner import scan_pdf_keywords
from utils.metadata_extractor import extract_metadata

def show_menu():
    print("\033[1;93m[::] Select an option below\033[0m")
    print("\033[1;92m[01] Scan for Suspicious Keywords")
    print("[02] Extract Metadata")
    print("[03] Exit\033[0m")

    choice = input("\n\033[1;94m[>>] Enter your choice: \033[0m")

    if choice == "1":
        path = input("Enter path to PDF: ")
        scan_pdf_keywords(path)
    elif choice == "2":
        path = input("Enter path to PDF: ")
        extract_metadata(path)
    elif choice == "3":
        print("Exiting. Goodbye!")
    else:
        print("Invalid choice. Try again.")
