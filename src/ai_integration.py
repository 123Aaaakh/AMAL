import ollama

class LocalMalwareAI:
    def __init__(self, model_name="llama3"):
        self.model_name = model_name
        self.system_prompt = (
                    "Kamu adalah AI Ahli CyberSecurity di bidang Red Team dan Reverse Engineering senior. "
                    "Tugasmu adalah menganalisis data mentah (statis/dinamis) dari sebuah file biner misterius "
                    "dan memberikan laporan analisis yang to-the-point, kritis, realistis, tanpa basa-basi. "
                    "Identifikasi potensi ancaman, klasifikasi jenis malware (jika ada), petakan ke framework MITRE ATT&CK, "
                    "dan berikan rekomendasi mitigasi teknis."
                )

    def query_llm(self, prompt_content):
        print(f"[+] Menghubungi LLM Lokal ({self.model_name}) untuk sintesis data...")
        try:
            response = ollama.chat(
                    model=self.model_name,
                    messages=[
                            {"role": "system", "content": self.system_prompt},
                            {"role": "user", "content": prompt_content}
                        ]
                    )
            return response['message']['content']
        except Exception as e:
            return f"[!] Gagal berkomunikasi dengan LLM Lokal: {e}"

    def generate_malware_report(self, static_data, dynamic_data, network_data):
        # Menyusun data mentah menjadi format laporan terstruktur untuk dibaca AI
        prompt_content = f"""
        Tolong analisis data mentah biner berikut dan buat laporan intelijen siber:

        === DATA ANALISIS STATIS ===
        - Metadata Dasar: {static_data.get('basic', 'Tidak ada')}
        - API Terimpor (IAT): {static_data.get('imports', 'Tidak ada')[:30]} ... (dipotong untuk efisiensi)
        - Entropi Section Memori: {static_data.get('entropy', 'Tidak ada')}

        === DATA ANALISIS DINAMIS (BEHAVIOR) ===
        - Urutan Eksekusi API (Sequence): {' -> '.join(dynamic_data[:50]) if dynamic_data else 'Tidak ada aktivitas'}

        === DATA JARIAN / IOCs ===
        - Domain yang Dihubungi: {network_data.get('domains', 'Tidak ada')}
        - Alamat IP Tujuan: {network_data.get('ips', 'Tidak ada')}

        Format Output Laporan yang saya minta:
        1. Ringkasan Eksekutif (Apakah file ini berbahaya? Berapa persentase keyakinanmu?)
        2. Analisis Perilaku Teknis (Apa yang dicoba dilakukan oleh file ini di sistem & jaringan?)
        3. Pemetaan Taktik MITRE ATT&CK (Sebutkan teknik yang terdeteksi, misal: Process Injection, Kriptografi/Ransomware, Persistensi Registry).
        4. Langkah Mitigasi Red Team / Blue Team.
        """
        
        # Kirim prompt yang sudah dijahit ke fungsi LLM lokal
        report_output = self.query_llm(prompt_content)
        return report_output
