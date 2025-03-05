#! /bin/bash

# This is the TIAM62x override file for the core/drivers package split.  The
# module directories listed here and in the generic list in filter-modules.sh
# will be moved to the resulting kernel-modules package for this arch.
# Anything not listed in those files will be in the kernel-core package.
#
# Please review the default list in filter-modules.sh before making
# modifications to the overrides below.  If something should be removed across
# all arches, remove it in the default instead of per-arch.

# driverdirs="scsi/hisi_sas gpu/drm/rcar-du base/regmap"
usbdrvs="atm image misc serial wusbcore gadget/function"

inputdrvs="joystick gameport tablet touchscreen"

driverdirs="atm auxdisplay bcma bluetooth firewire fmc fpga infiniband isdn leds media memstick mfd mmc mtd nfc ntb pcmcia platform power ssb soundwire staging tty uio uwb w1"

scsidrvs="aacraid advansys aic7xxx aic94xx be2iscsi bfa bnx2i bnx2fc csiostor cxgbi esas2r fcoe fnic isci lpfc megaraid mpt2sas mpt3sas mvsas pm8001 qla2xxx qla4xxx sym53c8xx_2 ufs qedf wd719x"

netprots="6lowpan appletalk atm ax25 batman-adv bluetooth can dccp dsa ieee802154 irda l2tp mac80211 mac802154 mpls netrom nfc rds rose sctp smc wireless"

drmdrvs="amd ast gma500 i2c i915 mgag200 nouveau panel radeon"

sounddrvs="ac97 aoa arm atmel drivers firewire hda i2c isa mips oss parisc pci pcmcia ppc sh soc sparc spi synth usb x86 xen"

fsdrvs="md-cluster gfs2"
