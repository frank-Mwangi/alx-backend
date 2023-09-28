import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient({
  host: 'localhost',
  port: 6379
});

// promisify the client.get method
const asyncGet = promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (err, res) => {
    if (err) {
      print(`Reply: ${err}`);
    } else {
      print(`Reply: ${res}`);
    }
  });
};

const displaySchoolValue = async (schoolName) => {
  try {
    const res = await asyncGet(schoolName);
    console.log(`${res}`);
  } catch (err) {
    console.error(`${err}`);
  }
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
