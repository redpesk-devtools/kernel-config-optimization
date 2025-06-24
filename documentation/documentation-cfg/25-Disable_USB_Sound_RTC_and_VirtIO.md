# 25 - Disable USB, Sound, RTC and VirtIO

## Summary

This fragment disables USB peripheral support, sound subsystems, real-time clock interfaces, and VirtIO virtualization support. Useful on minimal embedded devices.

## Configuration breakdown

### Peripheral and virtual interfaces

```none
CONFIG_USB_SUPPORT
CONFIG_SOUND
CONFIG_RTC_CLASS
CONFIG_VIRTIO
```

* Disables USB support.

* Disables audio subsystem.

* Disables real-time clock driver framework.

* Disables VirtIO virtualization support.

## Where to find a cfg sample

[25-Config-No-USB-Sound-RTC-VirtIO.cfg](https://raw.githubusercontent.com/redpesk-devtools/kernel-config-optimization/refs/heads/master/beagle-board/6.6.32/packaging/25-Config-No-USB-Sound-RTC-VirtIO.cfg)
