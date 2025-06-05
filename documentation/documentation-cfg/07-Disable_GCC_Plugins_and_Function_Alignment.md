07 - Disable GCC Plugins and Function Alignment

Summary: This fragment disables the use of GCC compiler plugins and specific function alignment settings. These options can slightly reduce binary size and complexity when such features are not needed.
Configuration breakdown:

    GCC plugin support

        CONFIG_GCC_PLUGINS
        → Disables all GCC plugin support, reducing build complexity.

    Function alignment

        CONFIG_FUNCTION_ALIGNMENT_32B
        CONFIG_FUNCTION_ALIGNMENT
        → Specifies function alignment to optimize cache performance.

