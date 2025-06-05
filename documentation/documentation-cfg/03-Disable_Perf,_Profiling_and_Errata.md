03 - Disable Perf, Profiling and Errata

Summary: This fragment disables performance monitoring infrastructure, profiling support, and ARM64 CPU errata workarounds, which are not necessary on known good hardware in production embedded systems.
Configuration breakdown:

    Performance events and profiling

        CONFIG_PERF_EVENTS
        CONFIG_PROFILING
        → Disables the performance monitoring infrastructure.

    Paravirtualization support

        CONFIG_PARAVIRT
        → Disables paravirtualization support used in virtual machines.

    ARM64 CPU errata

        CONFIG_ARM64_ERRATUM_843419
        CONFIG_ARM64_ERRATUM_845719
        CONFIG_ARM64_ERRATUM_819472
        CONFIG_ARM64_ERRATUM_832075
        CONFIG_ARM64_ERRATUM_834220
        CONFIG_ARM64_ERRATUM_1742098
        → → No detailed description available.

