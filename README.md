# BDD-Based Test Automation Framework

## Overview
This is a Behavior-Driven Development (BDD) test automation framework built with Python, Behave, and Allure Reports. It enables scalable, secure, and industry-standard test automation, offering detailed logging, interactive reporting, and seamless integration with CI/CD pipelines.

## Features
- Behavior-Driven Development (BDD): Uses Gherkin syntax for writing tests in plain language.
- Interactive Reporting: Generates Allure reports with step-level insights and logs.
- Scalability: Modular design supports large-scale automation projects.
- Error Traceability: Logs and debugging utilities for easy issue tracking.

## Project Structure
```
BehaveX/
├── README.md
├── behave.ini
├── config
│   └── config.jason
├── features
│   ├── auth
│   │   └── login.feature
│   └── steps
│       └── auth_steps.py
├── pages
│   ├── auth
│   │   └── login_page.py
│   └── common
│       └── base_page.py
├── reports
│   ├── allure-results
│   │   ├── 0a839c0f-d14b-4d79-9fc5-e85ad2f3c26a-result.json
│   └── logs
│       └── framework_execution.log
├── requirements.txt
├── runner.py
└── utilities
    ├── browser_manager.py
    └── logger.py
```

## Prerequisites
1. Install Python 3.7+
2. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Install Allure CLI (Follow the [Allure CLI Installation Guide](https://docs.qameta.io/allure/))

## Running Tests
Run all tests and generate Allure results:
```bash
python runner.py
```

View the Allure report:
```bash
allure serve reports/allure-results
```

## Future Enhancements
- 🛠 CI/CD Integration: Automate test execution within DevOps pipelines.
- ⚡ Parallel Execution: Speed up tests using concurrent execution.
- 🔄 API Testing Support: Extend the framework to support API testing.

## References
- [Behave Documentation](https://behave.readthedocs.io/)
- [Allure Reporting Tool](https://docs.qameta.io/allure/)
- [Selenium WebDriver](https://www.selenium.dev/documentation/)

## License
---
Author : Vaibhav Panditkar 🚀
