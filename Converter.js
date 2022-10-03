const cucumberJunitConvert = require('cucumber-junit-convert');

const options = {
    inputJsonFile: 'reports/cucumber_report.json',
    outputXmlFile: 'reports/cucumber_report.xml',
    featureNameAsClassName: true // default: false
}

cucumberJunitConvert.convert(options);

