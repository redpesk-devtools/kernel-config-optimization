09 - Enable Inline Spinlocks and Kernel Operations

Summary: This fragment enables inline implementations of spinlocks and low-level operations to improve performance, especially on uniprocessor systems or simple SMP setups.
Configuration breakdown:

    Inline low-level operations

        CONFIG_ARCH_INLINE_SPIN_LOCK
        CONFIG_ARCH_INLINE_SPIN_UNLOCK
        CONFIG_ARCH_INLINE_SPIN_LOCK_IRQ
        CONFIG_ARCH_INLINE_SPIN_UNLOCK_IRQ
        → → No detailed description available.

