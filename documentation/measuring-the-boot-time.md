
# Measuring the boot time

* Overview of boot time measurement.
* Tools to measure boot time (e.g., systemd-analyze, dmesg, bootchart).
* How to track boot events and milestones.

Measuring the Linux boot time involves capturing how long it takes for the system to transition from power-on or bootloader execution to a fully operational state. Here’s a step-by-step guide:

## Define the start and end points

* Start Point:
  Power-on or the bootloader's first activity.
* End Point:
  When a specific service or application is ready. The appearance of a login prompt or GUI. A signal sent from the system (e.g., a network connection established).

## Methods to measure boot time

* Using Bootloader (e.g., U-Boot) Timestamps
  Enable verbose output in the bootloader. Add timestamps to bootloader messages to measure the time spent in firmware and bootloader stages.
* Using Kernel Boot Logs
  Enable Kernel Timestamps: Pass time or initcall_debug as a boot parameter in the kernel command line.
  Example Add:

  ```bash
  loglevel=8 time initcall_debug
  ```

  loglevel=8: Ensures all messages are displayed, including debug messages.
  time: Displays timestamps for each log entry relative to the boot start.
  initcall_debug: This shows the time taken by each kernel subsystem or driver initialization function. to the bootloader configuration.

* Analyze Dmesg Logs:
  Run dmesg after boot to see timestamps for kernel initialization. Subtract the initial timestamp from the last timestamp to calculate boot time.
* Using systemd-analyze (For Systemd-based Systems)
  Install and run systemd-analyze
