// playwright.config.js
// @ts-check
/** @type {import('@playwright/test').PlaywrightTestConfig} */
const config = {
    timeout: 60000, // Timeout is shared between all tests.
    reporter: [
      ['list'],
      ['json', {  outputFile: 'test-results.json' }]
    ],
  
    projects: [
      {
        name: 'Smoke',
        testMatch: /.*feature/,
        retries: 0,
      },
      {
        name: 'Default',
        testIgnore: /.*smoke.spec.ts/,
        retries: 2,
      },
    ],
    globalSetup:"util/globalSetup.js"

  };
  module.exports = config;