27 - Enable Minimal Cryptographic Core with SHA3 and XTS

Summary: This fragment enables only the essential cryptographic modules including SHA3 and XTS modes. Useful for secure applications with minimal algorithm footprint.
Configuration breakdown:

    Cryptographic core features

        CONFIG_CRYPTO_SHA3
        CONFIG_CRYPTO_XTS
        → → No detailed description available.

