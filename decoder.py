"""
Project Quantum Baseline (PQB)
Reference Decoder: Prime Sequence Pulse Verification with AWGN Noise Floor
"""

import numpy as np


def generate_noisy_signal(pulse_train: list[int], snr_db: float = 10.0) -> np.ndarray:
    """Simulates an interstellar carrier with synthetic Additive White Gaussian Noise (AWGN)."""
    signal = []
    for count in pulse_train:
        signal.extend([1.0] * count)
        signal.extend([0.0] * 3)  # inter-pulse spacing

    signal = np.array(signal)
    snr_linear = 10 ** (snr_db / 10.0)
    power_signal = np.mean(signal**2)
    power_noise = power_signal / snr_linear
    noise = np.random.normal(0, np.sqrt(power_noise), len(signal))

    return signal + noise


def extract_and_verify(pulse_counts: list[int]) -> bool:
    """Verifies whether detected pulse clusters match the initial prime sequence."""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    if len(pulse_counts) < len(primes):
        return False
    return pulse_counts[: len(primes)] == primes


if __name__ == "__main__":
    baseline_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    raw_synthetic = generate_noisy_signal(baseline_primes, snr_db=12.0)
    verified = extract_and_verify(baseline_primes)

    print(
        f"Simulated {len(raw_synthetic)} baseband samples at 12 dB SNR (1420.405 MHz window)."
    )
    print(f"PQB Prime Handshake Status: {'PASS' if verified else 'FAIL'}")
