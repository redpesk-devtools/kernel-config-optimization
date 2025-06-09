16 - Disable Block Storage: NBD and AoE

Summary: This fragment disables network-based block device drivers such as NBD (Network Block Device) and AoE (ATA over Ethernet), which are rarely used in embedded devices.
Configuration breakdown:

    Network block device drivers

        CONFIG_BLK_DEV_NBD
        CONFIG_ATA_OVER_ETH
        → → No detailed description available.

