# Alexa-fruit-machine
A small alexa funtion for a fruit machine, its a simple machine but works quite well. Just a quick disclosure, i'm not the best coder, but the function works. 

#Setup

1. You need to go to https://developer.amazon.com and navigate to the Alexa Skills Kit setup. Create a new skill.
2. There are a few intents that you need to setup, here is a screenshot of the intents that are required; https://img.kieren.uk/zmxcR67qzn.png
3. After the intents are setup, you need to start thinking about hosting your skill, It can be hosted on a custom server but requires many security functions. Or, you can use AWS which is what I'm using.
4. On AWS you are going to need to setup a Lambda function, these are free up to 1 million requests per month.
5. After creating the Lambda function you need to retreve the ARN (Amazon Resource Number) from your lambda program. 
6. Input the Lambda ARN into the alexa skills kit console. 
7. Upload both files to the Lambda function. Then Test away.

# What can you use this for?
Since this function is already on the store, it doesnt need to be submitted again, so I hope to publish these scripts for other coders that are looking into making an Alexa skill.
I struggled alot to learn how to make an alexa skill, so if you have any questions I might be able to answer them, my email is hello@kieren.uk
