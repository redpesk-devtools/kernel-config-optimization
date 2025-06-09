# 08 - Disable Partition Parsers

## Summary

This fragment disables support for several types of partition table parsers. These are only needed when the system must recognize and handle partitioned storage devices.

## Configuration breakdown

### Partition parsers

```none
CONFIG_KARMA_PARTITION
CONFIG_EFI_PARTITION
CONFIG_SYSV68_PARTITION
```

* Disables Karma partition table parsing.

* Disables EFI/GPT partition support.

* Disables SYSV68 partition support.

## Where to find a cfg sample

[08-Config-Disable-Partition-Parsers.cfg](../../beagle-board/6.6.32/packaging/08-Config-Disable-Partition-Parsers.cfg)
