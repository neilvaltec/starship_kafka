# starship_kafka   
 [gazebo-haedless]  --->  [kafka producer]  --->  [kafka topic]  --->  [kafka consumer]

 - You can access the UI at http://localhost:18080/
 - e.g. Browse data 
 ![image](https://github.com/neilvaltec/starship_kafka/assets/133841195/c95fdc0b-b981-4088-8e82-de69a2f2b478)


## Run with drones
```sh
docker run --rm -it jonasvautherin/px4-gazebo-headless:1.13.2 # start drone simulator
docker-compose up
python src/producer_telemetry.py # produce demo data
python src/consumer_check_data.py # use this script to check data
```

## Run with auto generated data
```sh
docker-compose up
python src/producer_demo.py # produce demo data
python src/consumer_realtime.py # display data in real time
```


## Description of the repo
1. Give https://kafka.apache.org/quickstart a try so you can understand the basic concept of kafka.
2. kafka is not a monolithic app, it's composed by several binary programs and bash scripts. But luckily, we have many UI frameworks that encapsulates everything. For simplicity, here we choose https://github.com/provectus/kafka-ui.
3. Use docker environment makes everything easier.
4. Check `docker-compose.yml` and you'll see three image: zookeeper, kafka, kafka-ui. Pretty simple.
5. Follow `readme` to experience the event flow of kafka.

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
# More details about why use kafka and background

- ## Background
  - The traffic of ingesting multiple drones' mavlink message has a potential stuck issue in the previous version in starship "collector" and "processor". 
- ## Goal
  - We need a more reliable, industrial and matured solution to overcome the mavlink traffic issue and being able to scale whatever number of drones connection in the future without limitation.

- ## Resource
  - Kafka looks like a good try, recommended by ChatGPT as it indicates that kafka is flexible at scaling up, highly adopted by  industrial and has a well support community. It also meets our future requirement that supports 100 connections or more.
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
The reason why kafka instead of other message queue solutions, e.g., rabbitMQ.

## ChatGPT + my organization:

The choice between Apache Kafka and RabbitMQ depends on your specific use case, requirements, and priorities. Both are popular messaging systems, but they have different characteristics and strengths that make them suitable for different scenarios. Here are some reasons why you might choose Kafka over RabbitMQ:

- Scalability and Throughput:
  Kafka is designed for high-throughput and can handle a massive number of messages per second. It is well-suited for scenarios where you need to process a large volume of data in real-time, such as log aggregation, event sourcing, and streaming data pipelines.

- Distributed and Fault-Tolerant:
  Kafka is a distributed streaming platform that offers high fault tolerance and data durability. It replicates data across multiple brokers, ensuring that messages are not lost even in the event of hardware failures.

- Log-Centric Architecture:
  Kafka is built around a log-centric architecture, where data is stored as immutable logs. This makes it suitable for use cases where you need a reliable and durable record of events, such as event sourcing and auditing.

- Message Retention:
  Kafka allows you to retain messages for a specified period, making it useful for scenarios where historical data analysis or replay of events is required.

- Publish-Subscribe and Message Queues:
  While RabbitMQ primarily focuses on message queuing and publish-subscribe patterns, Kafka can handle both scenarios. It offers topic-based publish-subscribe and queue-like message distribution with consumer groups.

- Ecosystem and Integrations:
  Kafka has a rich ecosystem of tools and libraries for data processing and stream analytics, including Kafka Streams, Kafka Connect, and the Confluent Platform. This ecosystem can simplify building complex data pipelines.

- Community and Adoption:
  Kafka has gained widespread adoption in industries like finance, e-commerce, and social media, which can be an advantage when seeking community support and finding talent with Kafka expertise.

---
However, it's important to note that RabbitMQ also has its own strengths:

- Flexibility:
  RabbitMQ is highly configurable and supports a wide range of messaging patterns, making it a good choice for applications with diverse messaging requirements.

- Ease of Use:
  RabbitMQ is relatively easier to set up and configure compared to Kafka, which may make it a better choice for simpler use cases or when you need to get up and running quickly.

- Message Routing and Fanout:
  RabbitMQ offers more advanced routing options and fanout exchanges, which can be beneficial in scenarios where message routing is complex.


---
In summary, the choice between Kafka and RabbitMQ depends on your specific use case and requirements. If you need high-throughput, fault-tolerance, and a log-centric architecture for real-time data processing, Kafka may be a better fit. However, if you prioritize flexibility and ease of use for simpler messaging scenarios, RabbitMQ could be a more suitable choice. It's also worth considering other factors like your team's familiarity with the technology and your existing tech stack when making the decision.
