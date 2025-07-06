def scan_pdf_keywords(file_path):
    keywords = ["/JavaScript", "/Launch", "/OpenAction", "/AA", "/URI"]
    try:
        with open(file_path, "rb") as f:
            content = f.read()
            print("\n[+] Scanning for suspicious keywords:")
            for keyword in keywords:
                if keyword.encode() in content:
                    print(f"  [!] Suspicious keyword found: {keyword}")
    except FileNotFoundError:
        print("[-] File not found.")
    except Exception as e:
        print(f"[-] Error: {e}")
