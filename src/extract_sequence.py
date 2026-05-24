import json
import sys

def extract_api_sequence(report_path, max_sequence=150):
    print(f"\n[+] Mengekstrak Urutan Perilaku dari {report_path}...")
    api_sequence = []

    try:
        with open(report_path, 'r') as file:
            report = json.load(file)

        if 'behavior' not in report or 'processes' not in report['behavior']:
            print("[!] Tidak ada log perilaku.")
            return []

        for process in report['behavior']['processes']:
            process_name = process.get('process_name', 'Unknown')
            pid = process.get('process_id', '0')
            print(f"    - Memindai Proses: {process_name} (PID: {pid})")

            for call in process.get('calls', []):
                api_name = call.get('api')
                if api_name:
                    api_sequence.append(api_name)

                if len(api_sequence) >= max_sequence:
                    break

            if len(api_sequence) >= max_sequence:
                break

        print(f"[+] Berhasil Mengekstrak {len(api_sequence)} rantai API.")
        if api_sequence:
            print(f"    - Cuplikan Perilaku:: {' -> '.join(api_sequence[:7])}...")
        return api_sequence

    except FileNotFoundError:
        print("[!] File laporan Sandbox tidak ditemukan.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("[!] Format JSON Sandbox rusak.")
        sys.exit(1)
