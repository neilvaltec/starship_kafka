from confluent_kafka import Producer
import socket

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# Kafka producer configuration
conf = {
    'bootstrap.servers': 'localhost:9093',  # Replace with your broker
    'client.id': 'python-producer'
}

producer = Producer(conf)

# Create a socket to listen to port 14540
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Use SOCK_DGRAM for UDP
s.bind(('localhost', 14540))
print("Listening on port 14540...")

while True:
    data, address = s.recvfrom(1024)  # This call will block until a packet is received
    print(f"Received data from {address}")
    
    if data:
        producer.produce('starship_topic', value=data, callback=delivery_report)
        # Serve delivery callbacks from previous produce() calls
        producer.poll(0.1)

# Wait for any outstanding messages to be delivered and delivery reports to be received.
producer.flush()
