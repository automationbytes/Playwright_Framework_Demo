// const convertJson = require('jsonjunit');

// // const options = {
// //     inputJsonFile: 'reports/cucumber_report.json',
// //     outputXmlFile: 'reports/cucumber_report_new.xml',
// //     featureNameAsClassName: true // default: false
// // }

// convertJson({jsonPath: 'reports/cucumber_report.json',junitPath:'reports/cucumber_report_n.junit'});

const { CucumberConverter } = require('cucumber-to-junit');

const converter = new CucumberConverter({
  markUndefinedAsFailed: true // undefined scenario steps will fail the test case
});

converter.convertToJunit('reports/cucumber_report.json', 'reports/cucumber_junit.xml');
