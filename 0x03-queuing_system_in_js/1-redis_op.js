import redis from 'redis';

const connect = redis.createClient();

connect.on('connect', () => {
  console.log('Redis client connected to the server');
});

connect.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool(schoolName, value) {
  connect.set(schoolName, value, (err, reply) => {
    if (err) {
      console.log(err)
    } else {
      console.log(`Reply: ${reply}`)
    }
  });
}

function displaySchoolValue(schoolName) {
  connect.get(schoolName, (err, reply) => {
    if (err) {
      console.log(err)
    } else {
      console.log(reply)
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
