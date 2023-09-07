from confluent_kafka import Producer
import datetime    

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def produce_message(producer, num_partitions):
    """produce message"""
    for i in range(num_partitions):  # Loop for the number of partitions
        producer.poll(0.1)
        the_dt = str(datetime.datetime.utcnow())
        val = f"Count: {i} at {the_dt}".encode(encoding='utf8')
        key = str(i).encode(encoding='utf8')  # Use the loop index as the key
        producer.produce('starship_topic', value=val, key=key, callback=delivery_report)

    # Wait for any outstanding messages to be delivered and delivery reports
    # callbacks to be triggered.
    producer.flush()

if __name__ == "__main__":
    p = Producer({'bootstrap.servers': 'localhost:9093'})
    NUMBER_OF_CONNECTION_MAX_SUPPORT = 8
    produce_message(p, NUMBER_OF_CONNECTION_MAX_SUPPORT)  # Assuming you have 8 partitions
