# 27 - Enable Minimal Cryptographic Core with SHA3 and XTS

## Summary

This fragment enables only the essential cryptographic modules including SHA3 and XTS modes. Useful for secure applications with minimal algorithm footprint.

## Configuration breakdown

### Cryptographic core features

```none
CONFIG_CRYPTO_SHA3
CONFIG_CRYPTO_XTS
```

* Enables SHA3 hash algorithm.

* Enables XTS block cipher mode.

## Where to find a cfg sample

[27-Config-Crypto-Core-SHA3-XTS.cfg](../../beagle-board/6.6.32/packaging/27-Config-Crypto-Core-SHA3-XTS.cfg)
