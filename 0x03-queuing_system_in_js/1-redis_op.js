import { createClient, redis} from 'redis';


const client = createClient();

client.on('connect', function() {
    console.log('Redis client connected to the server');
});
client.on('error', function(error) {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

function setNewSchool(schoolName, value) {  
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, reply) => {
	  console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
