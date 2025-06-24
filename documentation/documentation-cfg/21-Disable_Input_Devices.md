# 21 - Disable Input Devices

## Summary

This fragment disables support for most input devices such as keyboards, mice, joysticks, and touchscreens. It is intended for headless or appliance-style systems.

## Configuration breakdown

### General input devices

```none
CONFIG_INPUT_KEYBOARD
CONFIG_INPUT_MOUSE
CONFIG_INPUT_JOYSTICK
CONFIG_INPUT_TOUCHSCREEN
```

* Disables keyboard input support.

* Disables mouse input support.

* Disables joystick input support.

* Disables touchscreen input support.

## Where to find a cfg sample

[21-Config-No-Input-Devices.cfg](https://raw.githubusercontent.com/redpesk-devtools/kernel-config-optimization/refs/heads/master/beagle-board/6.6.32/packaging/21-Config-No-Input-Devices.cfg)
