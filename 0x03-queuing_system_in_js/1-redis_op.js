import { createClient, print } from "redis";

const client = createClient({
  host: "localhost",
  port: 6379,
});

client.on_connect("connect", () => {
  console.log("Redis client connected to the server");
});
client.on("error", (error) => {
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

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, res) => {
    if (err) {
      console.error(`${err}`);
    } else {
      console.log(`${res}`);
    }
  });
};

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
