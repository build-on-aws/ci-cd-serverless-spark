## Serverless Spark CI/CD on AWS with GitHub Actions

Sample code repo that shows how to run GitHub Actions with Amazon EMR Serverless. Forms the basis of the following tutorial:

- [Deploy Serverless Spark jobs to AWS using GitHub Actions](https://buildon.aws/tutorials/deploy-serverless-spark-jobs-to-aws-using-github-actions)

The code here represents what your repository should look like after following the tutorial.

## Pre-requisites

- An AWS Account with Admin privileges
- GitHub OIDC Provider in AWS
- S3 Bucket(s)
- EMR Serverless Spark application(s)
- IAM Roles for GitHub and EMR Serverless

You can create all of these, including some sample data, using the included [CloudFormation template](template.cfn.yaml).

> **Warning** 💰 The CloudFormation template creates EMR Serverless applications that you will be charged for when integration tests **AND** the scheduled workflow runs.

> **Note** The IAM roles created in the template are _very tightly scoped_ to the relevant S3 Buckets and EMR Serverless applications created by the stack.

## Other resources

- [EMR Serverless User Guide](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html)
- [EMR Serverless Samples](https://github.com/aws-samples/emr-serverless-samples/)
- [EMR toolkit for VS Code](https://marketplace.visualstudio.com/items?itemName=AmazonEMR.emr-tools)
- [Amazon EMR CLI](https://github.com/awslabs/amazon-emr-cli)

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
