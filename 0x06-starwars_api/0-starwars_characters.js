#!/usr/bin/node

const request = require('request-promise-native');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movieId>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

(async () => {
  try {
    const movieData = await request(apiUrl);
    const characters = JSON.parse(movieData).characters;

    for (const url of characters) {
      const characterData = await request(url);
      console.log(JSON.parse(characterData).name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
})();
