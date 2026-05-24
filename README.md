# **AMAL (Analys Malware)**

AMAL is a Command Line Interface (CLI) malware analysis tool that combines static and dynamic feature extraction with the analytical power of local Large Language Models (LLMs).

Designed for Red and Blue Team analysts, this tool provides instant, automated Cyber Threat Intelligence (CTI) reports. By leveraging local AI processing, AMAL eliminates the need to send sensitive malware samples or telemetry to public APIs, ensuring **100% Operational Security (OpSec)**.

## **Key Features**

1. **Static Analysis**  
   * Parses Windows Portable Executable (PE) headers.  
   * Extracts the **Import Address Table (IAT)** to uncover the API functions the binary intends to call (malware intent).  
   * Calculates **Shannon Entropy** across memory sections to detect the presence of packers, obfuscation, or cryptographic routines.  
2. **Dynamic Analysis**  
   * Extracts API call sequences from Sandbox execution reports (e.g., CAPE or Cuckoo) in JSON format.  
   * Identifies execution chains that indicate malicious behaviors (e.g., Process Injection, Evasion).  
3. **Local AI Synthesis**  
   * Fuses static and dynamic data into a highly structured prompt.  
   * Utilizes **Ollama** to autonomously generate technical reports, threat classifications, and tactic mapping to the **MITRE ATT\&CK** framework.

## **Directory Structure**

.  
├── main.py                   \# Entry point. Handles CLI arguments and orchestrates the pipeline.  
├── src/  
│   ├── static\_analysis.py    \# Parses PE files to extract architectural metadata.  
│   ├── iat.py                \# Extracts Dynamic Link Libraries (DLLs) and imported API functions.  
│   ├── read\_algorithm.py     \# Calculates Shannon Entropy (0.0 \- 8.0) for each PE section.  
│   ├── extract\_sequence.py   \# Parses JSON sandbox reports to extract behavioral API chains.  
│   └── ai\_integration.py     \# Manages communication with the local LLM via Ollama.  
├── data/                     \# (Optional) Directory for storing malware samples (.exe) and sandbox logs (.json).  
├── requirements.txt          \# Python dependencies (pefile, ollama).  
└── README.md                 \# This documentation.

## **Prerequisites**

Before running AMAL, ensure your system (Linux/Windows/macOS) meets the following requirements:

1. **Python 3.8+**  
2. **Ollama** (Must be installed and running as a background service). [Download Ollama here](https://ollama.com/).  
3. A downloaded LLM model via Ollama (e.g., llama3). Run: ollama run llama3 to fetch it.

## **Installation**

It is highly recommended to run this tool inside an isolated Virtual Environment.

\# 1\. Clone the repository  
git clone [https://github.com/123Aaaakh/AMAL.git](https://github.com/123Aaaakh/AMAL.git)  
cd AMAL

\# 2\. Create and activate a Virtual Environment (Linux/macOS)  
python3 \-m venv venv  
source venv/bin/activate

\# 3\. Install required dependencies  
pip install \-r requirements.txt

## **Usage**

Execute the main script by providing the path to the sample file (PE), the Sandbox report (JSON), and the desired local model.

**Basic Syntax:**

python main.py \--pe \<PATH\_TO\_EXE\> \--report \<PATH\_TO\_JSON\> \--model \<OLLAMA\_MODEL\_NAME\>

**Example Execution:**

python main.py \--pe data/dummy\_malware.exe \--report data/report.json \--model llama3

**Execution Flow:**

1. Static Metadata & Entropy Extraction.  
2. API Sequence Parsing from JSON.  
3. Prompt injection and local LLM processing.  
4. The terminal prints the **Cyber Threat Intelligence Report** automatically.

**\[\!\]OpSec Disclaimer & Warning**

This tool is built for educational purposes, cybersecurity research, and defense analysis (Blue/Red Teaming). **Never** execute raw malware samples (.exe, .dll) directly on your primary Host machine. Always use an air-gapped or network-isolated Virtual Machine (VM) when handling live samples or generating sandbox reports. The developer assumes no liability for infrastructure damage caused by operational negligence.
