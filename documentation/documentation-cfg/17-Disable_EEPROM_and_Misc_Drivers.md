# 17 - Disable EEPROM and Misc Drivers

## Summary

This fragment disables support for miscellaneous EEPROM chip drivers and similar devices. These are not required unless interfacing with such chips over SPI or I2C.

## Configuration breakdown

### EEPROM and other embedded chip drivers

```none
        CONFIG_EEPROM_93CX6
        CONFIG_EEPROM_AT25
        CONFIG_MISC_RTSX
```


## Where to find a cfg sample


[17-Config-Eeprom-93CX6-Others-Disabled.cfg](../../beagle-board/6.6.32/packaging/17-Config-Eeprom-93CX6-Others-Disabled.cfg)