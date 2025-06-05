01 - Disable IPC, Timers and Audit

Summary: This fragment disables legacy inter-process communication features, auditing, high-resolution timers, and several process accounting/statistics options. These features are often unnecessary in embedded systems where resource usage must be minimal and predictable.
Configuration breakdown:

    System V IPC and message queues

        CONFIG_SYSVIPC
        CONFIG_POSIX_MQUEUE
        CONFIG_CROSS_MEMORY_ATTACH
        → Disables System V-style inter-process communication (IPC) mechanisms like message queues and semaphores.

    Kernel auditing system

        CONFIG_AUDIT
        → Disables the audit subsystem, reducing kernel size and improving performance when auditing is not needed.

    High-resolution timers

        CONFIG_HIGH_RES_TIMERS
        → Disables high-resolution timer support; lowers precision but reduces timer overhead.

    Preemption model

        CONFIG_PREEMPT_VOLUNTARY_BUILD
        CONFIG_PREEMPT_DYNAMIC
        → Selects voluntary kernel preemption for a balance between performance and latency.

    Process accounting and task statistics

        CONFIG_BSD_PROCESS_ACCT
        CONFIG_TASKSTATS
        → Disables BSD-style process accounting.

    Pressure Stall Information

        CONFIG_PSI
        → Disables Pressure Stall Information (PSI) for monitoring resource pressure.

