13 - Disable Wireless, Bluetooth, CAN and RFKILL

Summary: This fragment disables wireless communications including Wi-Fi, Bluetooth, CAN bus, and radio frequency kill switch support. Ideal for wired or non-networked embedded devices.
Configuration breakdown:

    Wireless and Bluetooth drivers

        CONFIG_CFG80211
        CONFIG_MAC80211
        CONFIG_RFKILL
        CONFIG_BT
        → → No detailed description available.

    CAN bus

        CONFIG_CAN
        → → No detailed description available.


## Where to find a cfg sample


[13-Config-Disabled-Wireless-BT-CAN-RFKILL.cfg](../../beagle-board/6.6.32/packaging/13-Config-Disabled-Wireless-BT-CAN-RFKILL.cfg)