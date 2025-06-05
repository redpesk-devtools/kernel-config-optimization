24 - Disable MFD, Display and Media Drivers

Summary: This fragment disables support for multi-function devices (MFDs), display interfaces and multimedia frameworks, saving memory and kernel space on non-GUI systems.
Configuration breakdown:

    MFD and display/media interfaces

        CONFIG_MFD_CORE
        CONFIG_FB
        CONFIG_MEDIA_SUPPORT
        → → No detailed description available.

