02 - Disable Kconfig, Scheduler and Initrd

Summary: This fragment disables scheduler tracing options, initial RAM disk (initrd) support, and other Kconfig debugging features. These options are not needed in most embedded systems with static root filesystems.
Configuration breakdown:

    Kconfig debugging options

        CONFIG_IKCONFIG
        CONFIG_IKCONFIG_PROC
        → → No detailed description available.

    Scheduler debugging and tracing

        CONFIG_SCHED_DEBUG
        → → No detailed description available.

    Initial RAM disk support

        CONFIG_BLK_DEV_INITRD
        → → No detailed description available.

