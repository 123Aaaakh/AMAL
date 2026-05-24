def extract_imports(pe):
    imports = []
    print("\n[+] Mengekstrak Imported API...")

    try:
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            dll_name = entry.dll.decode('utf-8').lower()

            for imp in entry.imports:
                if imp.name:
                    api_name = imp.name.decode('utf-8')
                    imports.append(f"{dll_name}:{api_name}")

        print(f"    - Ditemukan {len(imports)} fungsi yang diimpor.")

        for i in imports[:5]:
            print(f"    * {i}")

        return imports

    except AttributeError:
        print("[!] Peringatan: Import Table tidak ditemukan! Kemungkinan besar file di-pack(obfuscated)")
        return[]
