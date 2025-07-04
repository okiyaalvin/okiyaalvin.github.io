---
layout: post
title: "🛡️ How to Install and Use ClamAV on Ubuntu"
date: 2025-07-04
categories: ubuntu clamav antivirus
image: /assets/image/clamav_ubuntu.png
---

# 📝 Installing and Use ClamAV to Scan Ubuntu for Malware

Keeping your Ubuntu system clean from malicious files is critical — even on Linux. In this guide, you'll learn how to install, configure, and use **ClamAV**, a popular open-source antivirus tool, to scan for malware.

---

## 📦 Step 1: Install ClamAV

First, update your system and install ClamAV:

```bash
sudo apt update && sudo apt install clamav clamav-daemon -y
```

This installs the command-line scanner and the background daemon for automatic updates.

---

## 🔄 Step 2: Update Virus Definitions

ClamAV uses a virus database that must be kept up to date.

Stop the ClamAV daemon temporarily:

```bash
sudo systemctl stop clamav-freshclam
```

Manually update the definitions:

```bash
sudo freshclam
```

Then restart the daemon:

```bash
sudo systemctl start clamav-freshclam
```

> 💡 Tip: The daemon will now auto-update definitions in the background.

---

## 🧪 Step 3: Run a Manual Scan

To scan your **home directory**:

```bash
clamscan -r /home/yourusername
```

To scan your **entire system**:

```bash
sudo clamscan -r /
```

Use `--bell -i` to highlight infected files only:

```bash
sudo clamscan -r --bell -i /
```

---

## ⚙️ Step 4: Automate with Cron

You can run ClamAV daily or weekly using a cron job.

Open your crontab with the nano editor:

```bash
crontab -e
```

> 📝 If it's your first time using `crontab`, it may ask you to select an editor. Choose `nano` if available (usually option 1).

Add this line to schedule a scan every night at 2 AM:

```cron
0 2 * * * clamscan -r /home/yourusername --bell -i >> /var/log/clamav/scan.log
```

In nano, press `Ctrl+O` to save, then `Enter`, and `Ctrl+X` to exit.

---

## 📁 Optional: Use `clamdscan` for Faster Scans

`clamdscan` uses the daemon to scan faster than `clamscan`:

```bash
sudo clamdscan -r /home/yourusername
```

> Make sure the ClamAV daemon is running:

```bash
sudo systemctl status clamav-daemon
```

---

## ✅ You're Protected

ClamAV isn’t just for servers — it's also a smart choice for Linux desktops, file gateways, and anything that touches shared files. Stay secure, scan regularly, and automate where possible. ☁️🐧
