# Kernel Configuration Reference

This document provides a detailed breakdown of kernel configuration fragments used to optimize the Linux kernel for embedded use cases.

## 01 - Config disabled ipc timers audit

**Summary**: This fragment disables or configures kernel options related to: *config disabled ipc timers audit*.

### Configuration options:
- `CONFIG_PREEMPT_VOLUNTARY_BUILD`:
  - Set to `y`

## 02 - Config disabled kconfig scheduler initrd

**Summary**: This fragment disables or configures kernel options related to: *config disabled kconfig scheduler initrd*.

### Configuration options:
- `CONFIG_SYSFS_SYSCALL`:
  - Set to `y`

## 03 - Config disabled perf profiling errata

**Summary**: This fragment disables or configures kernel options related to: *config disabled perf profiling errata*.

### Configuration options:
- `CONFIG_NO_IOPORT_MAP`:
  - Set to `y`

## 04 - Config disabled efi power debug

**Summary**: This fragment disables or configures kernel options related to: *config disabled efi power debug*.

### Configuration options:

## 05 - Config cpufreq schedutil no virt

**Summary**: This fragment disables or configures kernel options related to: *config cpufreq schedutil no virt*.

### Configuration options:
- `CONFIG_CPU_FREQ_DEFAULT_GOV_SCHEDUTIL`:
  - Set to `y`

## 06 - Config disabled kprobes jumplabel

**Summary**: This fragment disables or configures kernel options related to: *config disabled kprobes jumplabel*.

### Configuration options:

## 07 - Config no gcc plugins block align

**Summary**: This fragment disables or configures kernel options related to: *config no gcc plugins block align*.

### Configuration options:
- `CONFIG_FUNCTION_ALIGNMENT`:
  - Set to `4`

## 08 - Config disabled partitions

**Summary**: This fragment disables or configures kernel options related to: *config disabled partitions*.

### Configuration options:

## 09 - Config arch inline spinlocks

**Summary**: This fragment disables or configures kernel options related to: *config arch inline spinlocks*.

### Configuration options:
- `CONFIG_ARCH_INLINE_SPIN_TRYLOCK`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_SPIN_TRYLOCK_BH`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_SPIN_LOCK`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_SPIN_LOCK_BH`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_SPIN_LOCK_IRQ`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_SPIN_LOCK_IRQSAVE`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_SPIN_UNLOCK`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_SPIN_UNLOCK_BH`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_SPIN_UNLOCK_IRQ`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_SPIN_UNLOCK_IRQRESTORE`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_READ_LOCK`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_READ_LOCK_BH`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_READ_LOCK_IRQ`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_READ_LOCK_IRQSAVE`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_READ_UNLOCK`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_READ_UNLOCK_BH`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_READ_UNLOCK_IRQ`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_READ_UNLOCK_IRQRESTORE`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_WRITE_LOCK`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_WRITE_LOCK_BH`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_WRITE_LOCK_IRQ`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_WRITE_LOCK_IRQSAVE`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_WRITE_UNLOCK`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_WRITE_UNLOCK_BH`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_WRITE_UNLOCK_IRQ`:
  - Set to `y`
- `CONFIG_ARCH_INLINE_WRITE_UNLOCK_IRQRESTORE`:
  - Set to `y`
- `CONFIG_INLINE_SPIN_TRYLOCK`:
  - Set to `y`
- `CONFIG_INLINE_SPIN_TRYLOCK_BH`:
  - Set to `y`
- `CONFIG_INLINE_SPIN_LOCK`:
  - Set to `y`
- `CONFIG_INLINE_SPIN_LOCK_BH`:
  - Set to `y`
- `CONFIG_INLINE_SPIN_LOCK_IRQ`:
  - Set to `y`
- `CONFIG_INLINE_SPIN_LOCK_IRQSAVE`:
  - Set to `y`
- `CONFIG_INLINE_SPIN_UNLOCK_BH`:
  - Set to `y`
- `CONFIG_INLINE_SPIN_UNLOCK_IRQ`:
  - Set to `y`
- `CONFIG_INLINE_SPIN_UNLOCK_IRQRESTORE`:
  - Set to `y`
- `CONFIG_INLINE_READ_LOCK`:
  - Set to `y`
- `CONFIG_INLINE_READ_LOCK_BH`:
  - Set to `y`
- `CONFIG_INLINE_READ_LOCK_IRQ`:
  - Set to `y`
- `CONFIG_INLINE_READ_LOCK_IRQSAVE`:
  - Set to `y`
- `CONFIG_INLINE_READ_UNLOCK`:
  - Set to `y`
- `CONFIG_INLINE_READ_UNLOCK_BH`:
  - Set to `y`
- `CONFIG_INLINE_READ_UNLOCK_IRQ`:
  - Set to `y`
- `CONFIG_INLINE_READ_UNLOCK_IRQRESTORE`:
  - Set to `y`
- `CONFIG_INLINE_WRITE_LOCK`:
  - Set to `y`
- `CONFIG_INLINE_WRITE_LOCK_BH`:
  - Set to `y`
- `CONFIG_INLINE_WRITE_LOCK_IRQ`:
  - Set to `y`
- `CONFIG_INLINE_WRITE_LOCK_IRQSAVE`:
  - Set to `y`
- `CONFIG_INLINE_WRITE_UNLOCK`:
  - Set to `y`
- `CONFIG_INLINE_WRITE_UNLOCK_BH`:
  - Set to `y`
