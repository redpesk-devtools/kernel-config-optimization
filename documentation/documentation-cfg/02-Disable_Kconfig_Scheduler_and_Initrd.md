# 02 - Disable Kconfig, Scheduler and Initrd

## Summary

This fragment disables kernel configuration debugging options, scheduler tracing mechanisms, and initial RAM disk (initrd) support. These features are mostly unnecessary in embedded systems with static root filesystems and limited resources.

## Configuration breakdown

### Kconfig debugging options

```none
CONFIG_IKCONFIG
CONFIG_IKCONFIG_PROC
```

* Disables embedding of the kernel .config file.

* Disables access to configuration through /proc/config.gz.

### Scheduler debugging and tracing

```none
CONFIG_SCHED_DEBUG
```

* Disables detailed scheduler stats and debug code.

### Initial RAM disk support

```none
CONFIG_BLK_DEV_INITRD
```

* Disables initrd/initramfs support, reducing early boot complexity.

## Where to find a cfg sample

[02-Config-Disable-Kconfig-Scheduler-and-Initrd.cfg](../../beagle-board/6.6.32/packaging/02-Config-Disable-Kconfig-Scheduler-and-Initrd.cfg)
