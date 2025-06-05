23 - Disable I2C, Power and Sensor Drivers

Summary: This fragment disables common I2C bus support and drivers for power regulators and sensors. These are unnecessary if the system has no such peripherals.
Configuration breakdown:

    I2C and sensors

        CONFIG_I2C
        CONFIG_REGULATOR
        CONFIG_SENSORS_CORETEMP
        CONFIG_HWMON
        → → No detailed description available.

