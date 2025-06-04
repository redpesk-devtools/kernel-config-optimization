30 - Disable Filesystem Verity and SecurityFS

Summary: This fragment disables integrity verification and internal security-related filesystems. These are only required for advanced security policies and attestation.
Configuration breakdown:

    Security and integrity interfaces

        CONFIG_FS_VERITY
        CONFIG_SECURITYFS
        → → No detailed description available.

