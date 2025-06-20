# 18 - Disable Network Device Drivers

## Summary

This fragment disables support for network interface drivers, including bonding and vendor-specific devices. This suits devices without any Ethernet or Wi-Fi hardware.

## Configuration breakdown

### Network drivers and bonding

```none
        CONFIG_NET_VENDOR_REALTEK
        CONFIG_NET_VENDOR_INTEL
        CONFIG_BONDING
```


## Where to find a cfg sample


[18-Config-No-Network-Devices-Bond-Vendor.cfg](../../beagle-board/6.6.32/packaging/18-Config-No-Network-Devices-Bond-Vendor.cfg)