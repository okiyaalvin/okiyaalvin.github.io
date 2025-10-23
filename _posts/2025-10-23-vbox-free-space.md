---
title: "💣 Shrinking a Kali or Parrot OS VirtualBox Disk (VDI)"
image: /assets/image/vbox-space/Shrink_vdi.png
date: 2025-10-23 14:00:00 +0300
categories: virtualization linux ubuntu
tags: [virtualbox, vdi, kali, parrot, optimization, disk-space]
layout: post
---

### 🧩 How to Shrink a Kali or Parrot OS VirtualBox Disk (VDI) Safely

This guide helps you **reduce the size of a VirtualBox VDI disk** after your Linux guest (Kali or Parrot) starts occupying too much space on Windows.

---

### 🧭 Step 1: Check Your Disk Layout

```bash
lsblk
```

Take note of the partition that holds `/` (root). In my case, it’s:

```
/dev/sda1 on / 
```
![image](/assets/image/vbox-space/lsblk.png)
---

### 🧹 Step 2: Clean Unused Files

Run these commands in your Kali or Parrot terminal:

```bash
sudo apt autoremove -y
sudo apt clean
sudo journalctl --vacuum-time=3d
```

This removes unnecessary packages, cleans cache, and truncates old logs.

---

### 💾 Step 3: Fill Free Space with Zeros (Prepares for Compression)

In your Linux VM, run:

```bash
sudo dd if=/dev/zero of=/EMPTY bs=1M
sudo sync
sudo rm -f /EMPTY
```
![image](/assets/image/vbox-space/dd.png)
> ⚠️ The `dd` command will fill your disk to 100% temporarily — that’s expected. Once it errors with *“No space left on device”*, continue.

This replaces all unused space with zeros, which makes compression more effective.

---

### 🧰 Step 4: (Optional) Use Zerofree for EXT Partitions

If your root filesystem is **ext4**, you can use `zerofree` — but since your system uses **Btrfs**, skip this step.

If you ever work with `ext4`, do this instead:

1. Boot from a **Live CD** (Kali or Ubuntu ISO).
2. Open terminal and find your root partition (e.g. `/dev/sda1`).
3. Run:

   ```bash
   sudo zerofree -v /dev/sda1
   ```

---

### 🧩 Step 5: Compact the VDI from Windows Host

After shutting down your VM, open **Command Prompt** as Administrator and run:

```cmd
cd "C:\Program Files\Oracle\VirtualBox"
VBoxManage modifymedium "C:\Users\<Your username>\VirtualBox VMs\Parrot-Os\Parrot-Os.vdi" --compact
```

> Adjust the `.vdi` path to match your VM’s location.

If `VBoxManage` is not recognized, add VirtualBox to your PATH or run the command from the folder where it’s installed.

---

### 🧾 Step 6: Verify the Space Reduction

Go to your VM folder on Windows and check the **VDI file size** before and after compacting. You should see a noticeable decrease.

---

### ✅ Optional Tips

* **Take a snapshot** before doing this, just in case.
* **Disable automatic snapshots** in VirtualBox if disk size grows again.
* Use `btrfs filesystem df /` to check actual space usage inside the VM.

---

### 🔒 Summary

| Step | Action                  | Purpose                            |
| ---- | ----------------------- | ---------------------------------- |
| 1    | Check partitions        | Identify mounted disk              |
| 2    | Clean junk              | Free real space                    |
| 3    | Write zeros             | Prepare free space for compression |
| 4    | Use Zerofree (optional) | EXT4 optimization                  |
| 5    | Compact VDI             | Physically reduce file size        |
| 6    | Verify                  | Confirm reduction                  |

---

Now your Kali or Parrot VDI should take **much less space** on your Windows host.
