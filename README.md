This repository is a pet-project showcasing my work on an automated testing framework for the end-to-end (E2E) and functional UI verification of the [SauceDemo](https://www.saucedemo.com/) website (created by SauceLabs)

## 🛠 Technologies & Tools

* **Programming Language:** Python 3.12+
* **Automation Tool:** Selenium WebDriver
* **Testing Framework:** Pytest
* **Reporting:** Allure Report
* **Network Mocking:** Selenium-Wire + CDP (Chrome DevTools Protocol)
* **CI/CD:** GitHub Actions
* **Hosting:** GitHub Pages

---

## Architectural Highlights

The project strictly adheres to industry standards to ensure scalability, stability, and maintainability:

### 1. Page Object Model (POM)
All site pages are defined as distinct classes inheriting from a `BasePage` class. The `BasePage` encapsulates all raw Selenium WebDriver interactions, utilizing explicit waits (`WebDriverWait`).

### 2. Data-Driven Testing (DDT)
Test data (such as valid/invalid credentials and product lists) is completely separated from the test logic and stored in `.json` files within the `test_data/` directory.

### 3. Reusable UI Components
Cross-cutting elements, such as the site footer, are implemented as isolated components (`footer_element.py`).

### 4. Advanced Test Scenarios & Network Mocking
* **Dynamic E2E Checkout:** The framework includes complex E2E tests that randomly select products, process the checkout, and dynamically calculate expected costs and taxes to verify mathematical correctness on the UI side.
* **Network Interception:** A test uses `selenium-wire` to intercept network requests for product images, simulating a backend failure (returning a `404 Not Found` status). It then uses JavaScript to verify that the UI handles the missing assets.

---

## CI/CD Pipeline & Reporting

A fully automated CI/CD pipeline is configured using **GitHub Actions**.

1. **Automated Execution:** After every push to the `main` branch triggers the pipeline, which spins up an isolated Ubuntu environment, installs dependencies, and runs the Pytest suite in headless mode.
2. **Continuous Reporting:** After test execution, an **Allure Report** is automatically generated.
3. **Deployment:** The final report is deployed to GitHub Pages.

 **View the latest test results here:** [SauceDemo Auto UI Tests - Allure Report](https://oladusheeek.github.io/saucedemo_auto_ui_tests/)

---

## Local Setup & Execution

To run the framework on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/oladusheeek/saucedemo_auto_ui_tests.git
   cd saucedemo_auto_ui_tests
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the test suite:**
   ```bash
   pytest
   ```

5. **Generate and view the local Allure report:**
   ```bash
   allure serve allure-results
   ```