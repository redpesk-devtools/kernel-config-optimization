# 03 - Disable Perf, Profiling and Errata

## Summary

This fragment disables performance monitoring infrastructure, profiling support, and ARM64 CPU errata workarounds, which are not necessary on known good hardware in production embedded systems.

## Configuration breakdown

### Performance events and profiling

```none
CONFIG_PERF_EVENTS
CONFIG_PROFILING
```

* Disables the performance monitoring infrastructure.

* Disables profiling support.

### Paravirtualization support

```none
CONFIG_PARAVIRT
```

* Disables paravirtualization support used in virtual machines.

### ARM64 CPU errata

```none
CONFIG_ARM64_ERRATUM_843419
CONFIG_ARM64_ERRATUM_845719
CONFIG_ARM64_ERRATUM_819472
CONFIG_ARM64_ERRATUM_832075
CONFIG_ARM64_ERRATUM_834220
CONFIG_ARM64_ERRATUM_1742098
```

* Disables workaround for ARM64 erratum 843419.

* Disables workaround for ARM64 erratum 845719.

* Disables workaround for ARM64 erratum 819472.

* Disables workaround for ARM64 erratum 832075.

* Disables workaround for ARM64 erratum 834220.

* Disables workaround for ARM64 erratum 1742098.

## Where to find a cfg sample

[03-Config-Disabled-Perf-Profiling-Errata.cfg](../../beagle-board/6.6.32/packaging/03-Config-Disabled-Perf-Profiling-Errata.cfg)
