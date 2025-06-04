29 - Disable Kernel Debugging Features

Summary: This fragment disables debugging options in the kernel to save memory and avoid unnecessary overhead in production builds.
Configuration breakdown:

    Debugging and instrumentation

        CONFIG_DEBUG_KERNEL
        CONFIG_KGDB
        CONFIG_DEBUG_INFO
        → → No detailed description available.

