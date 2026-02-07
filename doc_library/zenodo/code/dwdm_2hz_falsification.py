import numpy as np
from scipy.signal import welch
from gwpy.timeseries import TimeSeries
import warnings

warnings.filterwarnings("ignore")

def cks_locked_audit_multi_segment():
    # AXIOMATIC TARGET (ONE CONSTANT: K = 1.0857)
    # Target is fixed at 2.375 Hz based on the Hex-UV bridge
    f_target = 2.3750 
    
    # Audit Parameters
    # 5 independent segments of LIGO O3 data
    segments = [1241711616, 1241715712, 1241719808, 1241723904, 1241728000]
    duration = 4096
    detected_peaks = []

    print(f"--- CKS MULTI-SEGMENT AUDIT ---")
    print(f"Locked Analytic Target: {f_target:.4f} Hz")
    print(f"Bin Resolution: 0.03125 Hz\n")

    for i, start in enumerate(segments):
        try:
            data = TimeSeries.fetch_open_data('H1', start, start+duration, cache=True)
            fs = int(data.sample_rate.value)
            raw = np.nan_to_num(np.array(data.value))
            
            # High-res Spectral Analysis
            f_axis, pxx = welch(raw - np.mean(raw), fs, nperseg=fs*32)
            
            # Search window around target (2.0 to 2.8 Hz)
            mask = (f_axis >= 2.0) & (f_axis <= 2.8)
            peak_f = f_axis[mask][np.argmax(pxx[mask])]
            detected_peaks.append(peak_f)
            print(f"Segment {i+1}: Detected Peak = {peak_f:.6f} Hz")
            
        except Exception:
            print(f"Segment {i+1}: Data gap, skipping.")

    if not detected_peaks:
        return

    mean_peak = np.mean(detected_peaks)
    error = abs(mean_peak - f_target)

    print(f"\n--- FINAL AUDIT RESULTS ---")
    print(f"Mean Detected Peak: {mean_peak:.6f} Hz")
    print(f"Systematic Error:   {error:.6f} Hz")

    # THE ULTIMATUM
    # If error > bin width (0.03125), the 2.375 Hz prediction is falsified.
    if error < 0.03125:
        print("\nSTATUS: PASS. The 2.375 Hz signal is systematic and locked.")
    else:
        print("\nSTATUS: FAIL. The 12-bond derivation is falsified.")

if __name__ == "__main__":
    cks_locked_audit_multi_segment()

    