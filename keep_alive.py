import requests
import time
import threading


class KeepAlive:

    def __init__(self, url="http://0.0.0.0:8080", interval=300):
        """
        Initialize keep-alive service
        :param url: URL to ping to keep alive
        :param interval: Time in seconds between pings (default: 5 minutes)
        """
        self.url = url
        self.interval = interval
        self.running = False
        self.thread = None

    def ping(self):
        """Send a ping request to keep the service alive"""
        try:
            response = requests.get(self.url, timeout=10)
            if response.status_code == 200:
                print(
                    f"✓ Keep-alive ping successful at {time.strftime('%Y-%m-%d %H:%M:%S')}"
                )
            else:
                print(
                    f"⚠ Keep-alive ping returned status {response.status_code}"
                )
        except requests.exceptions.RequestException as e:
            print(f"✗ Keep-alive ping failed: {e}")

    def _keep_alive_loop(self):
        """Main loop for keep-alive pings"""
        while self.running:
            time.sleep(self.interval)
            if self.running:  # Check again in case stop was called during sleep
                self.ping()

    def start(self):
        """Start the keep-alive service"""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._keep_alive_loop,
                                           daemon=True)
            self.thread.start()
            print(
                f"Keep-alive service started - pinging {self.url} every {self.interval} seconds"
            )

    def stop(self):
        """Stop the keep-alive service"""
        self.running = False
        if self.thread:
            self.thread.join()
        print("Keep-alive service stopped")


# Global keep-alive instance
keep_alive = KeepAlive()


def start_keep_alive():
    """Start the keep-alive service"""
    keep_alive.start()


def stop_keep_alive():
    """Stop the keep-alive service"""
    keep_alive.stop()


if __name__ == "__main__":
    # Run as standalone script
    print("Starting keep-alive service...")
    keep_alive.start()

    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down keep-alive service...")
        keep_alive.stop()
