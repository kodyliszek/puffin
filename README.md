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
        <li><a href="#docker">Docker</a></li>
        <li><a href="#local">Local</a></li>
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
To get a local copy up and running follow these simple example steps. You have two options: to run project in docker or on or local machine:


### Docker

The solution is dockerized, so only thing that You need is docker Deamon installed on Your machine:
* docker [https://www.docker.com/get-started/](https://www.docker.com/get-started/)
enter puffin DIR and run:
```sh
   docker-compose up
   ```


### Local

1. Clone the repo
   ```sh
   git clone https://github.com/kodyliszek/puffin
   ```
2. Enter puffin DIR
   ```sh
   cd puffin
   ```
3. Activate virtualenv
 - if You do not have virtualenv install it with following command 
   ```sh
      pip install virtualenv
      ```
 - create new virtualenv with following command 
   ```sh
      python<version> -m venv <virtual-environment-name>
      ```
   e.g.
   ```sh
      python3.8 -m venv env3.8
      ```
 - activate virtualenv with following command 
    ```sh
    source env/bin/activate
    ```
4. Install  packages
   ```sh
   pip install -r requirements.txt
   ```
5. Change .env file in .en file `MONGODB_SETTINGS` phrase `mongodb:27017/puffin_db` have to be changed to `localhost:27017/puffin_db`
6. Set `ENV_FILE_LOCATION`
   To set this value mac/linux can run the command:
   ```sh
    export ENV_FILE_LOCATION=./.env
   ```
   and windows user can run the command:
      ```sh
    set ENV_FILE_LOCATION=./.env
   ```
7. in .env file put config to Your MongoDB:
8. Run Flask:
   ```sh
   flask run
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- Swagger -->
## Swagger

To reach swagger documentation, please use following url [http://127.0.0.1:5000/swagger-ui/#/](http://127.0.0.1:5000/swagger-ui/#/):

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- TESTS -->
## Tests
Unit tests are included in repository. You can run them in two ways on docker container or locally:
### Tests on Docker
To run tests on docker You have to start containers with command:
   ```sh
   docker-compose run --rm --entrypoint "python -m unittest tests/test_reports.py" test
   ```
or
   ```sh
   docker-compose run --rm --entrypoint "python -m unittest tests/test_consumptions.py" test
   ```
depending which model You want to test.

### Tests Locally
To run Test locally You have to do all above steps for Getting Started - Local.

1. Set in .env.test change MongoDb config to Your test DB. Remember to change `MONGODB_SETTINGS` phrase `mongodb:27017/puffin_db` have to be changed to `localhost:27017/puffin_db`

2. To run tests, first You have to change `ENV_FILE_LOCATION` environmental variable.
To set this value mac/linux can run the command:
   ```sh
   export ENV_FILE_LOCATION=./.env.test
   ```
   and windows user can run the command:
   ```sh
   set ENV_FILE_LOCATION=./.env.test
   ```
3. To run the test enter this command in your terminal.
   ```sh
   python -m unittest tests/test_report.py
   ```
   or 

    ```sh
      python -m unittest tests/test_consumptions.py
      ```
4. You should be able to see the output like this:
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
