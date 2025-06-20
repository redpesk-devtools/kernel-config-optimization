# 19 - Disable PHY Drivers

## Summary

This fragment disables PHY (physical layer) drivers for Ethernet and similar hardware interfaces, which are not needed when no wired interfaces are present.

## Configuration breakdown

### PHY drivers

```none
        CONFIG_AMD_PHY
        CONFIG_MARVELL_PHY
        CONFIG_REALTEK_PHY
```


## Where to find a cfg sample


[19-Config-Disabled-PHY-Drivers.cfg](../../beagle-board/6.6.32/packaging/19-Config-Disabled-PHY-Drivers.cfg)