14 - Disable PCI and Firmware

Summary: This fragment disables PCI subsystem support and firmware loading helpers. Embedded systems often use fixed hardware that doesn't need PCI probing or runtime firmware loading.
Configuration breakdown:

    PCI support and firmware loading

        CONFIG_PCI
        CONFIG_FW_LOADER
        → → No detailed description available.

