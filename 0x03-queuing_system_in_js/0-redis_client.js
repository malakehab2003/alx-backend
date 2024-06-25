import redis from 'redis';

const connect = redis.createClient();

connect.on('conncet', () => {
  console.log('Redis client connected to the server');
});

connect.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
