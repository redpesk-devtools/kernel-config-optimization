# 04 - Disable EFI, Power Management Debug and Energy Model

## Summary

This fragment disables EFI runtime services, debugging features for suspend/resume, and the energy model interface. These are often unused in minimal embedded deployments.

## Configuration breakdown

### EFI runtime support

```none
CONFIG_EFI
```

* Disables EFI runtime services, simplifying boot on non-EFI systems.

### Suspend/resume debugging

```none
CONFIG_PM_DEBUG
```

* Disables power management debugging features.

### Energy model

```none
CONFIG_ENERGY_MODEL
```

* Disables the energy-aware scheduling model.

## Where to find a cfg sample

[04-Config-Disabled-EFI-Power-Debug.cfg](../../beagle-board/6.6.32/packaging/04-Config-Disabled-EFI-Power-Debug.cfg)
