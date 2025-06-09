28 - Disable Hardware Cryptography, Keep DRBG and Jitter Entropy

Summary: This fragment disables hardware-accelerated cryptography but retains pseudo-random generation (DRBG) and entropy from CPU jitter, favoring software-only randomness sources.
Configuration breakdown:

    Software-only cryptography

        CONFIG_CRYPTO_DRBG
        CONFIG_CRYPTO_JITTERENTROPY
        CONFIG_CRYPTO_HW
        → → No detailed description available.