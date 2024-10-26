import threading

# create thread 
def create_thread(target, args):
    thread = threading.Thread(target=target, args=args)
    thread.start()
    return thread

if __name__ == "__main__":
    create_thread(lambda: print("Hello, thread is working"), ())