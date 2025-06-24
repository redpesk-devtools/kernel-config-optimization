# 20 - Disable PPP, WLAN Coexistence, and Failover

## Summary

This fragment disables Point-to-Point Protocol (PPP), Wi-Fi coexistence support, and failover mechanisms. These features are typically used in more complex networking environments.

## Configuration breakdown

### PPP, coexistence and failover

```none
        CONFIG_PPP
        CONFIG_WLAN_VENDOR_INTEL
        CONFIG_NET_FAILOVER
```


## Where to find a cfg sample


[20-Config-No-PPP-WLAN-Yes-Failover.cfg](https://raw.githubusercontent.com/redpesk-devtools/kernel-config-optimization/refs/heads/master/beagle-board/6.6.32/packaging/20-Config-No-PPP-WLAN-Yes-Failover.cfg)