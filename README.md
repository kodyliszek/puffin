<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#swagger">Swagger</a></li>
    <li><a href="#tests">Tests</a></li>
    <li><a href="#contact">Contact</a></li>

  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


Small little bird who knows how to catch a fish.




<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

The solution is dockerized, so only thing that You need is docker Deamon installed on Your machine:
* docker [https://www.docker.com/get-started/](https://www.docker.com/get-started/)


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/kodyliszek/puffin
   ```
3. Install  packages
   ```sh
   pip install -r requirements.txt
   ```
4. Docker Compose
   ```sh
    docker-compose up;
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- Swagger -->
## Swagger

To reach swagger documentation, please use following url [http://127.0.0.1:5000/swagger-ui/#/](http://127.0.0.1:5000/swagger-ui/#/):
   ```sh
   export ENV_FILE_LOCATION=./.env.test
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- TESTS -->
## Tests

To run tests, first You have to setup `ENV_FILE_LOCATION` environmental variable.
To set this value mac/linux can run the command:
   ```sh
   export ENV_FILE_LOCATION=./.env.test
   ```
and windows user can run the command:
   ```sh
   set ENV_FILE_LOCATION=./.env.test
   ```
To run the test enter this command in your terminal.
   ```sh
   python -m unittest tests/test_report.py
   ```
or 

 ```sh
   python -m unittest tests/test_consumptions.py
   ```
You should be able to see the output like this:
 ```sh
   .
----------------------------------------------------------------------
Ran 6 test in 1.023s

OK
   ```
This means our test run successfully.
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Damian Filipkowski - [@https://kodyliszek.github.io/resume/](https://kodyliszek.github.io/resume/) - kodyliszek@gmail.com

Project Link: [https://github.com/kodyliszek/puffin](https://github.com/kodyliszek/puffin)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
