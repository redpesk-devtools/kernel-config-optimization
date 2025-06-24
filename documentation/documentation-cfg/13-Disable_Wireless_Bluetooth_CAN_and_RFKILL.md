# 13 - Disable Wireless, Bluetooth, CAN and RFKILL

## Summary

This fragment disables wireless communications including Wi-Fi, Bluetooth, CAN bus, and radio frequency kill switch support. Ideal for wired or non-networked embedded devices.

## Configuration breakdown

### Wireless and Bluetooth drivers

```none
        CONFIG_CFG80211
        CONFIG_MAC80211
        CONFIG_RFKILL
        CONFIG_BT
```

### CAN bus

```none
        CONFIG_CAN
```


## Where to find a cfg sample


[13-Config-Disabled-Wireless-BT-CAN-RFKILL.cfg](https://raw.githubusercontent.com/redpesk-devtools/kernel-config-optimization/refs/heads/master/beagle-board/6.6.32/packaging/13-Config-Disabled-Wireless-BT-CAN-RFKILL.cfg)