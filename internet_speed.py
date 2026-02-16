import speedtest

def check_speed():
    st = speedtest.Speedtest()

    print("Finding best server...")
    st.get_best_server()

    print("Testing download speed...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps

    print("Testing upload speed...")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps

    ping = st.results.ping

    print("\n--- Internet Speed Results ---")
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")

check_speed()
