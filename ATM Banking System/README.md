# ATM Banking System

<p>A console-based ATM Banking System built with Python to practice Object-Oriented Programming (OOP) concepts through basic banking operations.</p>

<h2>Overview</h2>

<p>This project simulates basic ATM functionality using Python classes and a menu-driven interface. It demonstrates how inheritance and encapsulation can be used to organize banking operations and manage account information.</p>

<p>The project consists of a <code>BankAccount</code> parent class for balance management and an <code>Atm</code> child class that provides ATM operations with PIN verification.</p>

<h2>Features</h2>

<ul>
<li><strong>Account Management:</strong> Initialize and maintain the account balance.</li>
<li><strong>Deposit:</strong> Deposit money into the account with amount validation.</li>
<li><strong>Withdrawal:</strong> Withdraw money with balance and amount validation.</li>
<li><strong>Balance Inquiry:</strong> Check the current account balance after PIN verification.</li>
<li><strong>PIN Management:</strong> Set and update the account PIN.</li>
<li><strong>PIN Verification:</strong> Verify the PIN before performing transactions.</li>
<li><strong>Menu-Driven Interface:</strong> Navigate through ATM operations using a simple console menu.</li>
</ul>

<h2>Object-Oriented Programming Concepts</h2>

<ul>
<li><strong>Inheritance:</strong> The <code>Atm</code> class inherits from the <code>BankAccount</code> class.</li>
<li><strong>Encapsulation:</strong> Private attributes (<code>__balance</code> and <code>__pin</code>) are used to manage account information.</li>
<li><strong>Constructor Inheritance:</strong> <code>super()</code> is used to initialize the parent class and access its banking operations.</li>
<li><strong>Method Overriding:</strong> The <code>Atm</code> class overrides <code>check_balance()</code> to require PIN verification before displaying the balance.</li>
</ul>

<h2>Technologies Used</h2>

<ul>
<li><strong>Language:</strong> Python</li>
<li><strong>Concepts:</strong> Classes, objects, constructors, inheritance, encapsulation, and methods.</li>
</ul>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>

<ul>
<li>Python 3 installed on your system.</li>
<li>A terminal or code editor to run the program.</li>
</ul>

<h3>Installation and Execution</h3>

<p><strong>Clone the repository:</strong></p>

<pre><code>git clone &lt;repository-url&gt;</code></pre>

<p><strong>Navigate to the project directory:</strong></p>

<pre><code>cd &lt;project-directory&gt;</code></pre>

<p><strong>Run the Python program:</strong></p>

<pre><code>python main.py</code></pre>

<p>Replace <code>main.py</code> with the actual Python filename if it differs.</p>

<h2>Usage</h2>

<p>When you run the program, a menu displays the available operations:</p>

<ul>
<li>Set PIN</li>
<li>Deposit</li>
<li>Withdraw</li>
<li>Check Balance</li>
<li>Exit</li>
</ul>

<p>Select an option and follow the prompts. The default PIN is 1234 until it is changed.</p>

<h2>Project Status</h2>

<p><strong>In Development</strong></p>

<p>This project is a learning exercise focused on understanding Python Object-Oriented Programming. Future improvements may include stronger input validation, limited PIN attempts, and additional banking features.</p>

<h2>Disclaimer</h2>

<p>This project is intended for educational purposes only. It is not a production-ready banking application and should not be used to manage real financial accounts or sensitive information.</p>