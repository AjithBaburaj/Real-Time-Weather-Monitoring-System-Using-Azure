from azure.eventhub import EventHubProducerClient, EventData
import json

# Event Hub configuration
EVENT_HUB_CONNECTION_STRING = "XXXX"
EVENT_HUB_NAME = "XXXX"

# Initialize the Event Hub producer
producer = EventHubProducerClient.from_connection_string(conn_str=EVENT_HUB_CONNECTION_STRING, eventhub_name=EVENT_HUB_NAME)

# Function to send events to Event Hub
def send_event(event):
    event_data_batch = producer.create_batch()
    event_data_batch.add(EventData(json.dumps(event)))
    producer.send_batch(event_data_batch)

# Sample JSON event
event = {
    "event_id": 1111,
    "event_name": "Test Event"
}

# Send the event
send_event(event)

# Close the producer
producer.close()

'''code explaination : creating an producer using event hub configurations(that’s, event hub connection string and event hub name. this producer is the main component to send the event to the event hub.
after that we have a fuction called send event. it has a 3 step process-[using the producer we r creating a event batch,adding incoming event to the created event batch, using producer to send the batch]
sample json event is sented and after that producer is closed'''