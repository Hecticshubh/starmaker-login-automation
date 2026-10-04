# 🚀 StarMaker Login Automation

A web automation project built with **Python, Selenium WebDriver and Pytest** to test the StarMaker login page.

***

## 📌 Project Overview

This project automates login-page test scenarios, including successful login, form validation, incorrect credentials and password masking.

The project supports two environments:

- 📱 **Android:** Termux + Termux:X11 + Chromium
- 💻 **Desktop:** Windows, Linux and macOS

Each environment has its own WebDriver configuration.

***

## 📑 Table of Contents

- [📂 Project Structure](#-project-structure)
- [🧪 Test Coverage](#-test-coverage)
- [🛠️ Requirements](#️-requirements)
- [📱 Android + Termux Setup](#-android--termux-setup)
- [🖥️ Start Termux:X11](#️-start-termuxx11)
- [⚙️ WebDriver Configuration](#️-webdriver-configuration)
- [▶️ Running the Tests](#️-running-the-tests)
- [🔄 Test Execution Flow](#-test-execution-flow)
- [🔐 Test Credentials](#-test-credentials)
- [⚠️ Important Notes](#️-important-notes)
- [⭐ Project Highlights](#-project-highlights)

***

## 📂 Project Structure

```text
starmaker-login-automation/
│
├── test_login.py
├── conftest_termux.py
├── conftest_desktop.py
├── requirements.txt
├── README.md
└── .gitignore
```

|File|Description|
|---|---|
|`test_login.py`|Contains automated login test cases|
|`conftest_termux.py`|WebDriver configuration for Android Termux|
|`conftest_desktop.py`|WebDriver configuration for desktop operating systems|
|`requirements.txt`|Required Python packages|
|`README.md`|Project documentation|
|`.gitignore`|Excludes unnecessary files from version control|

***

## 🧪 Test Coverage

The project contains **10 login test cases**.

|Test ID|Test Scenario|
|---|---|
|TC-01|Login page opens|
|TC-02|Valid login|
|TC-03|Email field visibility and enabled state|
|TC-04|Password field visibility and enabled state|
|TC-05|Both fields blank|
|TC-06|Valid email with blank password|
|TC-07|Blank email with password filled|
|TC-08|Invalid email with invalid password|
|TC-09|Valid email with wrong password|
|TC-10|Password masking|

***

## 🛠️ Requirements

### Common Requirements

- Python 3.x
- Selenium WebDriver
- Pytest
- Compatible Chrome or Chromium browser
- Internet connection

### Python Dependencies

The `requirements.txt` file contains:

```text
pytest
selenium
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

***

## 📱 Android + Termux Setup

This project can run on Android using Termux, Termux:X11 and Chromium.

### Step 1: Update Termux

```bash
pkg update
pkg upgrade
```

### Step 2: Install Python

```bash
pkg install python
```

### Step 3: Install Python Packages

```bash
pip install pytest
pip install selenium
```

Alternatively:

```bash
pip install -r requirements.txt
```

### Step 4: Install Termux:X11 and Chromium

```bash
pkg install x11-repo
pkg install termux-x11-nightly
pkg install chromium
pkg install openbox
```

***

## 🖥️ Start Termux:X11

Run the following commands in order.

**1. Start Termux:X11**

```bash
termux-x11 :0 &
```

**2. Set the display**

```bash
export DISPLAY=:0
```

**3. Start Openbox**

```bash
openbox &
```

**4. Check Chromium**

```bash
chromium-browser &
```

Chromium should open in the Termux:X11 graphical environment.

***

## ⚙️ WebDriver Configuration

Pytest automatically discovers fixtures from a file named `conftest.py`.

This project maintains separate configurations for Android and desktop environments. Before running tests, rename the appropriate configuration file to `conftest.py`.

### 📱 Android + Termux

1. Locate `conftest_termux.py`.
2. Rename it to `conftest.py`.
3. Run the tests.

### 💻 Windows / Linux / macOS

1. Locate `conftest_desktop.py`.
2. Rename it to `conftest.py`.
3. Install the required Python dependencies.
4. Run the tests.

**Important:** Use the configuration that matches your current environment. Keep the original configuration files if you want to switch environments later.

***

## ▶️ Running the Tests

After preparing the correct `conftest.py`, open the terminal in the project directory.

Run the complete test suite:

```bash
pytest -v
```

Run only the login test file:

```bash
pytest -v test_login.py
```

Pytest displays the result of each test in the terminal.

***

## 🔄 Test Execution Flow

### Android

```text
Android
   ↓
Termux
   ↓
Termux:X11
   ↓
Chromium
   ↓
Selenium WebDriver
   ↓
Pytest
   ↓
Login Page
```

### Desktop

```text
Windows / Linux / macOS
   ↓
Chrome / Chromium
   ↓
Selenium WebDriver
   ↓
Pytest
   ↓
Login Page
```

***

## 🔐 Test Credentials

The project uses dummy test credentials for automation practice.

- Do not commit real passwords.
- Do not store API keys or access tokens in source files.
- Review all credentials before uploading the project publicly.

***

## ⚠️ Important Notes

This project tests a live web application.

Test cases may require updates if the application changes its:

- HTML structure
- Element IDs
- CSS classes
- Validation messages
- Login workflow
- Authentication behavior

Test results may vary depending on the application's current behavior and the browser environment.

***

## ⭐ Project Highlights

- Selenium WebDriver automation
- Pytest test framework
- Explicit waits
- Positive and negative login scenarios
- Form validation testing
- Password masking validation
- Android Termux support
- Termux:X11 and Chromium support
- Windows, Linux and macOS support
- Separate environment-specific WebDriver configurations

***

**Made for learning and practicing Python-based web automation. 🚀**
