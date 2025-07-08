from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'tricolor',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='meu-grupo'
)

print("Aguardando mensagens...")
for msg in consumer:
    print("Recebido:", msg.value.decode('utf-8'))
    break  # Sai depois de receber a primeira

