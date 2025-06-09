17 - Disable EEPROM and Misc Drivers

Summary: This fragment disables support for miscellaneous EEPROM chip drivers and similar devices. These are not required unless interfacing with such chips over SPI or I2C.
Configuration breakdown:

    EEPROM and other embedded chip drivers

        CONFIG_EEPROM_93CX6
        CONFIG_EEPROM_AT25
        CONFIG_MISC_RTSX
        → → No detailed description available.