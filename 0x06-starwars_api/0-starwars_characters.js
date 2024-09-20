#!/usr/bin/node
const axios = require('axios');
if (process.argv.length < 3) {
  console.log('Please provide a movie ID as a positional argument');
  process.exit(1);
}
const movieId = process.argv[2];
const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;
// Function to fetch and display character names
async function fetchCharacters() {
  try {
    // Get movie details
    const filmResponse = await axios.get(filmUrl);
    const characters = filmResponse.data.characters;
    // Fetch each character's details in order
    for (const characterUrl of characters) {
      const characterResponse = await axios.get(characterUrl);
      console.log(characterResponse.data.name);
    }
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}
// Call the function
fetchCharacters();
