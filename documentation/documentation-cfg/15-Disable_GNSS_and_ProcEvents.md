15 - Disable GNSS and ProcEvents

Summary: This fragment disables GNSS (Global Navigation Satellite System) support and kernel event exporting through procfs. Suitable for devices not relying on location services or user-space tracking.
Configuration breakdown:

    Location and process event support

        CONFIG_GNSS
        CONFIG_PROC_EVENTS
        → → No detailed description available.


## Where to find a cfg sample


[15-Config-No-GNSS-ProcEvents.cfg](../../beagle-board/6.6.32/packaging/15-Config-No-GNSS-ProcEvents.cfg)