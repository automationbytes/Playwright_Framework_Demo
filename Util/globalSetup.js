const FullConfig = require ("@playwright/test");
const dotenv = require("dotenv")

async function globalSetup(FullConfig) {

    if (process.env.test_env) {
        dotenv.config(
            { path: `.env.${process.env.test_env}` },
            {override:true}
            )
      

        console.log(path)
        
    }



}

module.exports = { globalSetup };

