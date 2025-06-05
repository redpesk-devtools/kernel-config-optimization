08 - Disable Partition Parsers

Summary: This fragment disables support for several types of partition table parsers. These are only needed when the system must recognize and handle partitioned storage devices.
Configuration breakdown:

    Partition parsers

        CONFIG_KARMA_PARTITION
        CONFIG_EFI_PARTITION
        CONFIG_SYSV68_PARTITION
        → Disables Karma partition table parsing.

