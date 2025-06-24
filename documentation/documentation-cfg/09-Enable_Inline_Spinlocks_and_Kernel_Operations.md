# 09 - Enable Inline Spinlocks and Kernel Operations

## Summary

This fragment enables inline implementations of spinlocks and low-level operations to improve performance, especially on uniprocessor systems or simple SMP setups.

## Configuration breakdown

### Inline low-level operations

```none
CONFIG_ARCH_INLINE_SPIN_LOCK
CONFIG_ARCH_INLINE_SPIN_UNLOCK
CONFIG_ARCH_INLINE_SPIN_LOCK_IRQ
CONFIG_ARCH_INLINE_SPIN_UNLOCK_IRQ
```

* Enables inline spinlock implementation.

* Enables inline spin unlock implementation.

* Enables inline spin lock with IRQ.

* Enables inline spin unlock with IRQ.

## Where to find a cfg sample

[09-Config-Arch-Inline-Spinlocks.cfg](https://raw.githubusercontent.com/redpesk-devtools/kernel-config-optimization/refs/heads/master/beagle-board/6.6.32/packaging/09-Config-Arch-Inline-Spinlocks.cfg)
