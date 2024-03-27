#HealthCareChatBot
This healthcare chatbot application is built using Amazon Lex, AWS Lambda, and DynamoDB. This chatbot is designed to assist users with medication suggestions, appointment booking, activity recommendations, health assessments, and more.

#Overview
HealthCareChatBot leverages the power of conversational interfaces to provide users with personalized healthcare assistance. With the integration of Amazon Lex, AWS Lambda, and DynamoDB, the chatbot offers a seamless and intuitive user experience.

#Features
Intent: suggestMedication
Description: Provides medication suggestions based on user symptoms.
Slots: PersonName, Symptoms, symptomDuration, symptomSeverity

Intent: appointmentBook
Description: Allows users to schedule appointments.
Slots: Name, Age, Location, Date, Time

Intent: suggestActivities
Description: Recommends physical or mental activities for users.
Slots: Name, weight, height

Intent: AssessHealth
Description: Assesses the user's health condition.
Slots: Name, weight, height, DiastolicBP, SystolicBP, Sugar, Cholesterol, StepsWalked, SleepHours, SleepQuality

Intent: StartingMenu
Description: Entry point for users to navigate through different features of the chatbot.

Setup
To deploy and use HealthCareChatBot, follow these steps:

Amazon Lex Configuration: Set up the necessary intents, slots, and utterances in Amazon Lex. Refer to the screenshots provided in the screenshots/intents_and_slots directory for guidance.

AWS Lambda Function: Implement the business logic for each intent in AWS Lambda functions. You can find the code for each Lambda function in the lambda_functions.py file.

DynamoDB Setup: Configure DynamoDB tables to store relevant data for your chatbot application. Refer to the screenshots in the screenshots/DynamoDB directory for table structure and settings.

Integration: Integrate the Amazon Lex bot with your preferred messaging platform or application. This can be done using the Kommunicate SDK or any other compatible platform.

Deployment: Deploy the Lambda functions and configure the necessary permissions. Ensure that the IAM roles associated with your Lambda functions have the required permissions to interact with Amazon Lex and DynamoDB.

#Usage
Once the setup is complete, users can interact with HealthCareChatBot through the integrated messaging platform. They can initiate conversations, provide input for different intents, and receive personalized responses based on their queries and inputs.

#Contributors
Hariprasad(https://github.com/hp113)






