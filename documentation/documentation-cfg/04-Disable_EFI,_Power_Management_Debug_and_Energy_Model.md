04 - Disable EFI, Power Management Debug and Energy Model

Summary: This fragment disables EFI runtime services, debugging features for suspend/resume, and the energy model interface. These are often unused in minimal embedded deployments.
Configuration breakdown:

    EFI runtime support

        CONFIG_EFI
        → Disables EFI runtime support.

    Suspend/resume debugging

        CONFIG_PM_DEBUG
        → Disables debug support for power management.

    Energy model

        CONFIG_ENERGY_MODEL
        → Disables kernel energy-aware scheduling support.

