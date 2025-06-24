# 11 - Disable Networking: IPv4, IPv6, Netfilter

## Summary

This fragment disables major networking protocols and packet filtering subsystems. Useful for systems that don't require full networking stacks, such as headless nodes or minimal appliances.

## Configuration breakdown:

### Networking core and protocols

```none
        CONFIG_INET
        CONFIG_IPV6
```

### Netfilter (firewall and packet mangling)

```none
        CONFIG_NETFILTER
        CONFIG_NF_TABLES
        CONFIG_NF_CONNTRACK
```


## Where to find a cfg sample


[11-Config-Disabled-Network-IPV4-IPV6-Netfilter.cfg](https://raw.githubusercontent.com/redpesk-devtools/kernel-config-optimization/refs/heads/master/beagle-board/6.6.32/packaging/11-Config-Disabled-Network-IPV4-IPV6-Netfilter.cfg)