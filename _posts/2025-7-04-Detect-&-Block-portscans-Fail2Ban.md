---
layout: post
title: "🧱 Block Port Scans on Ubuntu with Fail2ban"
date: 2025-07-04
categories: ubuntu security fail2ban firewall
image: /assets/image/fail2ban_protection.png
---

# 🛡️ How to Detect and Block Port Scans with Fail2ban on Ubuntu

Port scanning is one of the first steps attackers use to find vulnerabilities in your system. With **Fail2ban**, you can detect suspicious patterns like repeated SSH login attempts or port scans and **automatically ban IPs** to keep your server safe.

This guide shows you how to install and configure Fail2ban to protect your Ubuntu system against port scanning and brute-force attacks.

---

## 📦 Step 1: Install Fail2ban

Install Fail2ban from the official Ubuntu repositories:

```bash
sudo apt update
sudo apt install fail2ban -y
```

---

## ⚙️ Step 2: Configure Fail2ban for SSH

Create a local configuration override to avoid editing the default files:

```bash
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
```

Then open the config file using nano:

```bash
sudo nano /etc/fail2ban/jail.local
```

Scroll down to the `[sshd]` section and make sure it's enabled:

```ini
[sshd]
enabled = true
port    = ssh
logpath = %(sshd_log)s
maxretry = 3
```

- `maxretry = 3` means the IP will be banned after 3 failed login attempts.
- You can also set `bantime` (how long to block), `findtime`, and `ignoreip`.

Save and exit:
- Press `Ctrl + O` → `Enter` → `Ctrl + X`

---

## 🕵️ Step 3: Enable Detection of Port Scans

To detect port scanning, Fail2ban can monitor logs from services like `ufw` or `iptables`.

First, make sure UFW is logging:

```bash
sudo ufw logging on
```

Then edit or create a jail for UFW:

```bash
sudo nano /etc/fail2ban/jail.d/ufw.conf
```

Paste the following:

```ini
[ufw]
enabled = true
filter = ufw
logpath = /var/log/ufw.log
maxretry = 2
bantime = 3600
findtime = 600
```

> This jail bans IPs that trigger firewall rules more than twice in 10 minutes.

Save and exit the file.

---

## 🚀 Step 4: Restart and Enable Fail2ban

Apply changes and enable the service on boot:

```bash
sudo systemctl restart fail2ban
sudo systemctl enable fail2ban
```

---

## 🔍 Step 5: Monitor Fail2ban in Action

To check status of active jails:

```bash
sudo fail2ban-client status
```

To see status of the `sshd` jail:

```bash
sudo fail2ban-client status sshd
```

To unban an IP (if needed):

```bash
sudo fail2ban-client set sshd unbanip 192.168.1.100
```

---

## 📄 Logs and Bans

Fail2ban logs are located here:

```bash
/var/log/fail2ban.log
```

Use this to check what IPs were banned and why.

---

## ✅ You're Protected

Fail2ban gives your Ubuntu system a solid defense against brute-force attacks and port scans — all with just a few configurations. Keep it active, monitor your logs, and sleep a little easier knowing Fail2ban has your back. 🧱🛡️

---

Let me know if you'd like to combine this with UFW firewall rules or enable email notifications on bans.
