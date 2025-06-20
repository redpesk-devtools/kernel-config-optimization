# 10 - Disable Swap, Memory Hotplug and KSM

## Summary

This fragment disables features that support virtual memory management enhancements like swap, memory hotplug, and memory page merging. Useful for systems with fixed RAM and no swapping.

## Configuration breakdown

### Memory management features

```none
CONFIG_SWAP
CONFIG_MEMORY_HOTPLUG
CONFIG_KSM
```

* Disables swap support.

* Disables memory hotplugging capability.

* Disables Kernel Samepage Merging.

## Where to find a cfg sample

[10-Config-No-Swap-Hotplug-KSM.cfg](../../beagle-board/6.6.32/packaging/10-Config-No-Swap-Hotplug-KSM.cfg)
