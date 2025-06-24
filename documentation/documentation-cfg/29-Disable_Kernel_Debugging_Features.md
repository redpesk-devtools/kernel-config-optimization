# 29 - Disable Kernel Debugging Features

## Summary

This fragment disables debugging options in the kernel to save memory and avoid unnecessary overhead in production builds.

## Configuration breakdown

### Debugging and instrumentation

```none
CONFIG_DEBUG_KERNEL
CONFIG_KGDB
CONFIG_DEBUG_INFO
```

* Disables general kernel debugging.

* Disables Kernel GNU Debugger support.

* Disables generation of debug info in build.

## Where to find a cfg sample

[29-Config-No-Kernel-Debug.cfg](https://raw.githubusercontent.com/redpesk-devtools/kernel-config-optimization/refs/heads/master/beagle-board/6.6.32/packaging/29-Config-No-Kernel-Debug.cfg)
