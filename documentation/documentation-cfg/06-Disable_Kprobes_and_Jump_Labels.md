# 06 - Disable Kprobes and Jump Labels

## Summary

This fragment disables advanced kernel tracing and optimization mechanisms such as kprobes and jump labels. These are mostly useful for debugging or performance tuning during development.

## Configuration breakdown

### Dynamic instrumentation

```none
CONFIG_KPROBES
```

* Disables dynamic probes used for kernel debugging.

### Jump label optimization

```none
CONFIG_JUMP_LABEL
```

* Disables static branching optimization using jump labels.

## Where to find a cfg sample

[06-Config-Disable-Kprobes-and-Jump-Labels.cfg](../../beagle-board/6.6.32/packaging/06-Config-Disable-Kprobes-and-Jump-Labels.cfg)
