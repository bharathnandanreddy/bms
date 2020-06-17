

## Retail Bank Management



## Table of Contents

- 1 Purpose of the document
- 2 Business Overview
- 3 Stakeholders
- 4 Scope
- 5 Requirement Statements
   - 5.1 For New account executive/New customer
      - 5.1.1 Login Screen: <common function for any employee role>
      - Database table for login and password validation
      - 5.1.2 Create Customer Screen:
      - 5.1.3 Update Customer Screen:
      - 5.1.4 Delete Customer Screen:
      - 5.1.5 Create Account Screen:
      - 5.1.6 Delete Account Screen:
      - 5.1.7 View Customer Status Screen:
      - 5.1.8 View Account Status Screen:
      - 5.1.9 Create database table to store entries for customer and account status
   - 5.2 For Cashier/Teller
      - 5.2.1 Get Accounts and Account Details Screen:
      - 5.2.2 Deposit Screen:
      - 5.2.3 Withdraw Screen:
      - 5.2.4 Transfer Screen:
      - 5.2.5 Get Statement Screen:

## 1 Purpose of the document

This document intends to specify and layout the functional requirements of a new software
system required for **_Retail Bank employees as well as bank customers_** for the IT team to design and
deliver web based User Interface.

## 2 Business Overview

_Retail bank management_ is one of the most widely used application management functions in
banking and financial industry. This document specifies requirements, in a way, where in terms of both
bank employees and bank customers, there will be distinct set of functions. These should be made
available through well-defined User Interface.

**<ABC> Bank** is a retail bank which serves individual customers, to manage their savings and
current accounts. Key requirements of the system is the ability to create customer, open customer
account, update and delete customer, manage cashier transactions such as deposit, withdraw and
transfer. Also, to be able to view customer and account information and get account transaction
information.

## 3 Stakeholders

Bank Employees

- New account/New customer executive
- Cashier/Teller


## 4 Scope

The System needs to be able to handle primary functions that can be grouped into two set of activities,
with detailed requirement of each group explained in the requirement section.

```
New account executive/New customer
```
- Create, Update, Delete Customer
- Create and Delete Account
- View Customer and Account Status

```
Cashier/Teller
```
- Manage deposit, withdraw and transfer
- Get Customer and Account details
- Get Customer-Account Transactions/Get Statement


## 5 Requirement Statements

### 5.1 For New account executive/New customer

#### 5.1.1 Login Screen: <common function for any employee role>

```
To allow only bank employee to be able to login to bank web site
Login can be alphabetical or both alphanumeric with maximum n characters
Password can be alphabetical or both alphanumeric with maximum n characters
Implement session management on login operation.
Also, on every internal page, there should be logout link on click of which the logged in session
will be invalidated and user will be logged out.
```
#### Database table for login and password validation

```
RDBMS table
o Maintain your own RDBMS table for login and password
o Create table “userstore” with login, password and timestamp column(s)
o Read login and password information from table and based on verification,
options to allow user to continue to next pages or error message
```
#### 5.1.2 Create Customer Screen:

```
To allow new customer-account executive to create new customer
```
```
Input fields on screen:
```
```
Customer SSN ID, Customer Name, Age, Address Line1, Address Line2, City, State
```
```
Output message on screen after user clicks submit:
```
```
“Customer creation initiated successfully” Or Relevant error message to be displayed
```
#### 5.1.3 Update Customer Screen:

```
To allow account executive to update existing customer information
```
```
Before account executive can update anything, he/she should be able to query for existing
customer
```
```
a. Query/Pull existing customer:
```
```
Input fields on screen:
```
```
Either SSN ID or Customer ID as two input fields, with any one mandatory
```
```
Both fields are numeric and should have 9 digits
```

```
Output message on screen after user clicks submit:
```
```
Display following fields on screen: SSN ID, Customer ID, Name, Address, Age
```
```
Allow editing of fields, except SSN and Customer ID, by having update/edit button and editable
fields.
```
```
After editing of one or multiple fields, user can submit updated data
```
```
Output message on screen after user clicks submit:
```
```
“Customer update initiated successfully” Or Relevant error message to be displayed
```
#### 5.1.4 Delete Customer Screen:

```
To allow account executive to delete existing customer.
```
```
Before account executive can delete customer, he/she should be able to query for existing
customer by using query/pull existing customer screen.
```
```
Allow account executive to delete customer, with a delete button
```
```
Output message on screen after user clicks submit:
```
```
“Customer deletion initiated successfully” Or Relevant error message to be displayed.
```
#### 5.1.5 Create Account Screen:

```
To allow new customer-account executive to create new account for existing customer
```
```
Input fields on screen:
```
```
Customer ID
```
```
Drop down – Savings or Current Account
```
```
Deposit amount – Integer / Number (No decimals)
```
```
Output message on screen after user clicks submit:
```
```
“Account creation initiated successfully” Or Relevant error message to be displayed
```
#### 5.1.6 Delete Account Screen:

