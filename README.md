# Docker Exam
Docker exam featuring an api container and 3 individual containers performing a different test each on the api.
Outcomes of the tests are logged in a shared logfile. 
All output is logged in another file.


## Presentation
For the correction of this exercise, we will try to create a CI/CD pipeline to test an API. We will put ourselves in the shoes of a team that is supposed to create a set of tests to be applied automatically before deployment.

In our scenario, a team has created an application that allows to use a sentiment analysis algorithm: it allows to predict if a sentence is positive or negative. This API will be deployed in a container whose image is for the moment datascientest/fastapi:1.0.0.

Let's look at the entry points of our API:

- /status returns 1 if the API is running
- /permissions returns a user's permissions
- /v1/sentiment returns the sentiment analysis using an old model
- /v2/sentiment returns the sentiment analysis using a new template

The /status entry point simply checks that the API is working.
The /permissions entry point allows someone, identified by a username and a password to see which version of the template they have access to.
Finally the last two take a sentence as input, check that the user is identified,
check that the user has the right to use this template and if so, return the sentiment score: -1 is negative; +1 is positive.

To download the image, run the following command : `docker image pull datascientest/fastapi:1.0.0`

To test the API manually, run the command : `docker container run -p 8000:8000 datascientest/fastapi:1.0.0`

The API is available on port 8000 of the host machine. At the entry point /docs you can find a detailed description of the entry points.

We will define some test scenarios that will be done via separate containers.

## Tests
### Authentication
In this first test, we are going to check that the identification logic works well. To do this, we will need to make GET requests on the /permissions entry point.
We know that two users exist alice and bob and their passwords are wonderland and builder. We'll try a 3rd test with a password that doesn't work: clementine and mandarine.

The first two requests should return a 200 error code while the third should return a 403 error code.

### Authorization
In this second test, we will verify that our user authorization logic is working properly. We know that bob only has access to v1 while alice has access to both versions.
For each of the users, we will make a query on the /v1/sentiment and /v2/sentiment entry points:
we must then provide the arguments username, password and sentence which contains the sentence to be analyzed.

### Content
In this last test, we check that the API works as it should. We will test the following sentences with the alice account:

life is beautiful
that sucks
For each version of the model, we should get a positive score for the first sentence and a negative score for the second sentence.
The test will consist in checking the positivity or negativity of the score.

## Building the tests
For each of the tests, we want to create a separate container that will run those tests.
The idea of having one container per test means that the entire test pipeline does not have to be changed if only one of the components has changed.

When a test is run, if an environment variable LOG is set to 1, then a log should be printed in a api_test.log file.

You are free to choose the technology used: the Python libraries requests and os seem to be affordable options.

## Solution

A shared volume for the logfile and another one for the scripts so scripts can be adapted when containers are offline.
This also avoids copying the scripts to the containers.
Shared network of course.
Use for loops to cycle through users, urls and sentences.
Create dependencies between the containers to order the tests and avoid simultaneous writing to the log file.
And some other stuff.


