26 - Disable Filesystem Encodings and Compatibility

Summary: This fragment disables support for various character encoding and compatibility features used in filesystems, including legacy formats. Helps reduce footprint on systems using only modern filesystems.
Configuration breakdown:

    Encoding and legacy FS support

        CONFIG_NLS
        CONFIG_VFAT_FS
        CONFIG_FAT_DEFAULT_IOCHARSET
        → → No detailed description available.

