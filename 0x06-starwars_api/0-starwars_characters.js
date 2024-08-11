#!/usr/bin/node

const request = require('request');

// Retrieve the Movie ID from the command-line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Construct the API URL for the given Movie ID
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make an HTTP GET request to the API to retrieve the movie data
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to retrieve movie data. Status code: ${response.statusCode}`);
    return;
  }

  // Parse the JSON data from the response body
  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  // Iterate over the characters array and make a request for each character
  characters.forEach((characterUrl) => {
    request(characterUrl, (err, res, body) => {
      if (err) {
        console.error('Error:', err);
        return;
      }

      if (res.statusCode !== 200) {
        console.error(`Failed to retrieve character data. Status code: ${res.statusCode}`);
        return;
      }

      // Parse and log the character's name
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
