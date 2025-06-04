05 - Disable Schedutil, CPUFreq Governors and Virtualization

Summary: This fragment disables the `schedutil` CPU frequency governor, alternative CPUFreq governors, and virtualization support (like KVM and hypervisors). These options are generally unneeded for real hardware platforms.
Configuration breakdown:

    CPU frequency governor

        CONFIG_CPU_FREQ_DEFAULT_GOV_SCHEDUTIL
        CONFIG_CPU_FREQ_GOV_PERFORMANCE
        CONFIG_CPU_FREQ_GOV_POWERSAVE
        CONFIG_CPU_FREQ_GOV_USERSPACE
        CONFIG_CPU_FREQ_GOV_ONDEMAND
        CONFIG_CPU_FREQ_GOV_CONSERVATIVE
        → Selects `schedutil` as the default CPU frequency governor.

    Virtualization support

        CONFIG_VIRTUALIZATION
        → Disables virtualization extensions and related drivers.

