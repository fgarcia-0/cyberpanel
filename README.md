# 🛠️ CyberPanel

Web Hosting Control Panel powered by OpenLiteSpeed, designed to simplify hosting management.

---

## 🔧 Features & Services

- 🔐 **Different User Access Levels** (via ACLs).
- 🌌 **Auto SSL** for secure websites.
- 💻 **FTP Server** for file transfers.
- 🕒 **Light-weight DNS Server** (PowerDNS).
- 🔐 **phpMyAdmin** to manage databases (MariaDB).
- 📧 **Email Support** (SnappyMail).
- 🕌 **File Manager** for quick file access.
- 🌐 **PHP Management** made easy.
- 🔒 **Firewall** (✅ FirewallD & ConfigServer Firewall Integration).
- 📀 **One-click Backups and Restores**.

---

## 🔢 Supported PHP Versions

CyberPanel supports PHP versions based on your operating system:

### ☑️ **PHP 8.0 and Above**
- Fully supported on modern systems such as Ubuntu 22.04 and AlmaLinux 9.x and higher.

### ☑️ **PHP 7.4 and Below**
- Compatible with AlmaLinux 8, Ubuntu 18.04, and similar environments.

### Adding PHP Versions as Third-Party Add-ons

Some PHP versions can be added to operating systems as third-party packages using external repositories or tools. Here's an overview by OS:

#### **Ubuntu**:
- **Ubuntu 22.04**:
  - Highest: PHP 8.5 (default repository or Ondrej's PPA).
  - Lowest: PHP 7.4 (via Ondrej's PPA).
- **Ubuntu 20.04**:
  - Highest: PHP 8.5 (default repository or Ondrej's PPA).
  - Lowest: PHP 7.0 (via Ondrej's PPA).
- **Ubuntu 18.04**:
  - Highest: PHP 8.4 (via Ondrej's PPA).
  - Lowest: PHP 5.6 (via Ondrej's PPA).

#### **AlmaLinux**:
- **AlmaLinux 9**:
  - Highest: PHP 8.5 (default repository or Remi repository).
  - Lowest: PHP 7.4 (via Remi repository).
- **AlmaLinux 8**:
  - Highest: PHP 8.4 (default repository or Remi repository).
  - Lowest: PHP 5.6 (via Remi repository).

#### **CentOS**:
- **CentOS 9**:
  - Highest: PHP 8.4 (via Remi repository).
  - Lowest: PHP 7.4 (via Remi repository).
- **CentOS 8**:
  - Highest: PHP 8.4 (via Remi repository).
  - Lowest: PHP 5.6 (via Remi repository).
- **CentOS 7**:
  - Highest: PHP 8.0 (via Remi repository).
  - Lowest: PHP 5.4 (via Remi repository).

#### **RHEL**:
- **RHEL 9**:
  - Highest: PHP 8.4 (via Remi repository).
  - Lowest: PHP 7.4 (via Remi repository).
- **RHEL 8**:
  - Highest: PHP 8.4 (via Remi repository).
  - Lowest: PHP 5.6 (via Remi repository).

#### **RockyLinux**:
- **RockyLinux 8**:
  - Highest: PHP 8.5 (via Remi repository).
  - Lowest: PHP 5.6 (via Remi repository).

#### **CloudLinux**:
- **CloudLinux 8**:
  - Highest: PHP 8.5 (via Remi repository).
  - Lowest: PHP 5.6 (via Remi repository).
- **CloudLinux 7**:
  - Highest: PHP 8.0 (via Remi repository).
  - Lowest: PHP 5.4 (via Remi repository).

#### **openEuler**:
- **openEuler 22.03**:
  - Highest: PHP 8.4 (default repository).
  - Lowest: PHP 7.4 (default repository).
- **openEuler 20.03**:
  - Highest: PHP 7.3 (default repository).
  - Lowest: PHP 7.0 (default repository).

### Full List of PHP Versions and End of Life (EOL) Dates:
- ✨ **PHP 8.5** - EOL: 31 Dec 2028.
- ✨ **PHP 8.4** - EOL: 31 Dec 2027.
- ✨ **PHP 8.3** - EOL: 31 Dec 2027.
- ✨ **PHP 8.2** - EOL: 31 Dec 2026.
- ✨ **PHP 8.1** - EOL: 31 Dec 2025.
- 🛑 **PHP 8.0** - EOL: 26 Nov 2023.
- 🛑 **PHP 7.4** - EOL: 28 Nov 2022.
- 🛑 **PHP 7.3** - EOL: 6 Dec 2021.
- 🛑 **PHP 7.2** - EOL: 30 Nov 2020.
- 🛑 **PHP 7.1** - EOL: 1 Dec 2019.
- 🛑 **PHP 7.0** - EOL: 10 Jan 2019.
- 🛑 **PHP 5.6** - EOL: 31 Dec 2018.
- 🛑 **PHP 5.5** - EOL: 21 Jul 2016.
- 🛑 **PHP 5.4** - EOL: 3 Sep 2015.
- 🛑 **PHP 5.3** - EOL: 14 Aug 2014.

---

## 🌐 Supported OS Versions

CyberPanel runs on x86_64 architecture and supports the following operating systems:

### **Ubuntu**:
- Ubuntu 22.04 ✅ Supported until April 2027.
- Ubuntu 20.04 ✅ Supported until April 2025.
- Ubuntu 18.04 🛑 EOL: 31 May 2023.

### **CentOS**:
- CentOS 9 ✅ EOL: 31 May 2027.
- CentOS 8 🛑 EOL: 31 Dec 2021.
- CentOS 7 🛑 EOL: 30 June 2024.

### **RHEL**:
- RHEL 9 ✅ EOL: 31 May 2032.
- RHEL 8 ✅ EOL: 31 May 2029.

### **AlmaLinux**:
- AlmaLinux 9 ✅ EOL: 31 May 2032.
- AlmaLinux 8 ✅ EOL: 31 May 2029.

### **Other OS**:
- RockyLinux 9 ✅ EOL: 31 May 2032.
- RockyLinux 8 ✅ EOL: 31 May 2029.
- CloudLinux 8 ✅ EOL: 31 May 2029.
- CloudLinux 7 🛑 EOL: 1 Jul 2024.
- openEuler 22.03 🛑 EOL: March 2024.
- openEuler 20.03 🛑 EOL: April 2022.

---

## ⚙️ Installation Instructions

Install CyberPanel easily with the following command:

```bash
sh <(curl https://cyberpanel.net/install.sh || wget -O - https://cyberpanel.net/install.sh)
```

---

## 📊 Upgrading CyberPanel

Upgrade your CyberPanel installation using:

```bash
sh <(curl https://raw.githubusercontent.com/fgarcia-0/cyberpanel/stable/preUpgrade.sh || wget -O - https://raw.githubusercontent.com/fgarcia-0/cyberpanel/stable/preUpgrade.sh)
```

---

## 📚 Resources

- 🌐 [Official Site](https://cyberpanel.net)
- ✏️ [Docs (Old)](https://docs.cyberpanel.net)
- 🎓 [Docs (New)](https://community.cyberpanel.net/docs)
- ✅ [Changelog](https://community.cyberpanel.net/t/change-logs/161)
- 💬 [Forums](https://community.cyberpanel.net)
- 📢 [Discord](https://discord.gg/g8k8Db3)
- 📵 [Facebook Group](https://www.facebook.com/groups/cyberpanel)
- 🎥 [YouTube Channel](https://www.youtube.com/@Cyber-Panel)

---