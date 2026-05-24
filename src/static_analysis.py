import pefile
import sys

def extract_basic_pe_info(file_path):
    try:
        pe = pefile.PE(file_path)

        pe_features = {
                "Machine": pe.FILE_HEADER.Machine,
                "SizeOfOptionalHeader": pe.FILE_HEADER.SizeOfOptionalHeader,
                "Characteristics": pe.FILE_HEADER.Characteristics,
                "MajorLinkerVersion": pe.OPTIONAL_HEADER.MajorLinkerVersion,
                "MajorImageVersion": pe.OPTIONAL_HEADER.MajorImageVersion,
                "CheckSum": pe.OPTIONAL_HEADER.CheckSum,
                "NumberOfSections": pe.FILE_HEADER.NumberOfSections
                }

        print("[+] Ekstraksi Metadata Dasar Berhasil")
        for key, value in pe_features.items():
            print(f"    -{key}: {hex(value) if isinstance(value, int) else value}")
        return pe

    except Exception as e:
        print(f"[!] Gagal membaca file pe: {e}")
        sys.exit(1)