* systemd-analyze: This displays the total boot time split into kernel, initramfs, and user space.
  To generate a svg file:

  ```bash
  systemd-analyze
  ```

  ```bash
   systemd-analyze plot > /tmp/bootup.svg
  ```

  To see the time taken by each service:

  ```bash
  systemd-analyze blame
  ```

  For a detailed breakdown:

  ```bash
    systemd-analyze critical-chain
  ```

  * [systemd-analyze](https://www.freedesktop.org/software/systemd/man/latest/systemd-analyze.html)

* Using UART or Serial Console Logs
  Connect to the device's serial console using a tool like picocom or putty. Capture the boot log and note the timestamps. Measure from the first log line (e.g., bootloader starting) to the desired milestone.

* Using GPIO and Oscilloscope/Logic Analyzer
  Configure a GPIO pin to toggle high when the kernel starts and low when the application is ready. Measure the time difference between the toggles using an oscilloscope or logic analyzer. This method is especially useful for real-time, hardware-accurate boot time measurements.

* Measure Time to User Space
  To measure the time taken to reach user space, note the timestamp of the following message in dmesg:

  ```bash
    [    X.XXXXX] Run /sbin/init as init process
  ```

  Subtract the kernel start time (typically [0.000000]) from the timestamp of this message.

* Bootchart analysis
  Install systemd-bootchart. Enable bootchart by adding `init=/usr/lib/systemd/systemd-bootchart` to the kernel command line. Boot the system and review the generated chart in /var/log/bootchart/.

WARNING:

For systemd-bootchart, several proc debug interfaces are required in the kernel config:
  `CONFIG_SCHEDSTATS`
below is optional, for additional info:
  `CONFIG_SCHED_DEBUG`

* Optimize and Re-Test
  After measuring, identify bottlenecks using the detailed logs (e.g., long-running services, slow hardware initialization). Apply optimizations and repeat measurements to evaluate improvements.

By combining these methods, you can pinpoint where time is spent during boot and systematically reduce it.

## Using bootloader timestamps

### Enable timestamp logging in U-Boot

Configure U-Boot to enable timestamps:
Open the U-Boot configuration file, typically located in the source tree as .config.
Enable the `CONFIG_BOOTSTAGE` option:

```bash
    CONFIG_BOOTSTAGE=y
```

or with menuconfig

```bash
    make menuconfig
    Boot options  ---> Boot timing  ---> [ ] Boot timing and reporting 
```

This activates the bootstage feature in U-Boot, which records timestamps during the boot process.

And now rebuild U-Boot.
Flash the compiled U-Boot binary to your device. Ensure that you have the correct flashing tool and binary format for your hardware.

### Modify U-Boot to add explicit timestamp logging

If timestamps are not available natively or additional granularity is needed, you can modify the source code:

Edit the `common/board_r.c` File:

Add timestamp logging at key points in the U-Boot source code, such as:

* Start of U-Boot execution.
* Device initialization (e.g., storage, network, display).
* Handoff to the Linux kernel.

Example:

```C
static int initr_bootstage(void)
{

        printf("U-Boot start timestamp: %lu ms\n", get_timer(0));
        bootstage_mark_name(BOOTSTAGE_ID_START_UBOOT_R, "board_init_r");
        printf("Kernel handoff timestamp: %lu ms\n", get_timer(0));
        return 0;
}

```

Use the `get_timer()` API:

The `get_timer()` function returns the elapsed time in milliseconds since the last reset.

### Access the bootstage logs

Print bootstage information:

After enabling `CONFIG_BOOTSTAGE`, U-Boot will automatically log timestamps to the serial console if the bootstage commands are enabled.
Use the bootstage command in U-Boot to print timestamps:

```bash
    bootstage
```

Analyze bootstage output:

The output will include timestamps and labels for each recorded stage, such as:

```bash
        ID    Stage                             Time (ms)
        0     U-Boot Start                      0
        1     Device Initialization             120
        2     Handoff to Kernel                 340
```

### Save logs for analysis

Use a serial console tool (e.g., picocom, screen, or putty) to capture the output from the UART/serial console.
Redirect the output to a log file for later analysis.

#### Use bootloader environment variables

For additional timing markers, you can use U-Boot environment variables:

Add environment commands to measure time explicitly, e.g.:

```bash
    setenv start_time ${time}
    run load_kernel
    setenv kernel_time ${time}
```

Subtract the values later for measuring elapsed times.

By enabling and using timestamps in U-Boot, you can accurately measure the time spent in the firmware and bootloader stages, allowing you to identify and optimize any bottlenecks.

## Optimize kernel boot time

### Optimize initramfs

If you are using an initramfs, reduce its size and contents by including only necessary modules and binaries. Measure the time taken to mount the root filesystem in dmesg:

```bash
    [    X.XXXXX] VFS: Mounted root (ext4 filesystem) on device 8:1.
```

### Profile boot with ftrace

Use the kernel's ftrace tool to get detailed timing information:

* Enable `CONFIG_FUNCTION_TRACER` and related options in the kernel.
* Mount the tracefs filesystem

```bash
mount -t tracefs nodev /sys/kernel/debug/tracing

Start tracing:

echo function_graph > /sys/kernel/debug/tracing/current_tracer
```

  Analyze the trace file:

```bash
        cat /sys/kernel/debug/tracing/trace
```

### Optimize the slow subsystems

Optimizing slow subsystems in Linux requires a systematic approach to identifying bottlenecks, reducing overhead, and fine-tuning the kernel, services, and drivers. This guide provides a comprehensive strategy for addressing slow subsystems in Linux, particularly in embedded or industrial environments where performance and startup time are critical.

### Identify slow drivers or services

The initcall_debug kernel parameter is a powerful tool for debugging and optimizing the boot time of a Linux kernel. It provides detailed insights into the initialization process of various kernel components, allowing you to identify and address bottlenecks.

What is initcall_debug?

When initcall_debug is passed as a kernel parameter, it enables detailed logging of the initialization times for all functions invoked during the kernel's initialization phase. This includes initcalls for drivers, subsystems, and other components.

Each initcall logs:

* Start of Initialization: The name of the function being called.
* End of Initialization: The return value and the time taken to execute the function.

How to Use **initcall_debug** ?

* Add initcall_debug to the Kernel Command Line:
  * Edit your bootloader configuration
  * Append **initcall_debug** to the kernel command line

```bash
linux /boot/vmlinuz-linux root=/dev/sda1 initcall_debug
```

  * Save the changes and reboot the system.
* View the output in logs
  * Once the system boots, check the kernel logs using dmesg

```bash
dmesg | grep initcall
```

  * Alternatively, view logs from the serial console or a log file if the system is headless.

Example output:

```bash
[    0.123456] calling  init_memory_subsystem+0x0/0x100
[    0.234567] initcall init_memory_subsystem+0x0/0x100 returned 0 after 111 ms
[    0.345678] calling  init_networking+0x0/0x200
[    0.456789] initcall init_networking+0x0/0x200 returned 0 after 111 ms
```

Key details:

* calling: Indicates the function being called.
* returned: Indicates the return status (e.g., 0 for success).
* after: Shows the time taken to execute the function in milliseconds.

Kernel initcall levels:

Initcalls in the kernel are categorized into levels based on when they are executed during boot:

* `pure_initcall`: Runs as early as possible.
* `core_initcall`: Initializes core kernel components.
* `postcore_initcall`: Runs after the core initcalls.
* `arch_initcall`: Architecture-specific initialization.
* `subsys_initcall`: Subsystem initialization.
* `fs_initcall`: Filesystem initialization.
* `device_initcall`: Device driver initialization.
* `late_initcall`: Late initialization tasks.

initcall_debug logs the execution time for each of these levels, helping you identify the stage where bottlenecks occur.
