#!/usr/bin/env node

const request = require('request');
const baseUrl = 'https://swapi.dev/api/films/';

// Function to get the characters of a movie
function getMovieCharacters(movieId) {
  // Fetch the movie details from the Star Wars API
  request(`${baseUrl}${movieId}/`, (error, response, body) => {
    if (!error && response.statusCode == 200) {
      const movieData = JSON.parse(body);
      const characters = movieData.characters;

      // Function to fetch character names sequentially
      function fetchCharacterName(url, callback) {
        request(url, (error, response, body) => {
          if (!error && response.statusCode == 200) {
            const characterData = JSON.parse(body);
            callback(characterData.name);
          }
        });
      }

      // Loop through each character URL and fetch the name
      characters.forEach((characterUrl) => {
        fetchCharacterName(characterUrl, (name) => {
          console.log(name);
        });
      });
    } else {
      console.log(`Failed to fetch movie details for ID ${movieId}`);
    }
  });
}
