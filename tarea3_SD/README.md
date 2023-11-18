
```sh
find / -name "docker-entrypoint.sh" 2>/dev/null
```

```sh
chmod +x "path encontrado"
```
```sh
python python3 wiki.py
```

```sh
docker compose up -d --build
```
```sh
docker compose down -v
```
```sh
docker system prune -a
```
```sh
hdfs dfs -mkdir /user
```
```sh
hdfs dfs -mkdir /user/hduser
```
```sh
hdfs dfs -mkdir input
```
```sh
sudo chown -R hduser .
```
```sh
cd examples/
```
```sh
hdfs dfs -put carpeta1/*.txt input
```

```sh
hdfs dfs -put carpeta2/*.txt input
```

```sh
hdfs dfs -ls input
```
```sh
mapred streaming -files mapper.py,reducer.py -input /user/hduser/input/*.txt -output hduser/outhadoop/ -mapper ./mapper.py -reducer ./reducer.py
```
```sh
hdfs dfs -get /user/hduser/hduser/outhadoop/ /home/hduser/examples
```
```sh
python 
```


