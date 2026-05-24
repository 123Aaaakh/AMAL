import math 

def calculate_entropy(data):
    if not data:
        return 0
    entropy = 0

    for x in range(256):
        p_x = float(data.count(x)) / len(data)
        if p_x > 0:
            entropy += - p_x * math.log(p_x, 2)
    return entropy

def extract_section_entropy(pe):
    section_data = []
    print("\n[+] Menganalisis Entropy Memory...")

    for section in pe.sections:
        sec_name = section.Name.decode('utf-8', errors='ignore').strip('\00')
        sec_size = section.SizeOfRawData

        sec_data = section.get_data()
        sec_entropy = calculate_entropy(sec_data)

        section_data.append({
            "Name": sec_name,
            "Size": sec_size,
            "Entropy": round(sec_entropy, 3)
            })

        warning = ""
        if sec_entropy > 7.0:
            warning = " [!] WARNING: Entropy sangat tinggi" 

        print(f"    - Section {sec_name}: Size={sec_size} bytes, Entropy={round(sec_entropy, 3)}{warning}")

    return section_data
