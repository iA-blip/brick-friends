import argparse
import threading
import queue

from .__init__ import __version__

# Returns the cli arguments.
def get_args(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """Returns the cli arguments.

    Args:
        parser (argparse.ArgumentParser): The argparse parser object.

    Returns:
        argparse.Namespace: All the given arguments.
    """

    # Required arguments.
    parser.add_argument("session", type=str, help="The brick-hill session cookie.")
    parser.add_argument("token", type=str, help="brick-hill token to be able to add friends.")  # The brick-hill token to be able to send requests.

    # Optional arguments.
    parser.add_argument("-m", "--minrange", type=int, help="Minimum search range.", default=1)  # Minimum search range, default is 1.
    parser.add_argument("-M", "--maxrange", type=int, help="Maximum search range.", default=1000)  # Maximum search range, default is 1000.
    parser.add_argument("-t", "--threadamount", type=int, help="Amount of threads to use", default=100)  # How many threads the program will use, default is 100
    parser.add_argument("-a", "--autoproxy", action="store_true", help="Automatically find and use a proxy.")  # If the program should automate proxy.

    # Parse arguments.
    return parser.parse_args()

# Main entry point.
def main():
    # Creates a command-line parser
    parser = argparse.ArgumentParser()
    arguments = get_args(parser)
    session = None

    # Whether to use proxy based on user specified.
    if arguments.autoproxy:
        from pypac import PACSession

        # Create a proxy session.
        session = PACSession()
    else: 
        import requests

        # Creates a normal session.
        session = requests.Session()
    assert session is not None

    thread_lock = threading.Lock()

    # brick-hill friends api
    friends_api = "https://www.brick-hill.com/friends"

    token: str = arguments.token
    session_cookie = dict(brick_hill_session=arguments.session)

    # Adds brick-hill user with the user id.
    def add_friend(user_id: int) -> bool:
        """Adds brick-hill user with the user id.

        Args:
            user_id (int): brick-hill user id.
        """
        
        try:
            payload = {
                "_token":   token,
                "userId":   user_id,
                "sender":   "profile",
                "type":     "send",
            }

            # Prevent threading to access same variables at the same time.
            with thread_lock:

                # Makes a post request.
                res = session.post(friends_api, data=payload, cookies=session_cookie)

                # Add back to queue if ratelimited.
                if res.status_code == 429:
                    print(f"Rate limited while adding {user_id}")
                    q.put(user_id)
                else:
                    print(f"Added {user_id}")
                    # print(res.status_code)
        except KeyboardInterrupt:
            # This exception doesn't really work.
            exit()
        except:
            pass

    # Daemon thread loop.
    def threader():
        """Daemon thread loop."""

        while True:
            worker = q.get()
            add_friend(worker)
            q.task_done()

    # Queue object to store user ids.
    q = queue.Queue()

    # Spawning x amount daemon threads.
    for _ in range(arguments.threadamount):
        thread = threading.Thread(target=threader, daemon=True)
        thread.start()

    # Generating user id queue.
    for user_id in range(arguments.minrange, arguments.maxrange):
        q.put(user_id)

    q.join()

if __name__ == "__main__":
    main()