- `CONFIG_INLINE_WRITE_UNLOCK_IRQ`:
  - Set to `y`
- `CONFIG_INLINE_WRITE_UNLOCK_IRQRESTORE`:
  - Set to `y`

## 10 - Config no swap hotplug ksm

**Summary**: This fragment disables or configures kernel options related to: *config no swap hotplug ksm*.

### Configuration options:

## 11 - Config disabled network ipv4 ipv6 netfilter

**Summary**: This fragment disables or configures kernel options related to: *config disabled network ipv4 ipv6 netfilter*.

### Configuration options:

## 12 - Config sctp no vlan tipc batman

**Summary**: This fragment disables or configures kernel options related to: *config sctp no vlan tipc batman*.

### Configuration options:
- `CONFIG_IP_SCTP`:
  - Set to `y`
- `CONFIG_SCTP_DEFAULT_COOKIE_HMAC_NONE`:
  - Set to `y`
- `CONFIG_NET_MPLS_GSO`:
  - Set to `m`

## 13 - Config disabled wireless bt can rfkill

**Summary**: This fragment disables or configures kernel options related to: *config disabled wireless bt can rfkill*.

### Configuration options:
- `CONFIG_FAILOVER`:
  - Set to `m`

## 14 - Config disabled pci firmware

**Summary**: This fragment disables or configures kernel options related to: *config disabled pci firmware*.

### Configuration options:

## 15 - Config no gnss procevents

**Summary**: This fragment disables or configures kernel options related to: *config no gnss procevents*.

### Configuration options:

## 16 - Config disabled block nbd aoe

**Summary**: This fragment disables or configures kernel options related to: *config disabled block nbd aoe*.

### Configuration options:

## 17 - Config eeprom 93cx6 others disabled

**Summary**: This fragment disables or configures kernel options related to: *config eeprom 93cx6 others disabled*.

### Configuration options:
- `CONFIG_EEPROM_93CX6`:
  - Set to `y`

## 18 - Config no network devices bond vendor

**Summary**: This fragment disables or configures kernel options related to: *config no network devices bond vendor*.

### Configuration options:

## 19 - Config disabled phy drivers

**Summary**: This fragment disables or configures kernel options related to: *config disabled phy drivers*.

### Configuration options:

## 20 - Config no ppp wlan yes failover

**Summary**: This fragment disables or configures kernel options related to: *config no ppp wlan yes failover*.

### Configuration options:
- `CONFIG_NET_FAILOVER`:
  - Set to `m`

## 21 - Config no input devices

**Summary**: This fragment disables or configures kernel options related to: *config no input devices*.

### Configuration options:

## 22 - Config no serial tty tpm

**Summary**: This fragment disables or configures kernel options related to: *config no serial tty tpm*.

### Configuration options:

## 23 - Config disabled i2c power sensors

**Summary**: This fragment disables or configures kernel options related to: *config disabled i2c power sensors*.

### Configuration options:

## 24 - Config no mfd display media

**Summary**: This fragment disables or configures kernel options related to: *config no mfd display media*.

### Configuration options:

## 25 - Config no usb sound rtc virtio

**Summary**: This fragment disables or configures kernel options related to: *config no usb sound rtc virtio*.

### Configuration options:
- `CONFIG_VIRTIO`:
  - Set to `m`

## 26 - Config no fs encodings

**Summary**: This fragment disables or configures kernel options related to: *config no fs encodings*.

### Configuration options:
- `CONFIG_DLM`:
  - Set to `y`

## 27 - Config crypto core sha3 xts

**Summary**: This fragment disables or configures kernel options related to: *config crypto core sha3 xts*.

### Configuration options:
- `CONFIG_CRYPTO_AEAD`:
  - Set to `m`
- `CONFIG_CRYPTO_RNG_DEFAULT`:
  - Set to `m`
- `CONFIG_CRYPTO_AUTHENC`:
  - Set to `m`
- `CONFIG_CRYPTO_CTR`:
  - Set to `m`
- `CONFIG_CRYPTO_ECB`:
  - Set to `m`
- `CONFIG_CRYPTO_XTS`:
  - Set to `m`
- `CONFIG_CRYPTO_GENIV`:
  - Set to `m`
- `CONFIG_CRYPTO_SEQIV`:
  - Set to `m`
- `CONFIG_CRYPTO_GHASH`:
  - Set to `y`
- `CONFIG_CRYPTO_SHA512`:
  - Set to `m`
- `CONFIG_CRYPTO_SHA3`:
  - Set to `m`
- `CONFIG_CRYPTO_CRCT10DIF`:
  - Set to `m`
- `CONFIG_CRYPTO_DEFLATE`:
  - Set to `m`

## 28 - Config crypto drbg jitter no hw

**Summary**: This fragment disables or configures kernel options related to: *config crypto drbg jitter no hw*.

### Configuration options:
- `CONFIG_CRYPTO_DRBG_MENU`:
  - Set to `m`
- `CONFIG_CRYPTO_DRBG`:
  - Set to `m`
- `CONFIG_CRYPTO_JITTERENTROPY`:
  - Set to `m`
- `CONFIG_ZLIB_INFLATE`:
  - Set to `m`
- `CONFIG_ZLIB_DEFLATE`:
  - Set to `m`

## 29 - Config no kernel debug

**Summary**: This fragment disables or configures kernel options related to: *config no kernel debug*.

### Configuration options:

## 30 - Config no fs verity securityfs

**Summary**: This fragment disables or configures kernel options related to: *config no fs verity securityfs*.

### Configuration options:

