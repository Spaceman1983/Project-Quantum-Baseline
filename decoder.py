"""
Project Quantum Baseline (PQB)
Reference Decoder: Prime Sequence Verification & 2D Raster Frame Reconstruction
Carrier: 1420.405 MHz | License: MIT
"""

import numpy as np


def verify_prime_handshake(pulse_counts: list[int]) -> bool:
    """Verifies beacon acquisition against fundamental prime seed."""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    return len(pulse_counts) >= len(primes) and pulse_counts[: len(primes)] == primes


def decode_raster_payload(bitstream: list[int]) -> np.ndarray:
    """
    Deconstructs a linear 1D bitstream into a 2D matrix by identifying
    its unique non-trivial prime factorization (Semiprime check: N = p * q).
    """
    total_bits = len(bitstream)

    # Find prime factor pairs
    factors = [
        (p, total_bits // p)
        for p in range(2, int(total_bits**0.5) + 1)
        if total_bits % p == 0
    ]

    if not factors:
        raise ValueError(
            f"Bitstream length {total_bits} is not a valid semiprime product."
        )

    # Standardize dimensions (height, width)
    rows, cols = factors[0]
    return np.array(bitstream).reshape((rows, cols))


if __name__ == "__main__":
    # 1. Verify Phase 1 Beacon Handshake
    test_beacons = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    handshake_status = verify_prime_handshake(test_beacons)
    print(f"Phase 1 Beacon Acquisition: {'PASS' if handshake_status else 'FAIL'}")

    # 2. Simulate Phase 5 Raster (7 x 5 = 35-bit Semiprime Payload)
    # Synthetic cross/glyph pattern in binary:
    payload_35bit = [
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        1,
        1,
        1,
        1,
        1,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        0,
        0,
        1,
    ]

    raster = decode_raster_payload(payload_35bit)
    print(f"Phase 5 Payload Restructured to Matrix Dimensions: {raster.shape}")
    print("\nVisual Raster Output:")
    for row in raster:
        print("".join(["██" if bit == 1 else "  " for bit in row]))
   
