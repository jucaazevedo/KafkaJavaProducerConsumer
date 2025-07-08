from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
mensagem = "Viva o Fluminense"
producer.send('tricolor', mensagem.encode('utf-8'))
producer.flush()
print("Mensagem enviada.")

