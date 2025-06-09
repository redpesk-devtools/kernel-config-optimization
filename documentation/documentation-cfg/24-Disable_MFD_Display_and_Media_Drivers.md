# 24 - Disable MFD, Display and Media Drivers

## Summary

This fragment disables support for multi-function devices (MFDs), display interfaces and multimedia frameworks, saving memory and kernel space on non-GUI systems.

## Configuration breakdown

### MFD and display/media interfaces

```none
CONFIG_MFD_CORE
CONFIG_FB
CONFIG_MEDIA_SUPPORT
```

* Disables Multi-Function Device core support.

* Disables framebuffer device support.

* Disables multimedia subsystem.

## Where to find a cfg sample

[24-Config-Disable-MFD-Display-and-Media-Drivers.cfg](../../beagle-board/6.6.32/packaging/24-Config-Disable-MFD-Display-and-Media-Drivers.cfg)
