14 - Disable PCI and Firmware

Summary: This fragment disables PCI subsystem support and firmware loading helpers. Embedded systems often use fixed hardware that doesn't need PCI probing or runtime firmware loading.
Configuration breakdown:

    PCI support and firmware loading

        CONFIG_PCI
        CONFIG_FW_LOADER
        → → No detailed description available.


## Where to find a cfg sample


[14-Config-Disabled-PCI-Firmware.cfg](../../beagle-board/6.6.32/packaging/14-Config-Disabled-PCI-Firmware.cfg)