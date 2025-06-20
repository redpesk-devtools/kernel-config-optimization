# 07 - Disable GCC Plugins and Function Alignment

## Summary

This fragment disables the use of GCC compiler plugins and specific function alignment settings. These options can slightly reduce binary size and complexity when such features are not needed.

## Configuration breakdown

### GCC plugin support

```none
CONFIG_GCC_PLUGINS
```

* Disables all GCC plugin support, reducing build complexity.

### Function alignment

```none
CONFIG_FUNCTION_ALIGNMENT_32B
CONFIG_FUNCTION_ALIGNMENT
```

* Avoids alignment of functions to 32-byte boundaries.

* Disables custom function alignment.

## Where to find a cfg sample

[07-Config-No-GCC-Plugins-Block-Align.cfg](../../beagle-board/6.6.32/packaging/07-Config-No-GCC-Plugins-Block-Align.cfg)
