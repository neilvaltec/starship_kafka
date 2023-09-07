import argparse
from confluent_kafka import Consumer, TopicPartition
from pymavlink import mavutil

def decode_mavlink_message(message_data):
    """decode the message"""
    mav = mavutil.mavlink_connection('udpin:localhost:14000', 
                                     dialect="ardupilotmega", 
                                     notimestamps=True)
    # Parse the entire message buffer
    mavlink_msgs = mav.mav.parse_buffer(message_data)
    
    # Print the parsed MAVLink messages
    for mavlink_msg in mavlink_msgs:
        print("Decode mavlink message")
        print(mavlink_msg)

def main(args):
    """main"""
    conf = {
        'bootstrap.servers': args.bootstrap_servers,
        'group.id': 'check_data',
        'auto.offset.reset': 'earliest'
    }

    consumer = Consumer(conf)

    # Assign consumer to specific topic, partition, and offset
    tp = TopicPartition(args.topic, args.partition, args.offset)
    consumer.assign([tp])

    msg = consumer.poll(1.0)
    if msg is not None:
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
        else:
            print("Received raw message: {}".format(msg.value()))
    else:
        print("No message retrieved from the specified input arguments.")
        return
    
    # Decode the MAVLink message
    decode_mavlink_message(msg.value())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Consume a Kafka message and decode MAVLink content.',
                                     epilog="Example usage: python check_data.py --bootstrap_servers localhost:9093 --topic starship_topic --partition 0 --offset 0")

    parser.add_argument('--bootstrap_servers', default='localhost:9093', help='Bootstrap servers for Kafka. Default: localhost:9093')
    parser.add_argument('--topic', default='starship_topic', help='Kafka topic to consume from. Default: starship_topic')
    parser.add_argument('--partition', type=int, default=0, help='Partition number to consume from. Default: 0')
    parser.add_argument('--offset', type=int, default=0, help='Offset number to start consuming from. Default: 0')

    args = parser.parse_args()
    print("Arguments:", vars(args))
    
    main(args)
