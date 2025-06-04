18 - Disable Network Device Drivers

Summary: This fragment disables support for network interface drivers, including bonding and vendor-specific devices. This suits devices without any Ethernet or Wi-Fi hardware.
Configuration breakdown:

    Network drivers and bonding

        CONFIG_NET_VENDOR_REALTEK
        CONFIG_NET_VENDOR_INTEL
        CONFIG_BONDING
        → → No detailed description available.

