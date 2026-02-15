import speedtest

def run_speed_test():
    try:
        print("Finding the best server...")
        st = speedtest.Speedtest()
        
        st.get_best_server()
        
        print(" Testing Download Speed...")
        download_speed = st.download()
        
        print(" Testing Upload Speed...")
        upload_speed = st.upload()
        
        download_mbps = download_speed / 10**6
        upload_mbps = upload_speed / 10**6
        ping = st.results.ping

        print("\n" + "="*30)
        print("   INTERNET SPEED RESULTS")
        print("="*30)
        print(f"Download Speed: {download_mbps:.2f} Mbps")
        print(f"Upload Speed:   {upload_mbps:.2f} Mbps")
        print(f"Ping (Latency): {ping:.2f} ms")
        print("="*30)

    except Exception as e:
        print(f" An error occurred: {e}")
        print("Tip: Make sure you are connected to the internet.")

if __name__ == "__main__":
    run_speed_test()