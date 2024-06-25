import { createClient } from 'redis';

const connect = createClient();

connect.on('connect', () => {
  console.log('Redis client connected to the server')
});

connect.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`)
});

connect.subscribe('holberton school channel', (err, reply) => {
  if (err) {
    console.log(err)
  } else {
    console.log('Subscribed to channel:', reply);
  }
});

connect.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    connect.unsubscribe();
    connect.quit();
  }
});
