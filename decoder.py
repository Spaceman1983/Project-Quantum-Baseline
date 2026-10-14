"""
Project Quantum Baseline (PQB)
Reference Decoder: Prime Sequence Pulse Verification
"""

def verify_prime_pulse_train(pulse_counts: list[int]) -> bool:
    """Verifies whether detected pulse clusters match the initial prime sequence."""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    if len(pulse_counts) < len(primes):
        return False
    return pulse_counts[: len(primes)] == primes


if __name__ == "__main__":
    synthetic_signal = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    verified = verify_prime_pulse_train(synthetic_signal)
    print(f"PQB Prime Handshake Verified: {verified}")
