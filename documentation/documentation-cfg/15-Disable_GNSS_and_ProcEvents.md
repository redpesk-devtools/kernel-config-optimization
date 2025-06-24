# 15 - Disable GNSS and ProcEvents

## Summary

This fragment disables GNSS (Global Navigation Satellite System) support and kernel event exporting through procfs. Suitable for devices not relying on location services or user-space tracking.

## Configuration breakdown

### Location and process event support

```none
        CONFIG_GNSS
        CONFIG_PROC_EVENTS
```


## Where to find a cfg sample


[15-Config-No-GNSS-ProcEvents.cfg](https://raw.githubusercontent.com/redpesk-devtools/kernel-config-optimization/refs/heads/master/beagle-board/6.6.32/packaging/15-Config-No-GNSS-ProcEvents.cfg)