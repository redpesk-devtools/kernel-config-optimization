# Configure Linux Kernel

* Kernel-specific optimizations: minimal modules, kernel parameters, initrd, and others
* Building a reduced kernel (with less modules for examples) for faster boot time

Please note in our usecase, we used the [BeagleBoard BeaglePlay](https://docs.redpesk.bzh/docs/en/master/redpesk-os/boards/docs/boards/beagleplay.html) as our reference.

We used Linux kernel version 6.6, you can check some of our sources [here](https://github.com/redpesk-devtools/kernel-config-optimization/tree/main/beagle-board/packaging)

## Generating a .cfg file for Linux Kernel configuration

You may want to customize your Linux Kernel configuration with a configuration fragment (called `cfg`).

An easy way to do that is to:

```bash
cd ${KERNEL_SOURCE}
cp .config .config.sav
make menuconfig
diff --unchanged-line-format= --old-line-format= --new-line-format="%L" ./.config.sav ./.config > 01-my-file.cfg
```

## Merge a .cfg file to Linux Kernel configuration

If you want to merge a cfg configuration fragment to your Linux Kernel configuration just:

```bash
scripts/kconfig/merge_config.sh -m -r .config 01-my-file.cfg
```

If you have more than one cfg files:

```bash
for CFG in *.cfg; do
  scripts/kconfig/merge_config.sh -m -r .config ${CFG}
done
```

## Test your new Kernel

After the build of your kernel packages, you can simply copy them to your board and install them.

```bash
scp ./kernel-modules-extra-${VER}-${REL}.rpbatz.aarch64.rpm \
    ./kernel-modules-${VER}-${REL}.rpbatz.aarch64.rpm \
    ./kernel-core-${VER}-${REL}.rpbatz.aarch64.rpm \
    ./kernel-${VER}-${REL}.rpbatz.aarch64.rpm \
    root@X.X.X.X:/;
ssh root@X.X.X.X dnf install -y /*; 
```

## Disable unused drivers

Disabling unused drivers is a key step in optimizing the boot time of a Linux Kernel, especially for embedded or industrial systems where specific hardware configurations are well-defined.

Use `make menuconfig` to go to the configuration of the Kernel!

*This requires to already have your defconfig declared and used*. For more reference, go [here](https://docs.kernel.org/kbuild/kconfig.html)!

So our goal is to disable unnecessary drivers. Navigate to `Device Drivers` and uncheck drivers not required for the system. See our examples below!

### 01 Unnecessary protocols

If your system doesn’t require certain networking features:

* Appletalk: `CONFIG_ATALK`
* AX.25 and Packet Radio: `CONFIG_X25`
* Amateur Radio Protocols: `CONFIG_HAMRADIO`, `CONFIG_AX25`, `CONFIG_NETROM`
* WAN Support
  * WAN drivers like `CONFIG_HDLC`, `CONFIG_PPP`, or `CONFIG_SLIP` if not needed.

### 02 Wireless

If your system doesn’t use Wi-Fi or specific wireless features:

* Wireless LAN drivers
  * Disable all unused drivers under `CONFIG_WLAN`.
* Specific chipset drivers:
  * Examples: `CONFIG_RTL8192CU`, `CONFIG_ATH9K`, `CONFIG_B43`
* RF Kill:
  * If unused, disable `CONFIG_RFKILL`.
* Regulatory framework:
  * If unnecessary, disable `CONFIG_CFG80211` and related features like `CONFIG_CFG80211_WEXT`.
* Wireless extensions:
  * Disable `CONFIG_WIRELESS_EXT` if not required for backward compatibility.

### 03 Bluetooth

If your system doesn’t use Bluetooth:

* Disable Bluetooth stack entirely: `CONFIG_BT`
* Disable profiles and protocols like:
  * Audio (RFCOMM): `CONFIG_BT_RFCOMM`

If your system has limited or no network requirements:

* QoS and traffic control:
  * Disable: `CONFIG_NET_SCHED`, `CONFIG_NET_CLS`
  Specific schedulers like `CONFIG_NET_SCH_HTB`, `CONFIG_NET_SCH_HFSC`
* Routing and tunneling protocols:
  * Examples: `CONFIG_NET_IPGRE`, `CONFIG_IPV6_SIT`, `CONFIG_NET_IPIP`, `CONFIG_NET_UDP_TUNNEL`
* Mobile networking:
  * GPRS, LTE, or 5G support: `CONFIG_NET_MPLS`
* ISDN:
  * Disable `CONFIG_ISDN`, `CONFIG_ISDN_CAPI`.
* Ethernet adapters:
  * Disable drivers for unused Ethernet chipsets: `CONFIG_E1000`, `CONFIG_TIGON3`, `CONFIG_R8169`, etc.

### 04 Filesystems

Disable filesystems you don’t use (on redpesk OS we only use `vfat` and `ext4` filesystems for example):

* Network filesystems:
  * CIFS/SMB (Windows Sharing): `CONFIG_CIFS`
  * AFS: `CONFIG_AFS`
  * Ceph: `CONFIG_CEPH_FS`
* Specialized distributed filesystems:
  * Examples: `CONFIG_GFS2_FS`, `CONFIG_OCFS2_FS`.
* CD/DVD support:
  * Disable: `CONFIG_UDF_FS`.
* Specialty filesystems:
  * ReiserFS: `CONFIG_REISERFS_FS`
  * JFS: `CONFIG_JFS_FS`
  * XFS: `CONFIG_XFS_FS`
  * OCFS2: `CONFIG_OCFS2_FS`
  * Btrfs: `CONFIG_BTRFS_FS` (if not used).
* FUSE:
  * Filesystem in userspace: `CONFIG_FUSE_FS` (used for mounts like SSHFS).

### 05 Graphics

For headless systems or if the display is not used during boot:

* Framebuffer devices:
  * Disable framebuffer drivers: `CONFIG_FB`.
* DRM (Direct Rendering Manager):
  * Disable drivers for GPUs not used, such as `CONFIG_DRM_AMDGPU`, `CONFIG_DRM_I915`, or `CONFIG_DRM_NOUVEAU`.
* Console support:
  * Reduce console support: `CONFIG_VGA_CONSOLE`, `CONFIG_FRAMEBUFFER_CONSOLE`.

### 06 Multimedia (cameras, TV Tuners, video devices)

For systems without multimedia capabilities:

* V4L (Video for Linux): `CONFIG_MEDIA_SUPPORT`(main config), `CONFIG_VIDEO_DEV`
* TV and radio tuner support: `CONFIG_DVB_CORE`, `CONFIG_MEDIA_TUNER`
* Camera drivers:
  * Example: `CONFIG_USB_VIDEO_CLASS` (UVC for webcams).
* Radio transmitters:
  * Disable support for FM transmitters: `CONFIG_RADIO_ADAPTERS`.
* Specialized video hardware:
  * Examples: `CONFIG_VIDEO_TW5864`.

### 07 Input devices

For systems without input peripherals:

* Keyboards and mice:
  * PS/2 Keyboard/Mouse: `CONFIG_KEYBOARD_ATKBD`
  * USB HID Devices: `CONFIG_USB_HID`, `CONFIG_HID_GENERIC`
* Touchscreens and Joysticks:
  * Disable under `CONFIG_INPUT_TOUCHSCREEN` and `CONFIG_INPUT_JOYSTICK`.
* Display adapters:
  * Disable: `CONFIG_FB_VGA16`, `CONFIG_FB_RADEON`.
* Tablets
* Miscellaneous devices

### 08 Storage

For unused storage controllers and filesystems:

* SCSI and RAID:
  * Disable unnecessary SCSI drivers: `CONFIG_SCSI`, `CONFIG_RAID456`, `CONFIG_DM_RAID`.
* Floppy drives:
  * `CONFIG_BLK_DEV_FD`
* MMC/SD card support:
  * `CONFIG_MMC`, `CONFIG_MMC_BLOCK`

### 09 Sound

For systems without audio needs:

* Sound subsystem:
  * Disable ALSA and OSS: `CONFIG_SOUND`.
* Specific sound drivers:
  * Disable drivers under `CONFIG_SND` for hardware you don’t use.
* High-Definition audio:
  * Disable `CONFIG_SND_HDA_INTEL`, `CONFIG_SND_HDA_CODEC`
* Digital audio interfaces:
  * Examples: `CONFIG_SND_SOC`, `CONFIG_SND_USB_AUDIO`.

### 10 Power management

If power-saving features aren’t needed:

* CPU frequency scaling:
  * `CONFIG_CPU_FREQ` and governors like `CONFIG_CPU_FREQ_GOV_ONDEMAND`.
* ACPI:
  * `CONFIG_ACPI` and related options like `CONFIG_ACPI_SLEEP`.
* Thermal management:
  * `CONFIG_THERMAL`, `CONFIG_THERMAL_HWMON`.
* Dynamic voltage and frequency scaling (DVFS):
  * Disable CPU frequency governors: `CONFIG_CPU_FREQ_GOV_USERSPACE`, `CONFIG_CPU_FREQ_GOV_PERFORMANCE`.
* Energy measurement:
  * Disable drivers like `CONFIG_ENERGY_MODEL`.

### 11 Power supply and battery

For systems without batteries or power supply monitoring:

* Battery management and Power supply monitoring
  * `CONFIG_POWER_SUPPLY_HWMON`
  * `CONFIG_GENERIC_ADC_BATTERY`
  * `CONFIG_BATTERY_DS2760`
  * `CONFIG_BATTERY_SBS`
  * `CONFIG_BATTERY_BQ27XXX`
  * `CONFIG_CHARGER_GPIO`
  * `CONFIG_CHARGER_BQ2415X`
  * `CONFIG_CHARGER_BQ25890`

### 12 Legacy hardware

For systems that don’t use old specific hardware:

* Parallel port:
  * `CONFIG_PARPORT`, `CONFIG_PRINTER`, `CONFIG_USB_CONFIGFS_F_PRINTER`
* Serial port:
  * `CONFIG_SERIAL_8250` (if no serial console is required).
* PCMCIA:
  * `CONFIG_PCMCIA` and related drivers.

### 13 LED and GPIO drivers

If your system doesn’t require LEDs or GPIO-specific functionality

* LED Support: `CONFIG_LEDS_CLASS`
* LED Triggers:
  * Examples: `CONFIG_LEDS_TRIGGER_TIMER`, `CONFIG_LEDS_TRIGGER_HEARTBEAT`
* GPIO Drivers:
  * Disable unused platform-specific GPIO drivers under `CONFIG_GPIO`.

Serial, Infrared, and Industrial Communication: For embedded systems without legacy communication interfaces

* Serial drivers:
  * General: `CONFIG_SERIAL_8250`
    * If you remove `CONFIG_SERIAL_8250` you will not have access to the log on your seriel port.
  * USB Serial: `CONFIG_USB_SERIAL`
  * Specific device drivers, such as `CONFIG_USB_SERIAL_PL2303` or `CONFIG_USB_SERIAL_CP210X`.
* CAN Bus, CANOpen, DeviceNet, etc.:
  * If unused, disable `CONFIG_CAN`, `CONFIG_CAN_RAW`, and specific drivers like `CONFIG_CAN_SJA1000`.
* I2C and SPI drivers:
  * Disable unused platform-specific drivers for `CONFIG_I2C` and `CONFIG_SPI`.
* Industrial I/O:
  * Disable unused IIO drivers: `CONFIG_IIO`.

### 14 Real-Time Clock (RTC)

* RTC Framework:
  * `CONFIG_RTC_CLASS`
* Platform-Specific RTC drivers:
  * Examples: `CONFIG_RTC_DRV_CMOS`, `CONFIG_RTC_DRV_DS1307`

### 15 Sensors and monitoring

For systems without hardware monitoring needs:

* Hardware monitoring (HWMON):
  * `CONFIG_HWMON`
* Sensor drivers:
  * Examples: `CONFIG_SENSORS_LM75`, `CONFIG_SENSORS_CORETEMP`.

### 16 Debugging features

Disable debugging options to reduce kernel size and improve performance:

* Kernel debugging:
  * `CONFIG_DEBUG_KERNEL`
* DebugFS:
  * If not used: `CONFIG_DEBUG_FS`
* Printk debugging:
  * Reduce `CONFIG_PRINTK` overhead.
* Kprobes:
  * Disable `CONFIG_KPROBES`, `CONFIG_UPROBES`.
* Tracepoints:
  * Disable `CONFIG_FTRACE`.

### 17 Special hardware devices

For embedded or industrial systems that do not use specialized hardware:

* Tablet input devices:
  * Examples: `CONFIG_INPUT_TABLET`
* Joystick/Gamepad support:
  * Examples: `CONFIG_INPUT_JOYSTICK`, `CONFIG_JOYDEV`
* Haptic devices:
  * Example: `CONFIG_INPUT_FF_MEMLESS`

### 18 Virtualization and emulation

If virtualization is not required:

* KVM (Kernel Virtual Machine):
  * `CONFIG_KVM`
* Xen Hypervisor support:
  * `CONFIG_XEN`
* QEMU guest agent:
  * `CONFIG_VIRTIO_CONSOLE`
* Virtual network interfaces:
  * Examples: `CONFIG_VIRTIO_NET`, `CONFIG_TUN`.
* Advanced virtualization features:
  * Disable `CONFIG_VIRTIO_BLK`, `CONFIG_VIRTIO_MMIO`.
* Hypervisor frameworks:
  * Disable `CONFIG_BALLOON_COMPACTION`, `CONFIG_MEMORY_BALLOON` , `CONFIG_VIRTIO_BALLOON`.

### 19 Cryptographic and security features

For systems without advanced cryptographic requirements:

* Unused cryptographic algorithms:
  * Examples: `CONFIG_CRYPTO_DES`, `CONFIG_CRYPTO_BLOWFISH`
* Security modules:
  * If not used, disable AppArmor or SELinux: `CONFIG_SECURITY_APPARMOR`, `CONFIG_SECURITY_SELINUX`.
* Key retention services:
  * Example: `CONFIG_KEYS`

### 20 Special subsystems

* Huge pages:
  * If not used, disable `CONFIG_HUGETLBFS` and `CONFIG_HUGETLB_PAGE`.

### 21 USB devices

If your system does not use certain USB peripherals, disable unnecessary drivers

* USB Printers: `CONFIG_USB_PRINTER`
* USB Modem support: `CONFIG_USB_ACM`
* USB Storage:
  * If no USB storage devices are required: `CONFIG_USB_STORAGE`
* USB Wi-Fi adapters:
  * Examples: `CONFIG_RT2800USB`, `CONFIG_RTL8187`
* USB Gadget Drivers:
  * For embedded systems not using USB gadgets: `CONFIG_USB_GADGET`.

### 22 Kernel subsystems

* Block layer:
  * Disable unused IO schedulers: `CONFIG_IOSCHED_BFQ`, `CONFIG_IOSCHED_DEADLINE`.
* Watchdog support:
  * If unused, disable `CONFIG_WATCHDOG` and related drivers.
* IRQ debugging:
  * Disable: `CONFIG_DEBUG_IRQFLAGS`, `CONFIG_DEBUG_STACKOVERFLOW`.

### 23 Miscellaneous

If you don't use specific debugging features:

* Debugging options:
  * Disable kernel debugging to reduce overhead: `CONFIG_EXPERT`, `CONFIG_DEBUG_KERNEL`, `CONFIG_PRINTK`.
  * To disable the time stamp of the kernel journal `CONFIG_PRINTK_TIME`.

### Tips for safe optimization

* Start with known requirements
  * Clearly define the hardware and peripherals your system uses
* Disable features incrementally
  * Test the system after disabling each set of features to verify functionality
