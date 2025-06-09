# 22 - Disable Serial, TTY and TPM

## Summary

This fragment disables serial communication interfaces, traditional TTY subsystems, and Trusted Platform Module support. These are unneeded on secure, self-contained systems.

## Configuration breakdown

### TTY and serial devices

```none
CONFIG_SERIAL_8250
CONFIG_TTY
CONFIG_VT
```

* Disables standard 8250 UART serial support.

* Disables generic TTY subsystem.

* Disables virtual terminal support.

### Trusted computing

```none
CONFIG_TCG_TPM
```

* Disables TPM (Trusted Platform Module) support.

## Where to find a cfg sample

[22-Config-Disable-Serial-TTY-and-TPM.cfg](../../beagle-board/6.6.32/packaging/22-Config-Disable-Serial-TTY-and-TPM.cfg)
