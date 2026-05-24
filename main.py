import argparse
import sys
import os

# Menambahkan 'src' ke path agar bisa import modul di dalamnya
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from static_analysis import extract_basic_pe_info
from iat import extract_imports
from read_algorithm import extract_section_entropy
from extract_sequence import extract_api_sequence
from ai_integration import LocalMalwareAI

def main():
    parser = argparse.ArgumentParser(description="Analys Mal - Automated Malware Analysis with AI")
    parser.add_argument("--pe", required=True, help="Path to the PE file (exe/dll) for static analysis")
    parser.add_argument("--report", required=True, help="Path to the Sandbox behavior report (JSON)")
    parser.add_argument("--model", default="llama3", help="Ollama model name to use (default: llama3)")
    
    args = parser.parse_args()

    if not os.path.exists(args.pe):
        print(f"[!] Error: File PE '{args.pe}' tidak ditemukan.")
        sys.exit(1)
    
    if not os.path.exists(args.report):
        print(f"[!] Error: File laporan '{args.report}' tidak ditemukan.")
        sys.exit(1)

    print("=== MEMULAI ANALISIS MALWARE ===")

    # 1. Analisis Statis
    pe = extract_basic_pe_info(args.pe)
    imports = extract_imports(pe)
    entropy = extract_section_entropy(pe)

    static_data = {
        "basic": {
            "Machine": hex(pe.FILE_HEADER.Machine),
            "Sections": pe.FILE_HEADER.NumberOfSections,
            "Characteristics": hex(pe.FILE_HEADER.Characteristics)
        },
        "imports": imports,
        "entropy": entropy
    }

    # 2. Analisis Dinamis
    api_sequence = extract_api_sequence(args.report)

    # 3. AI Synthesis
    ai = LocalMalwareAI(model_name=args.model)
    
    # Menyiapkan network_data (saat ini masih placeholder karena modul network belum ada)
    network_data = {
        "domains": "Analisis network belum diimplementasikan",
        "ips": "Analisis network belum diimplementasikan"
    }

    print("\n[+] Mengirim data ke AI untuk sintesis laporan...")
    report = ai.generate_malware_report(static_data, api_sequence, network_data)

    print("\n=== LAPORAN INTELIJEN AI ===")
    print(report)
    print("\n=== ANALISIS SELESAI ===")

if __name__ == "__main__":
    main()
