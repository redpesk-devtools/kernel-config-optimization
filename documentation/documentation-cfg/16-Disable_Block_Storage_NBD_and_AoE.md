# 16 - Disable Block Storage: NBD and AoE

## Summary

This fragment disables network-based block device drivers such as NBD (Network Block Device) and AoE (ATA over Ethernet), which are rarely used in embedded devices.

## Configuration breakdown

### Network block device drivers

```none
        CONFIG_BLK_DEV_NBD
        CONFIG_ATA_OVER_ETH
```


## Where to find a cfg sample


[16-Config-Disabled-Block-NBD-AoE.cf](../../beagle-board/6.6.32/packaging/16-Config-Disabled-Block-NBD-AoE.cfg)