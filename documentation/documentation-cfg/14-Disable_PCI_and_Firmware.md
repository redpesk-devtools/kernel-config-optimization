# 14 - Disable PCI and Firmware

## Summary

This fragment disables PCI subsystem support and firmware loading helpers. Embedded systems often use fixed hardware that doesn't need PCI probing or runtime firmware loading.

## Configuration breakdown

### PCI support and firmware loading

```none
        CONFIG_PCI
        CONFIG_FW_LOADER
```

## Where to find a cfg sample


[14-Config-Disabled-PCI-Firmware.cfg](https://raw.githubusercontent.com/redpesk-devtools/kernel-config-optimization/refs/heads/master/beagle-board/6.6.32/packaging/14-Config-Disabled-PCI-Firmware.cfg)