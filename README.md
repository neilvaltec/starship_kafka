# starship_kafka   
 [gazebo-haedless]  --->  [kafka producer]  --->  [kafka topic]  --->  [kafka consumer]

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
