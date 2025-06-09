19 - Disable PHY Drivers

Summary: This fragment disables PHY (physical layer) drivers for Ethernet and similar hardware interfaces, which are not needed when no wired interfaces are present.
Configuration breakdown:

    PHY drivers

        CONFIG_AMD_PHY
        CONFIG_MARVELL_PHY
        CONFIG_REALTEK_PHY
        → → No detailed description available.