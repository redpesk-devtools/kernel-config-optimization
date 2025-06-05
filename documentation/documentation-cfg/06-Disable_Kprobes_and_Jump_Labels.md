06 - Disable Kprobes and Jump Labels

Summary: This fragment disables advanced kernel tracing and optimization mechanisms such as kprobes and jump labels. These are mostly useful for debugging or performance tuning during development.
Configuration breakdown:

    Dynamic instrumentation

        CONFIG_KPROBES
        → Disables dynamic probes used for debugging kernel internals.

    Jump label optimization

        CONFIG_JUMP_LABEL
        → Disables static branching optimization using jump labels.