```
To allow account executive to delete existing account.
```
```
Before account executive can delete account, he/she should be able to query for existing account for
a customer by using query/pull existing customer accounts screen. Input is either Customer ID or SSN
ID.
```
```
Allow account executive to delete account, with a delete button
```

```
Output message on screen after user clicks submit:
```
```
“Account deletion initiated successfully” Or Relevant error message to be displayed
```
#### 5.1.7 View Customer Status Screen:

```
This screen shows rows of customers/SSN IDs and status of create/update/delete status. Each row
can have about five columns, i.e. SSN ID, Status, Message, Last Updated, Refresh Button
```
```
This can be either a separate screen or part of Create/Update/Delete Customer screen
```
```
There is no input in this screen, but it shows all customers, where the process is in progress or
complete.
```
```
Refresh button, in last column on each row, allows to pull latest status of each customer
```
#### 5.1.8 View Account Status Screen:

```
This screen shows rows with columns - customer ID, account type, status, message, Last updated and
refresh button.
```
```
This can be either a separate screen or part of Create/Delete Account screen
```
```
There is no input in this screen, but it shows all accounts, where the process is in progress or complete.
```
```
There should be refresh button, against each row, to pull latest status of each account
```
#### 5.1.9 Create database table to store entries for customer and account status

**Option1** : Create single table with column(s) e.g. Customer ID, SSN ID, Account ID, Account type,
status, message, Last updated

**Option2** : Create two separate tables – CustomerStatus, AccountStatus

CustomerStatus table columns – SSN ID, Customer ID, Status, Message, Last Updated

AccountStatus table columns – Customer ID, Account ID, Account Type, Status, Message, Last Updated

### 5.2 For Cashier/Teller

#### 5.2.1 Get Accounts and Account Details Screen:

```
To allow cashier to pull information for a specific account of a customer
```
```
Input fields:
```
```
Customer/SSN ID or Account ID
```
```
Output fields:
```

```
Displays account(s), as a drop drown if input is customer ID/SSN ID. If account ID is input, then display
relevant account information – Customer ID, Account ID, Account type, Balance
```
```
Output fields:
```
```
Customer ID, Account ID, Account Type, Account Balance, Amount to deposit
```
#### 5.2.2 Deposit Screen:

```
From account details screen, cashier can have option to deposit, withdraw or transfer money, as three
different buttons
```
```
In case of deposit screen, input fields:
```
```
Deposit amount
```
```
Output fields:
```
```
Customer ID, Account ID
```
```
Balance before deposit
```
```
Latest balance
```
```
Status message: “Amount deposited successfully”
```
#### 5.2.3 Withdraw Screen:

```
From account details screen, cashier can have option to deposit, withdraw or transfer money, as three
different buttons
```
```
In case of withdraw screen, input fields:
```
```
Withdraw amount
```
```
Output fields:
```
```
Account ID
```
```
Balance before withdraw
```
```
Latest balance
```
```
Status message: “Amount withdrawn successfully” or in case balance is not enough “Withdraw not
allowed, please choose smaller amount”
```
#### 5.2.4 Transfer Screen:

```
From account details screen, cashier can have option to deposit, withdraw or transfer money, as three
different buttons
```

```
In case of transfer screen, input fields:
```
```
Transfer amount, Source Account, Target Account
```
```
Output fields:
```
```
Source Account ID, Target Account ID
```
```
Balance before transfer for both account
```
```
Latest balance for both accounts
```
```
Status message: “Amount transfer completed successfully” or in case balance is not enough in source
account “Transfer not allowed, please choose smaller amount”
```
#### 5.2.5 Get Statement Screen:

```
To allow cashier to pull account statement for a customer-account
```
```
Input fields:
```
```
Account ID, Last N Transactions (option to choose from drop down 1-10) or Start date and End date
```
```
Output:
```
```
Account statement, with each row showing date, transaction description, credit or debit, balance
```
### 5.3 Validations

Validations required for input.

1. SSN, Account ID and Customer ID should be 9 digit
2. Date should be of the format CCYY-MM-DD

**Customer** (^)

#### Input SSN ws_ssn 9 digit numeric

#### Customer id ws_cust_id 9 digit numeric

#### Name ws_name alphabet

#### Address ws_adrs alphanumeric

#### Age ws_age 3 digit numeric

#### Account^

#### Input Customer id ws_cust_id 9 digit numeric

#### Account id ws_acct_id 9 digit numeric


#### Account type ws_acct_type S or C

#### Balance ws_acct_balance number add suffix 00

#### CR data ws_acct_crdate CCYY-MM-DD

#### CR last date ws_acct_lasttrdate CCYY-MM-DD

#### Duration ws_acct_duration number

#### Transactions

#### Input Customer id ws_cust_id 9 digit numeric

#### Account type ws_accnt_type S or C

#### Amount ws_amt number

#### Transaction date ws_trxn_date CCYY-MM-DD

#### Source Acct type ws_src_typ S or C

#### Target Acct type ws_tgt_typ S or C

### 5.4 Assumptions

Assumptions can be made and they are to be shared along with the Team details in the
assumptions tab.


