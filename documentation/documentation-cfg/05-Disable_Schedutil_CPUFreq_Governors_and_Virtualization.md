# 05 - Disable Schedutil, CPUFreq Governors and Virtualization

## Summary

This fragment disables the `schedutil` CPU frequency governor, alternative CPUFreq governors, and virtualization support (like KVM and hypervisors). These options are generally unneeded for real hardware platforms.

## Configuration breakdown

### CPU frequency governor

```none
CONFIG_CPU_FREQ_DEFAULT_GOV_SCHEDUTIL
CONFIG_CPU_FREQ_GOV_PERFORMANCE
CONFIG_CPU_FREQ_GOV_POWERSAVE
CONFIG_CPU_FREQ_GOV_USERSPACE
CONFIG_CPU_FREQ_GOV_ONDEMAND
CONFIG_CPU_FREQ_GOV_CONSERVATIVE
```

* Avoids using schedutil as the default governor.

* Disables performance CPUFreq governor.

* Disables powersave CPUFreq governor.

* Disables userspace CPUFreq governor.

* Disables ondemand CPUFreq governor.

* Disables conservative CPUFreq governor.

### Virtualization support

```none
CONFIG_VIRTUALIZATION
```

* Disables virtualization extensions and related drivers.

## Where to find a cfg sample

[05-Config-Disable-Schedutil-CPUFreq-Governors-and-Virtualization.cfg](../../beagle-board/6.6.32/packaging/05-Config-Disable-Schedutil-CPUFreq-Governors-and-Virtualization.cfg)
