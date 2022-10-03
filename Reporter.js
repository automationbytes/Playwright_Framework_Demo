const fs = require('fs-extra');

const report = require('cucumberjs-playwright-reporter');
const reportPath = './reports/html'
fs.removeSync(reportPath); 

  

report.generate({
	jsonDir: './reports',
	reportPath: reportPath,
    openReportInBrowser: true,
staticFilePath: true,
saveCollectedJSON: true,
disableLog: false,
pageTitle: "Playwright Cucumber Reporter",
reportName: "<h3><I>  Playwright Reporter </I></h3>",
displayDuration: true,
durationInMS: true,
hideMetadata: false,
displayReportTime: true,
	metadata:{
        browser: {
            name: 'chrome',
            version: '105'
        },
        device: 'Local test machine',
        platform: {
            name: 'Windows',
            version: '10'
        }
    },
    customData: {
        title: 'Run info',
        data: [
            {label: 'Project', value: 'Cucumber project'},
            {label: 'Release', value: '1'},
            {label: 'Execution Start Time', value: 'Sep 29th 2022, 02:31 PM EST'},
            {label: 'Execution End Time', value: 'Sep 29th 2022, 02:36 PM EST'}
        ]
    }
});