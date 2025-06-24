# 28 - Disable Hardware Cryptography, Keep DRBG and Jitter Entropy

## Summary

This fragment disables hardware-accelerated cryptography but retains pseudo-random generation (DRBG) and entropy from CPU jitter, favoring software-only randomness sources.

## Configuration breakdown

### Software-only cryptography

```none
CONFIG_CRYPTO_DRBG
CONFIG_CRYPTO_JITTERENTROPY
CONFIG_CRYPTO_HW
```

* Keeps deterministic random bit generator.

* Keeps entropy generation from CPU jitter.

* Disables hardware crypto support.

## Where to find a cfg sample

[28-Config-Crypto-DRBG-Jitter-No-HW.cfg](https://raw.githubusercontent.com/redpesk-devtools/kernel-config-optimization/refs/heads/master/beagle-board/6.6.32/packaging/28-Config-Crypto-DRBG-Jitter-No-HW.cfg)
