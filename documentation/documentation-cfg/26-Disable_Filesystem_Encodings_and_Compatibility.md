# 26 - Disable Filesystem Encodings and Compatibility

## Summary

This fragment disables support for various character encoding and compatibility features used in filesystems, including legacy formats. Helps reduce footprint on systems using only modern filesystems.

## Configuration breakdown

### Encoding and legacy FS support

```none
CONFIG_NLS
CONFIG_VFAT_FS
CONFIG_FAT_DEFAULT_IOCHARSET
```

* Disables Native Language Support for filesystems.

* Disables VFAT filesystem support.

* Disables default charset for FAT filesystem.

## Where to find a cfg sample

[26-Config-Disable-Filesystem-Encodings-and-Compatibility.cfg](../../beagle-board/6.6.32/packaging/26-Config-Disable-Filesystem-Encodings-and-Compatibility.cfg)
