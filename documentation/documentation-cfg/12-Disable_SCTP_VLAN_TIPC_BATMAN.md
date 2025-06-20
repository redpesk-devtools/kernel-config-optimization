12 - Disable SCTP, VLAN, TIPC, BATMAN

Summary: This fragment removes support for specialized networking protocols like SCTP, VLAN, TIPC, and BATMAN routing. These are often unused in embedded applications.
Configuration breakdown:

    Specialized networking protocols

        CONFIG_SCTP
        CONFIG_VLAN_8021Q
        CONFIG_TIPC
        CONFIG_BATMAN_ADV
        → → No detailed description available.


## Where to find a cfg sample


[12-Config-SCTP-No-VLAN-TIPC-BATMAN.cfg](../../beagle-board/6.6.32/packaging/12-Config-SCTP-No-VLAN-TIPC-BATMAN.cfg)
