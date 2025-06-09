# 30 - Disable Filesystem Verity and SecurityFS

## Summary

This fragment disables integrity verification and internal security-related filesystems. These are only required for advanced security policies and attestation.

## Configuration breakdown

### Security and integrity interfaces

```none
CONFIG_FS_VERITY
CONFIG_SECURITYFS
```

* Disables support for file-based integrity verification.

* Disables internal security filesystem.

## Where to find a cfg sample

[30-Config-Disable-Filesystem-Verity-and-SecurityFS.cfg](../../beagle-board/6.6.32/packaging/30-Config-Disable-Filesystem-Verity-and-SecurityFS.cfg)
