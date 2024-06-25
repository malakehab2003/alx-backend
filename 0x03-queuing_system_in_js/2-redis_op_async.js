import redis from 'redis';
import { promisify } from 'util';

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

const getAsync = promisify(connect.get).bind(connect);


async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (err) {
    console.error(err);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
