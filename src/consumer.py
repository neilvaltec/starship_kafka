"""concumer script"""
import threading
from confluent_kafka import Consumer

def consume_messages(index: int):
    """consume messages"""
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9093',
        'group.id': 'unique_group_' + str(index),  # Each consumer should have a unique group ID
        # 'auto.offset.reset': 'earliest'
    })

    consumer.subscribe(['KafkaExplored'])

    while True:
        msg = consumer.poll(0.1)
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
        else:
            print(f"Received message: {msg.value().decode('utf-8')}")

def thread_function(concumer_index: int):
    """thread function"""
    consume_messages(concumer_index)

def main(max_connection_support: int):
    """main"""
    threads = []
    for i in range(max_connection_support):
        thread = threading.Thread(target=thread_function, args=[i])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All threads completed")

if __name__ == "__main__":
    NUMBER_OF_CONNECTION_MAX_SUPPORT = 8
    main(NUMBER_OF_CONNECTION_MAX_SUPPORT)
