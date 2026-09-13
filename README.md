# selenium-web-ui-testing
Python web UI automation testing using Selenium WebDriver and Microsoft Edge.

## About

The project demonstrates automated testing of a web application using Selenium WebDriver. The test program works with several predefined SauceDemo users and performs a sequence of actions in the browser.

The automated scenarios include:

* user login;
* product sorting;
* adding products to the shopping cart;
* removing products from the cart;
* opening the shopping cart;
* checkout;
* entering customer information;
* completing an order;
* navigation through the website menu;
* logout.

Microsoft Edge is used as the browser for automated testing.

This project was developed as a university coursework project during the third year of university.


## Main Functions

* users() - returns the list of user test functions that will be executed.
* safe_execute(driver, func, *args, **kwargs) - executes a test function and handles exceptions by displaying information about the error.
* spisok(driver) - tests product sorting using several available sorting options.
* menu(driver) - tests the main navigation menu of the website.
* cart_test(driver) - adds available products to the shopping cart and then removes them.
* test_web(driver) - performs the main web application testing scenario, including:
  * cart operations;
  * checkout;
  * customer information;
  * order completion;
  * navigation;
  * menu testing.
* standard_user(driver) - enters credentials for the standard user.
* locked_out_user(driver) - enters credentials for the locked-out user.
* problem_user(driver) - enters credentials for the problem user.
* performance_glitch_user(driver) - enters credentials for the performance-glitch user.
* error_user(driver) - enters credentials for the error user.
* visual_user(driver) - enters credentials for the visual user.
* test() - creates the Edge WebDriver, opens SauceDemo, runs the user scenarios, and closes the browser after each test.

## Key Variables

* driver - Selenium WebDriver instance;
* test_func - current user test function;
* sort_values - product sorting options;
* dropdown_element - product sorting dropdown element;
* dropdown - Selenium Select object;
* menu_items - website menu elements;
* product_ids - identifiers of tested products;
* add_cart - identifier for adding a product to the cart;
* remove_cart - identifier for removing a product from the cart;
* checkout_items - checkout form fields;
* checkout_values - values entered into checkout fields;
* item - current page element identifier;
* value - value entered into the current field.

## How to Run

1. Clone the repository

```bash
git clone https://github.com/dolzhkris/selenium-web-ui-testing.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the main Python script:

```bash
python main.py
```

The program will:

1. Start Microsoft Edge.
2. Open SauceDemo.
3. Log in using the current test account.
4. Execute the automated web scenario.
5. Close the browser.
6. Repeat the process for the next test user.

The test progress and errors are displayed in the console.
