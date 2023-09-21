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
## More details about why use kafka and background
- Check https://github.com/neilvaltec/starship_kafka/issues/1
