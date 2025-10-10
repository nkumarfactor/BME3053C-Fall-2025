import math
import random

# Generate the PPG signal (simulated data)
ppg_signal = [1000 + 100 * math.sin(0.1 * x) + random.randint(-20, 20) for x in range(100)]

def count_peaks(ppg_signal):
    """
    Counts the number of peaks in a PPG signal.
    A peak is defined as a value greater than its immediate neighbors.
    """
    peak_count = 0
    
    # Loop through the signal using indices (ignore the first and last points)
    for i in range(1, len(ppg_signal) - 1):
        if (ppg_signal[i] > ppg_signal[i - 1]) and (ppg_signal[i] > ppg_signal[i + 1]):
            peak_count += 1
    
    print(f"Total number of peaks detected: {peak_count}")

# Call the function
count_peaks(ppg_signal)
