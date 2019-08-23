# tomster

## About

This project features a python web application utilizing flask framework.  Docker was used for containerization.  Alpine linux was used for the operating system.  Bash was used for scripts.  The code pipeline leverages IAM, s3, CodePipeline, CodeCommit, CodeBuild, and ECR.  CloudFormation was used for infrastructure as code.  Route 53 is handling DNS.  EC2 and associated services were used to host the kubernetes environment.  Cloud9 was used as the IDE.

## Get Started

The code in this repo offers 2 ways for deploying the application:

* Option 1: Local docker
* Option 2: CodePipeline to kubernetes

### Option 1: Local docker

This will build the docker image and run it locally on your machine.

#### Setup

1. Clone this github repo.

    ```bash
    git clone https://github.com/tommygarvin/tomster.git
    ```

1. Build the docker image.

    ```bash
    docker build -t tomster:001 ./tomster/build/
    ```

1. Run the docker image.  Expose port 5000.

    ```bash
    docker run -d -p 5000:5000 tomster:001
    ```

#### Verify

1. GET messagelist

    ```bash
    curl 127.0.0.1:5000/api/v1/messagelist
    ```

1. GET messages/message1

    ```bash
    curl 127.0.0.1:5000/api/v1/messages/message1
    ```

#### Cleanup

1. Stop 'tomster' containers

    ```bash
    docker ps -a | awk '/tomster/ {print $1}' | xargs docker stop
    ```

1. Remove unused resources

    ```bash
    docker system prune
    ```

1. Remove 'tomster' images

    ```bash
    docker images | awk '/tomster/ {print $3}' | xargs docker rmi
    ```

### Option 2: CodePipeline to kubernetes

This will deploy an AWS CodePipeline that builds and deploys the application to a kubernetes cluster of your choosing.  I recommend kops https://github.com/kubernetes/kops if you need a kubernetes environment.

<img src="https://tommygarvin-001.s3.amazonaws.com/tomster.png">

View in <a href="https://console.aws.amazon.com/cloudformation/designer/home?region=us-east-1&templateURL=https://tommygarvin-001.s3.amazonaws.com/cfn.json">CloudFormation Designer</a>

#### Setup

1. Deploy the AWS CodePipeline stack via CloudFormation:

    <a href="https://console.aws.amazon.com/cloudformation/home?#/stacks/new?&templateURL=https://tommygarvin-001.s3.amazonaws.com/cfn.json" target="_blank"><img src="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png"></a>

1. Copy the contents of this GitHub repo into the CodeCommit repo.
1. Create a new AWS Route 53 alias record for the url you wish to use. Set the alias to your kubernetes ingress controller.  Reference ./deploy/aws-r53.json for example.
1. Update ./deploy/k8s-ing.yml with your url.
1. Update ./deploy/config with your kubectl config.
1. Git add, commit, and push the files to the CodeCommit repo.
1. Browse to AWS CodePipeline.  Hit 'release change'.  Wait for the pipeline to complete.

#### Verify

1. GET messagelist

    ```bash
    curl tomster.tommygarvin.com/api/v1/messagelist
    ```

1. GET messages/message1

    ```bash
    curl tomster.tommygarvin.com/api/v1/messages/message1
    ```

#### Cleanup

1. Delete AWS CloudFormation stack.
1. Delete AWS Route 53 alias record.
1. Delete k8s namespace 'tomster'

## Application Usage

### /messagelist

GET - Returns all messages

POST - Add a new message

### /messages/<message_id>

GET - Returns the specified message

DELETE - Delete the specified message

PUT - Updates the specified message

### Live from my AWS account

<http://tomster.tommygarvin.com/api>

<http://tomster.tommygarvin.com/api/v1/messagelist>

<http://tomster.tommygarvin.com/api/v1/messages/message1>

<http://tomster.tommygarvin.com/api/v1/messages/message2>

<http://tomster.tommygarvin.com/api/v1/messages/message3>
