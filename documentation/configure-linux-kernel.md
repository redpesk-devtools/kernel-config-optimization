# Configure Linux Kernel

* Kernel-specific optimizations: minimal modules, kernel parameters, initrd, and others
* Building a reduced kernel (with less modules for examples) for faster boot time

Please note in our usecase, we used the [BeagleBoard BeaglePlay](https://docs.redpesk.bzh/docs/en/master/redpesk-os/boards/docs/boards/beagleplay.html) as our reference.

We used Linux kernel version 6.6, you can check some of our sources [here](https://github.com/redpesk-devtools/kernel-config-optimization/tree/master/beagle-board/packaging)

## Generating a .cfg file for Linux Kernel configuration

You may want to customize your Linux Kernel configuration with a configuration fragment (called `cfg`).

An easy way to do that is to:

```bash
cd ${KERNEL_SOURCE}
cp .config .config.sav
make menuconfig
diff --unchanged-line-format= --old-line-format= --new-line-format="%L" ./.config.sav ./.config > 01-my-file.cfg
```

## Merge a .cfg file to Linux Kernel configuration

If you want to merge a cfg configuration fragment to your Linux Kernel configuration just:

```bash
scripts/kconfig/merge_config.sh -m -r .config 01-my-file.cfg
```

If you have more than one cfg files:

```bash
for CFG in *.cfg; do
  scripts/kconfig/merge_config.sh -m -r .config ${CFG}
done
```

## Test your new Kernel

After the build of your kernel packages, you can simply copy them to your board and install them.

```bash
scp ./kernel-modules-extra-${VER}-${REL}.rpbatz.aarch64.rpm \
    ./kernel-modules-${VER}-${REL}.rpbatz.aarch64.rpm \
    ./kernel-core-${VER}-${REL}.rpbatz.aarch64.rpm \
    ./kernel-${VER}-${REL}.rpbatz.aarch64.rpm \
    root@X.X.X.X:/;
ssh root@X.X.X.X dnf install -y /*; 
```

## Disable unused drivers

Disabling unused drivers is a key step in optimizing the boot time of a Linux Kernel, especially for embedded or industrial systems where specific hardware configurations are well-defined.

Use `make menuconfig` to go to the configuration of the Kernel!

*This requires to already have your defconfig declared and used*. For more reference, go [here](https://docs.kernel.org/kbuild/kconfig.html)!

So our goal is to disable unnecessary drivers. Navigate to `Device Drivers` and uncheck drivers not required for the system. See our examples below!

### Tips for safe optimization

* Start with known requirements
  * Clearly define the hardware and peripherals your system uses
* Disable features incrementally
  * Test the system after disabling each set of features to verify functionality
