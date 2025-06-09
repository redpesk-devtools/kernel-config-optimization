# 23 - Disable I2C, Power and Sensor Drivers

## Summary

This fragment disables common I2C bus support and drivers for power regulators and sensors. These are unnecessary if the system has no such peripherals.

## Configuration breakdown

### I2C and sensors

```none
CONFIG_I2C
CONFIG_REGULATOR
CONFIG_SENSORS_CORETEMP
CONFIG_HWMON
```

* Disables I2C subsystem.

* Disables power regulator framework.

* Disables Intel Core temperature sensors.

* Disables hardware monitoring support.

## Where to find a cfg sample

[23-Config-Disable-I2C-Power-and-Sensor-Drivers.cfg](../../beagle-board/6.6.32/packaging/23-Config-Disable-I2C-Power-and-Sensor-Drivers.cfg)
