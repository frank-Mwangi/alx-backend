import { createClient } from 'redis';

const client = createClient({
  host: 'localhost',
  port: 6379
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

const ourChannel = 'holberton school channel';
client.subscribe(ourChannel);

client.on('message', (channel, message) => {
  if (channel === ourChannel) {
    console.log(message);
    if (message === 'KILL_SERVER') {
      client.unsubscribe();
      client.quit();
    }
  }
});
