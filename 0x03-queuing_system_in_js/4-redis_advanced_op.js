import redis from 'redis';

const connect = redis.createClient();

connect.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

connect.on('connect', () => {
  console.log('Redis client connected to the server');
});

function createHash () {
  const hashes = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };
  for (const [key, value] of Object.entries(hashes)) {
    connect.hset('HolbertonSchools', key, value, redis.print);
  }

  connect.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.log(err);
    } else {
      console.log(reply);
    }
  });
}
createHash();
