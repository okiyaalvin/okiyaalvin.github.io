---
layout: post
title: "💾 Setting Up OneDrive on Ubuntu the Right Way"
date: 2025-07-03
categories: ubuntu onedrive backup
image: /assets/image/one_drive_ubuntu.png
---

# 📦 OneDrive Backup Setup Guide for Ubuntu

Looking to back up your important files on Ubuntu seamlessly? This guide walks you through installing and configuring the official OneDrive CLI client. With just a few commands, your Desktop, Documents, and Pictures will be safely synced to the cloud — automatically.

✅ **Tested on Ubuntu 22.04 and 24.04.**

---

## 📘 Step-by-Step Instructions

### 1️⃣ Check Your Ubuntu Version

Let’s make sure you’re using a supported version:

```bash
lsb_release -a
```

> 📌 This will display your Ubuntu version. You need this to choose the correct repository in step 2. Supported versions include `22.04` and `24.04`.

---

### 2️⃣ Add the OneDrive Repository Key

Before installing the client, you need to add a trusted GPG key that allows your system to verify the packages.

#### 🔹 Ubuntu 22.04:

```bash
wget -qO - https://download.opensuse.org/repositories/home:/npreining:/debian-ubuntu-onedrive/xUbuntu_22.04/Release.key | gpg --dearmor | sudo tee /usr/share/keyrings/obs-onedrive.gpg >/dev/null
```

#### 🔹 Ubuntu 24.04:

```bash
wget -qO - https://download.opensuse.org/repositories/home:/npreining:/debian-ubuntu-onedrive/xUbuntu_24.04/Release.key | gpg --dearmor | sudo tee /usr/share/keyrings/obs-onedrive.gpg >/dev/null
```

> 🔐 This ensures the software you install is signed and secure.

---

### 3️⃣ Add the OneDrive Repository Source

Now you’ll add the actual software source to your APT list.

#### 🔹 Ubuntu 22.04:

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/obs-onedrive.gpg] https://download.opensuse.org/repositories/home:/npreining:/debian-ubuntu-onedrive/xUbuntu_22.04/ ./" | sudo tee /etc/apt/sources.list.d/onedrive.list
```

#### 🔹 Ubuntu 24.04:

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/obs-onedrive.gpg] https://download.opensuse.org/repositories/home:/npreining:/debian-ubuntu-onedrive/xUbuntu_24.04/ ./" | sudo tee /etc/apt/sources.list.d/onedrive.list
```

> 🧠 This tells Ubuntu where to find and download the OneDrive CLI software.

---

### 4️⃣ Install the OneDrive CLI

Now update your sources and install the client:

```bash
sudo apt update && sudo apt install onedrive
```

> ✅ This installs the `onedrive` command line tool you'll use to sync files with your OneDrive account.

---

### 5️⃣ Authorize and Run Your First Sync

Authenticate and sync with your Microsoft account:

```bash
onedrive --synchronize
```

- This will open a Microsoft login page in your browser.
- If it doesn’t, a login URL will appear in the terminal — just copy and paste it into a browser manually.
- Sign in with your Microsoft account and authorize the app.

![image](/assets/image/one_drive_ubuntu2.jpg)

> 🔑 This step links your Ubuntu device with your OneDrive account.

---

### 6️⃣ Back Up Your Important Folders

Use symbolic links to include your main folders (Desktop, Documents, Pictures) in the backup:

```bash
ln -s ~/Desktop ~/OneDrive/Desktop
ln -s ~/Documents ~/OneDrive/Documents
ln -s ~/Pictures ~/OneDrive/Pictures
```

> 📁 This makes OneDrive treat those folders like they’re inside `~/OneDrive`, ensuring their contents are synced.

---

### 7️⃣ Enable Auto Sync at Login

Make sure OneDrive syncs every time the user logs in:

```bash
systemctl --user enable onedrive
systemctl --user start onedrive
```

> 🔁 This starts a background service that watches for changes and syncs automatically — no manual syncing needed.

---

## 🧯 Troubleshooting & Common Issues

### ⚠️ `ln: failed to create symbolic link '...': File exists`

You may already have a folder with the same name in your `~/OneDrive` directory. Fix it like this:

```bash
mv ~/OneDrive/Desktop ~/OneDrive/Desktop-backup
ln -s ~/Desktop ~/OneDrive/Desktop
```

> 💡 This renames the old folder and creates the symbolic link safely.

---

### 🔁 OneDrive Does Not Sync After Reboot

Make sure the auto-sync service is actually enabled:

```bash
systemctl --user enable onedrive
```

> Also make sure the user is logging into a full graphical desktop session — background sync requires that.

---

### 🔑 Authorization Fails or Doesn’t Appear

If you skipped the browser login or something went wrong, rerun the sync to trigger login:

```bash
onedrive --synchronize
```

> This will give you a new link to authorize your account if needed.

---

### 🔍 View Current Configuration

To see all current settings and sync locations:

```bash
onedrive --display-config
```

> Useful for checking what’s actually being backed up or if defaults are in use.

---

## ✅ Done!

🎉 Your system is now set to automatically back up your files to OneDrive — quietly and continuously in the background.

No more worries about forgotten documents or misplaced photos. You're synced. ☁️🐧
