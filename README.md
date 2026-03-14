# ⚔️ RedTeam-Arsenal: The Ultimate APT & Red Team Toolkit for Single Combat

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Contributors](https://img.shields.io/github/contributors/ADA-XiaoYao/RedTeam-Arsenal)](https://github.com/ADA-XiaoYao/RedTeam-Arsenal/graphs/contributors)
[![Platforms: Windows, macOS, Linux](https://img.shields.io/badge/Platforms-Windows%20%7C%20macOS%20%7C%20Linux-blue)](https://github.com/ADA-XiaoYao/RedTeam-Arsenal)

**RedTeam-Arsenal** is a world-class, all-in-one toolkit designed for top-tier Red Teamers and APT actors. It covers the entire attack lifecycle, from reconnaissance to reporting, supporting both CLI and GUI interfaces across Windows, macOS, and Linux.

Developed for **ADA-XiaoYao**, this arsenal aims to be a "phenomenal" single-combat weapon for professional offensive security operations.

---

## 🚀 Key Features

- **Full Lifecycle Coverage**: Recon, Scanning, Exploitation, Post-Exploitation, C2, Evasion, Persistence, Lateral Movement, Exfiltration, and Reporting.
- **Cross-Platform Support**: Seamless operation on Windows, macOS, and Linux.
- **Dual Interface**: Robust Command Line Interface (CLI) and an intuitive Graphical User Interface (GUI).
- **Tool Integration**: Pre-configured integration for 100+ mainstream Red Team and APT tools.
- **Modular Design**: Easily add, update, or remove tool modules.
- **Stealth & Evasion**: Built-in scripts for AV/EDR evasion and persistent access.

---

## 🛠️ Tool Catalog (Initial Preview)

| Phase | Core Tools |
| :--- | :--- |
| **Reconnaissance** | Subfinder, Amass, Assetfinder, Findomain, Shodan-CLI |
| **Scanning & Vuln** | Nmap, Nuclei, Nikto, Acunetix-CLI, Nessus-CLI |
| **Exploitation** | Metasploit Framework, SQLMap, BeEF, Commix, Evilginx2 |
| **C2 Frameworks** | Sliver, Havoc, Mythic, Cobalt Strike (Loader), PoshC2 |
| **Post-Exploitation** | Mimikatz, BloodHound, Impacket, Rubeus, SharpView |
| **Evasion & Stealth** | Veil, SharPersist, Inveigh, ScareCrow, Donut |
| **Persistence** | SharPersist, AnyDesk-Backdoor, Cron-Persistence |
| **Lateral Movement** | CrackMapExec, Responder, Invoke-TheHash, PsExec |
| **Exfiltration** | Rclone, DNScat2, Chisel, Ligolo-ng |
| **Reporting** | Ghostwriter, Serpico, Dradis |

---

## 📦 Installation

### Prerequisites

- Python 3.8+
- Git
- Go (for certain tools)
- Docker (optional, for containerized tools)

### Quick Start

```bash
git clone https://github.com/ADA-XiaoYao/RedTeam-Arsenal.git
cd RedTeam-Arsenal
pip install -r requirements.txt
python arsenal.py --help
```

---

## 🖥️ Usage

### CLI Mode
```bash
python arsenal.py list-tools
python arsenal.py install <tool_name>
```

### GUI Mode
```bash
python arsenal.py gui
```

---

## 📜 Disclaimer

This toolkit is intended for **educational purposes and authorized professional security testing only**. Unauthorized use of these tools against targets without prior written consent is illegal and strictly prohibited. The developer (ADA-XiaoYao) and contributors are not responsible for any misuse or damage caused by this toolkit.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

---

## 👤 Author

- **GitHub**: [ADA-XiaoYao](https://github.com/ADA-XiaoYao)
