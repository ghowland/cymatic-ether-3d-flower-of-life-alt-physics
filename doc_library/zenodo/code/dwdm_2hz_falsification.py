import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from gwpy.timeseries import TimeSeries
import warnings

warnings.filterwarnings("ignore")

def cks_bulk_audit_100():
    """
    CKS Bulk Audit: One download, 100 slices.
    Bypasses server-side latency by processing data locally.
    """
    N_BIN = 32           
    df = 1.0 / N_BIN     
    
    # We download a single large block of confirmed "Science Mode" data
    # GPS 1241711616 is known to have a long continuous lock
    start_gps = 1241711616 
    # 100 segments of 32s each = 3200 seconds (approx 1 hour)
    # We take 4096s segments for high spectral resolution
    segment_len = 4096
    total_duration = segment_len * 10 
    
    print(f"--- CKS BULK DATA AUDIT ---")
    print(f"Lattice Bin: {df:.6f} Hz")
    print(f"Downloading 10-segment bulk block (approx 11 hours of physics)...")

    try:
        # One single request to the server
        data = TimeSeries.fetch_open_data('H1', start_gps, start_gps + 40960, cache=True)
        print("Download complete. Processing 100 topological slices...")
    except Exception as e:
        print(f"Bulk download failed: {e}. Trying secondary GPS...")
        # Fallback to a different O3 window if the first is down
        data = TimeSeries.fetch_open_data('H1', 1238166018, 1238166018 + 40960, cache=True)

    fs = int(data.sample_rate.value)
    full_array = np.nan_to_num(np.array(data.value))
    
    audit_results = []
    
    # We slice the bulk block into 100 overlapping segments to see the snap evolution
    # Overlap allows us to see how the 'heartbeat' shifts across the lattice
    step = (len(full_array) - (segment_len * fs)) // 100
    
    for i in range(100):
        start_idx = i * step
        end_idx = start_idx + (segment_len * fs)
        
        slice_raw = full_array[start_idx:end_idx]
        slice_raw -= np.mean(slice_raw)
        
        # Spectral Analysis
        f, pxx = welch(slice_raw, fs, nperseg=fs*N_BIN)
        
        mask = (f >= 2.0) & (f <= 3.5)
        peak_f = f[mask][np.argmax(pxx[mask])]
        
        k_val = peak_f / df
        k_int = int(round(k_val))
        error = abs(peak_f - (k_int * df))
        
        audit_results.append([i+1, peak_f, k_int, error])
        
        if (i+1) % 10 == 0:
            print(f"Slice [{i+1:03d}] | Peak: {peak_f:.6f} Hz | k: {k_int} | Err: {error:.12f}")

    # --- FINAL REPORT ---
    res = np.array(audit_results)
    mean_err = np.mean(res[:, 3])

    print("\n--- FINAL BULK SUMMARY ---")
    print(f"Mean Lattice Snap Error: {mean_err:.12e} Hz")

    plt.figure(figsize=(10, 5))
    plt.scatter(res[:, 0], res[:, 1], c=res[:, 1], cmap='viridis', edgecolors='k')
    for k in range(int(2.0/df), int(3.5/df) + 1):
        plt.axhline(k * df, color='gray', alpha=0.2)
    plt.title("CKS Bulk Audit: 100 Topological Slices")
    plt.xlabel("Slice Index")
    plt.ylabel("Frequency (Hz)")
    plt.colorbar(label="Frequency")
    plt.show()

if __name__ == "__main__":
    cks_bulk_audit_100()

    