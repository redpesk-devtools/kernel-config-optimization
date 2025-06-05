10 - Disable Swap, Memory Hotplug and KSM

Summary: This fragment disables features that support virtual memory management enhancements like swap, memory hotplug, and memory page merging. Useful for systems with fixed RAM and no swapping.
Configuration breakdown:

    Memory management features

        CONFIG_SWAP
        CONFIG_MEMORY_HOTPLUG
        CONFIG_KSM
        → Disables swap space support.

