# Tutorial & Guides Library

Welcome to our [Tutorials and Guides Library](https://developer.moveworks.com/creator-studio/resources/), designed to inspire you and enhance your experience with Creator Studio. Find detailed instructions and best practices for quick and effective implementation.

There are several types of guides and tutorials:

1. **Authentication Guide** (`./authentication-guides`): Follow these authentication guides to connect your copilot to your favorite systems in Creator Studio.
2. **Design Patterns** (`./design-patterns`): Learn to combine triggers, slots, actions, and guidelines to accomplish common copilot tasks. [Read more on design patterns](https://developer.moveworks.com/creator-studio/design-patterns/overview/).
3. **Use Case Guides** (`./use-case-guides`): Follow our use case guides for end-to-end tutorials on the most popular use cases.

You can search all our guides [on our developer site](https://developer.moveworks.com/creator-studio/resources/) for a better experience.

## How do I request a guide?

You’ll need a Github account to request a guide. You can [create one for free](https://github.com/signup). 

If you’re looking for a guide, but don’t see one, try to **upvote an existing request for a guide**.

1. Go to our [most-popular open issues](https://github.com/moveworksinc/developer-docs/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions-%2B1-desc)
2. Search for your guide in the _Filters_ search box
    
    ![Searching issues](./contributing/search.png)
    
3. Upvote the issue
    
    ![Upvoting issues](./contributing/upvote.png)
    

If there is no existing request for that guide, you can **submit a new request**

1. Click here to [create a new issue](https://github.com/moveworksinc/developer-docs/issues/new/choose)
2. Pick the type of guide you'd like to request
3. Tell us about your guide!

## Adding & Editing Guides

Our library grows in value with each contribution. You can edit any guide that feels wrong or unclear. You can also add your own guides if you have one to share with the community.

[Learn to contribute here.](./.github/CONTRIBUTING.md)

## Closing Thoughts

Thank you for contributing to our resource library. Your effort will go a long way in enhancing the experience of developers just like you. If you need further assistance, please reach out.

- [Academy](https://academy.moveworks.com/page/persona-developer)
- [Community](https://community.moveworks.com/developer-hub-6)
- [Support](https://developer.moveworks.com/creator-studio/support/)


***Disclaimer:** This code is provided as an example only and is not designed for production use. You should fully understand the code and consider all the security implications before using it in a live environment.
# Welcome Contributors!

Thank you for contributing! This guide will walk you through how to add new guides to the Moveworks Tutorials & Guides Library.

If it’s your first time contributing, try tackling issues labeled `good-first-issue` for something simple, or [see which requests have the most likes](https://github.com/moveworksinc/developer-docs/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions-%2B1-desc) to help as much of the community as possible.

## Add new guides

### Prerequisites

You'll need a running [Github Desktop](https://desktop.github.com/) setup. If you haven't installed it yet, refer to the official Github Desktop guide.

### Tutorial Videos

- [Setup your repository](https://www.loom.com/share/f5b299cb4c264cf7b818ddf11c9f6b63)
- [Add your content](https://www.loom.com/share/730e5afb24444afba5688597e2be7c44)

### Steps

1. **Fork the Repository**: On the main page of the repository, click on **`Fork`** button located in the upper right-hand corner. This will create a copy of the repository in your account.
2. **Clone the Repository**: Open GitHub Desktop and click on **`File -> Clone repository`**, select the forked repository from the list and choose the local folder where you want the repository files.
3. **Create a New Branch**: In GitHub Desktop, click on the branch dropdown and select **`New Branch`** option. Give the branch a name (e.g., **`add-my-use-case-guide`**). Click the **`Create Branch`** button.
4. **Add Your Content**: Navigate to the cloned repository folder using your file explorer. From there, move to the directory where you want to add a guide (i.e., either **`./use-case-guide`**, **`./design-pattern`**, or **`./authentication-guide`**). In this directory, create a new "guide directory", which must include a `README.md` file, along with any other necessary files.
5. **Ensure Your Guide Adheres to the Format**: Your README.md file and accompanying files must follow [the rules below](https://github.com/moveworksinc/developer-docs/blob/main/README.md#guide-requirements).
6. **Add and Commit the Changes**: Return to GitHub Desktop. You should see the files you added listed under "Changes". Provide a summary and description for changes made, then click on **`Commit to <your-branch-name>`**.
7. **Push the Changes**: Click on the **`Push origin`** button at the top to push your changes to the remote repository on GitHub.
8. **Create a Pull Request**: Navigate back to your forked repository on GitHub, switch to your branch, and click on **`Pull request`**. Fill out the pull request form, then click on **`Create pull request`**.

## Edit existing guides

If you're making changes to existing files or if you'd like to work via Github directly:

1. Navigate to the file you want to edit.
2. Click on the pencil icon in the top-right corner of the file view to edit. You’ll be prompted to fork the repository to propose changes.
3. Make your changes, then scroll down to see the `Propose changes` button. Click on it.
4. You will be redirected to the 'Comparing changes' view, where you can create a pull request.
5. Start your pull request / commit with `[non-contributing]` if you do not want credit for your edit. (e.g. “[non-contributing] fix spelling mistakes”).

## Guide Requirements

When you create a new guide, you'll create a "content folder" in one of the guide directories:

1. Authentication Guide (`./authentication-guides`)
2. Design Patterns (`./design-patterns`)
3. Use Case Guides (`./use-case-guides`)

You'll need to make sure your content follows these rules:

### URL Rules

URLs are written as `[Text](link)`

1. URLs should only point to publicly accessible URLs.
2. URLs should only point to assets within your content folder. You can reference README files from other guides, but do not access their images in your guides.

### File Structure

1. Your content folder should be unique across the repository (regardless of the tutorial/guide type)
2. Every content folder MUST have a `README.md`
3. If you're building an Authentication Guide, you must have a `logo.png` in your content folder.

### File Metadata

Some metadata needs to be placed at the top of the file. That metadata changes based on the type of guide you're creating. Identify your guide type below.

#### Authentication Guides

Files in this directory require the following content at the top of the file:

```
---
name: <Guide Name>   # The name of the guide
description: <Description>   # Brief description of the guide
time_in_minutes: <Time in Minutes>   # Time in minutes to complete the guide
difficulty_level: <Difficulty Level>  # Difficulty level: "Beginner", "Intermediate", or "Advanced"
---
```

#### Design Patterns

Files in this directory require the following content at the top of the file:

```
---
id: <Design Pattern ID>  # Unique ID number for the design pattern
name: <Design Pattern Name>   # Name of the design pattern
description: <Description>   # Brief description of the design pattern
time_in_minutes: <Time in Minutes>  # Time in minutes to complete the pattern
purple_chat_link: <Purple Chat Link>   # URL of the related chat
difficulty_level: <Difficulty Level>   # Difficulty level: "Beginner", "Intermediate", or "Advanced"
---
```

#### Use Case Guides

Files in this directory require the following content at the top of the file:

```
---
design_pattern_id: <Design Pattern ID>  # The ID of the associated design pattern
name: <Use Case Name>  # Name of the use case
description: <Description>  # Brief description of the use case
systems: [<System1>, <System2>, ...]  # List of systems involved in the use case
purple_chat_link: <Purple Chat Link>  # URL of the linked chat
time_in_minutes: <Time in Minutes>  # Time in minutes to complete the use case
difficulty_level: <Difficulty Level>  # Difficulty level: "Beginner", "Intermediate", or "Advanced"
---
```

1. `systems`: This field should be an array of folder names from the `./authentication-guides` directory.
2. `design_pattern_id`: This should match the id of an existing design pattern in the design-patterns directory.

## Pull Requests

We provide feedback directly on your pull requests if changes need to be made. Please address any feedback in a timely fashion.

## License

By contributing to examples, you agree that your contributions will be licensed under the LICENSE file in the root directory of this source tree.

## Closing Thoughts

Thank you for contributing to our resource library. Your effort will go a long way in enhancing the experience of developers just like you. If you need further assistance, please reach out.

- [Academy](https://academy.moveworks.com/page/persona-developer)
- [Community](https://community.moveworks.com/developer-hub-6)
- [Support](https://developer.moveworks.com/creator-studio/support/)
---
name: Authentication Guide Request
about: Request a new authentication guide
title: "[Auth Guide] {{SYSTEM_NAME}}"
labels: 'request: authentication guide'
assignees: ''

---

# Authentication Guide Request: {{SYSTEM_NAME}}

**Link:** _Add a link to the product homepage here. There can be multiple products sold by one company, so product homepages are essential_

# Research

Add links and notes on any research you've already done for this system
---
name: Report an Issue
about: Report an Issue
title: "[BUG] Description"
labels: invalid
assignees: ''

---

# Issue Report

**Link to Resource**
Provide a link to the resource / guide that's problematic.

**What's wrong**
Describe what's wrong with the resource / guide
---
name: Use Case Guide Request
about: Request a new use case guide
title: "[Use Case] {{USE_CASE_TITLE}}"
labels: 'request: use case guide'
assignees: ''

---

# Use Case Guide Request: {{USE_CASE_TITLE}}

**Description of Use Case:**
Briefly describe what the use case should do

**System:** 
Include a link to an existing authentication guide at https://developer.moveworks.com/creator-studio/resources, or create an authentication guide issue and link it here

**(Optional) Purple Chat Mockup:**
Draft a purple chat mockup of your use case here: https://developer.moveworks.com/creator-studio/purple-chat-builder

# Research

Add links and notes on any research you've already done for this use case
# Welcome to our guides
### Important disclaimers
 - This code is provided as an example only and is not designed for production use. You should fully understand the code and consider all the security implications before using it in a live environment.
 - API keys / tokens are examples and not live
---
name: Asana
description: Connect Creator Studio to Asana
time_in_minutes: 15
difficulty_level: Beginner
---

# **Introduction**

Asana's API provides a robust platform to integrate and streamline tasks in your Asana workspace. This guide will demonstrate how to create an Asana Personal Access Token (PAT), authenticate with Asana's API, and test it in Creator Studio.

# **Prerequisites**

- Access to an Asana workspace
- [Install Postman](https://www.postman.com/downloads/)

# **Walkthrough**

## **Step 1: Create a Personal Access Token**

1. Go to the [Asana developer console](https://app.asana.com/0/my-apps)
2. Click on `Create New Token` under `Personal access tokens`. 
    
    ![Untitled](Authentication%20Guide%20Asana%20187c2020eb774256ab9e452a4efdb183/Untitled.png)
    
3. Provide a description for your key
    
    ![Untitled](Authentication%20Guide%20Asana%20187c2020eb774256ab9e452a4efdb183/Untitled%201.png)
    
4. Copy the token
    
    ![Untitled](Authentication%20Guide%20Asana%20187c2020eb774256ab9e452a4efdb183/Untitled%202.png)
    

## **Step 2: Test with Postman**

1. Set up your request in Postman with your `Personal access token`.
    
    ```bash
    curl https://app.asana.com/api/1.0/users/me \
      -H "Authorization: Bearer {{YOUR_PERSONAL_ACCESS_TOKEN}}"
    ```
    
2. Import this request into Postman and execute it. You should get a successful response of your user information.
    
    ![Untitled](Authentication%20Guide%20Asana%20187c2020eb774256ab9e452a4efdb183/Untitled%203.png)
    

## **Step 3: Integrate with Creator Studio**

1. In Creator Studio, create a new connector with the following configuration:
    - Base URL: `https://app.asana.com/api`
    - Auth Config: `Api Key Auth`
    - Api Key Auth Auth Type: `Header Auth`
    - Header Auth Key: `Authorization`
    - Header Auth Value Pattern: `Bearer %s`
    - Api Key: `{{your_personal_access_token}}`
2. Define your API action for channel creation.
    
    ```bash
    curl https://app.asana.com/api/1.0/users/me \
      -H "Authorization: Bearer {{YOUR_PERSONAL_ACCESS_TOKEN}}"
    ```
    
    - Path: `/1.0/users/me`
    - Method: `GET`
3. Test your setup in Creator Studio and look for a successful execution.
    
    ```json
    
    {
    	"data": {
    		"email": "************",
    		"gid": "1200311869439617",
    		"name": "Ajay Merchia",
    		...
    	}
    }
    ```
    

# **Congratulations!**

You've successfully integrated Asana’s API with Creator Studio. This opens up a variety of automation and integration possibilities within your Asana workspace.
---
name: Azure Function Apps   # The name of the guide
description: Connect Creator Studio to Azure Function Apps   # Brief description of the guide
time_in_minutes: 60   # Time in minutes to complete the guide
difficulty_level: Advanced  # Difficulty level: "Beginner", "Intermediate", or "Advanced"
---

# Introduction

Azure Functions is a serverless computing service provided by Microsoft Azure, offering an event-driven approach to building and deploying applications. 

In this guide, we will demonstrate how to authenticate with an Azure Function App from Creator Studio. We will walk through creating a function app, implementing code, deploying it to Azure, testing it in Postman, and connecting it to Creator Studio

We are going to use the [Star Wars API](https://swapi.dev/) to build an API that returns a list of starships & vehicles based on the name of a Star Wars character.

# Prerequisites

- [Create an Azure Account](https://learn.microsoft.com/en-us/office/developer-program/microsoft-365-developer-program-get-started)
- [Install VS Code](https://code.visualstudio.com/) or your code editor of choice
- [Install the Azure Functions Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) (make sure you link your Azure account)
    
    ![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled.png)
    
- [Install Postman](https://www.postman.com/downloads/) or your API tester of choice
- [Install Python](https://www.python.org/downloads/)

# Steps

## Step 1: Create Function

1. In the `Azure` tab, under `Workspace`, click the Azure Function App icon, then click `Create Function`
    
    ![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled%201.png)
    
2. For the prompts, use the following settings:
    
    ![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled%202.png)
    
    - Folder: Any
    - Language: `Python`
    - Programming Model: `V2`
    - Interpreter: Choose the version of Python you installed. I’m using 3.9.6 for this one.
3. Setup an `HTTP Trigger`
    
    ![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled%203.png)
    
    - Function name: `creator_studio_hello_world`
    - Authorization Level: `Function`
4. Your Function App should automatically populate in VS Code!
    
    ![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled%204.png)
    

## Step 2: Add some code

### Pseudocode

Our function will do roughly the following

1. Retrieve the name of the star wars character based on a search parameter. We’ll just take the first result to simplify things.
    
    ```jsx
    https://swapi.dev/api/people?search={{name}}
    
    // Example where "name" = "Luke"
    
    {
    	"count": 1,
    	"next": null,
    	"previous": null,
    	"results": [
    		{
    			"name": "Luke Skywalker",
    			"height": "172",
    			"mass": "77",
    			"hair_color": "blond",
    			"skin_color": "fair",
    			"eye_color": "blue",
    			"birth_year": "19BBY",
    			"gender": "male",
    			"homeworld": "https://swapi.dev/api/planets/1/",
    			"films": [
    				"https://swapi.dev/api/films/1/",
    				"https://swapi.dev/api/films/2/",
    				"https://swapi.dev/api/films/3/",
    				"https://swapi.dev/api/films/6/"
    			],
    			"species": [],
    			"vehicles": [
    				"https://swapi.dev/api/vehicles/14/",
    				"https://swapi.dev/api/vehicles/30/"
    			],
    			"starships": [
    				"https://swapi.dev/api/starships/12/",
    				"https://swapi.dev/api/starships/22/"
    			],
    			"created": "2014-12-09T13:50:51.644000Z",
    			"edited": "2014-12-20T21:17:56.891000Z",
    			"url": "https://swapi.dev/api/people/1/"
    		}
    	]
    }
    ```
    
2. Retrieve all vehicles belonging to the character
    
    ```jsx
    "https://swapi.dev/api/vehicles/14/"
    "https://swapi.dev/api/vehicles/30/"
    ```
    
3. Retrieve all starships belonging to the character
    
    ```jsx
    "https://swapi.dev/api/starships/12/"
    "https://swapi.dev/api/starships/22/"
    ```
    
4. Merge the results into 1 response.
    
    ```jsx
    {
    	"results": [
    		{
    			"type": "Vehicle",
    			"id": "14",
    			"name": "Speeder",
    			...
    		},
    		...
    	]
    }
    ```
    

### Install Dependencies

Since we are going to make API calls, we’ll need the `requests` library. Add it to your `requirements.txt` file.

![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled%205.png)

### Implement the code

You can modify the default code to the following to implement our pseudocode.

```python
import azure.functions as func
import logging
import json
import requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="creator_studio_hello_world")
def creator_studio_hello_world(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    # Attempt to parse the "name" from the query parameter
    name = req.params.get("name")

    # Parse the "name" from the JSON body if it's not in the query
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get("name")

    if name:
        # Find a matching character
        response = requests.get(f"https://swapi.dev/api/people?search={name}")
        result = response.json()

        try:
            character = result["results"][0]
        except IndexError:
            return func.HttpResponse(
                json.dumps({"error": f"No results found for {name}"}),
                mimetype="application/json",
                status_code=404,
            )

        # Initialize an array to store all vehicles & starships in
        all_transportation = []

        # Get details for all vehicles this character has
        for vehicle_url in character["vehicles"]:
            # Parse the vehicle ID from the URL (e.g. https://swapi.dev/api/vehicles/14/)
            vehicle_id = vehicle_url.split("/")[-2]
            response = requests.get(vehicle_url)
            result = response.json()

            all_transportation.append(
                {
                    "type": "Vehicle",
                    "full-id": f"Vehicle-{vehicle_id}",
                    "name": result["name"],
                    "model": result["model"],
                    "cost": result["cost_in_credits"],
                }
            )

        # Get details for all starships this character has
        for starship_url in character["starships"]:
            # Parse the vehicle ID from the URL (e.g. https://swapi.dev/api/starships/12/)
            starship_id = starship_url.split("/")[-2]
            response = requests.get(starship_url)
            result = response.json()

            all_transportation.append(
                {
                    "type": "Starship",
                    "full-id": f"Starship-{starship_id}",
                    "name": result["name"],
                    "model": result["model"],
                    "cost": result["cost_in_credits"],
                }
            )

        return func.HttpResponse(
            json.dumps({"results": all_transportation}),
            mimetype="application/json",
            status_code=200,
        )
    else:
        return func.HttpResponse(
            body=json.dumps({"error": "Please provide a name"}),
            mimetype="application/json",
            status_code=400,
        )
```

## Step 3: Test Locally

1. In the `Run & Debug` tab click the `Run` icon (the green triangle).
    
    ![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled%206.png)
    
    You should get a function URL in your terminal output. Ours is `http://localhost:7071/api/creator_studio_hello_world`
    
2. Open Postman and place your function URL in the URL bar
    
    ![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled%207.png)
    
3. Try out a few variations. Make sure you’re handling errors appropriately.
    1. GET request with no parameters
        
        ![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled%208.png)
        
    2. GET request with a query parameter
        
        ![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled%209.png)
        
    3. POST request with a search body
        
        ![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled%2010.png)
        

## Step 4: Deploy & Test

1. Go back to the Azure tab. Click the Azure Function Icon again, and this time select `Create Function App in Azure`
    
    ![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled%2011.png)
    
2. Name your app. I’m naming mine `creator-studio-tutorials-ajay`
    
    ![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled%2012.png)
    
3. You will probably want to select the same python version you’re using locally.
    
    ![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled%2013.png)
    
4. Use the recommended region. You want to provision the app where you have a subscription.
    
    ![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled%2014.png)
    
5. Click the Azure Function Icon again, and this time select `Deploy to Function App`
    
    ![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled%2015.png)
    
6. Select the function app you created
    
    ![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled%2016.png)
    
7. Check your output for a successful deployment
    
    ![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled%2017.png)
    
    Make sure you jot down your API URL `creator-studio-tutorials-ajay.azurewebsites.net`
    
8. Final step, let’s get the “Function Key” used to authenticate this API
    
    ![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled%2018.png)
    
9. Now we can test in Postman. 
    - Swap the localhost out for your API URL
    - Add a new URL parameter `code` and set that to your Function Key.
    
    ![Untitled](Authentication%20Guide%20Azure%20Function%20Apps%207503f66bf6994df5b7bb481e05e82e9f/Untitled%2019.png)
    

Nice! We have a working API endpoint to connect to Creator Studio.

## Step 5: Connect to Creator Studio

1. In your API editor, create a new connector. You can read more about the supported auth types on [our connector reference](https://developer.moveworks.com/creator-studio/connector-configuration/).
    - Base Url: `https://creator-studio-tutorials-ajay.azurewebsites.net`
    - Auth Config: `Api Key Auth`
    - Api Key Auth Auth Type: `Param Auth`
    - Param Auth Param Name: `code`
    - API Key: `{{function_key}}`
2. Add your API details. You can read more about setting up API actions from our [API configuration reference](https://developer.moveworks.com/creator-studio/api-configuration/).
    
    ```python
    curl --location '{{base_url}}/api/creator_studio_hello_world?name=Han&code=*****' \
    --data ''
    ```
    
    - Path: `/api/creator_studio_hello_world`
    - Method: `GET`
    - Query parameters:
        
        
        | Key | Value |
        | --- | --- |
        | name | {{query}} |
    - Example Value: `Han` (as in Han Solo)
3. Hit test & celebrate!
    
    ```bash
    {
        "results": [
            {
                "type": "Starship",
                "full-id": "Starship-10",
                "name": "Millennium Falcon",
                "model": "YT-1300 light freighter",
                "cost": "100000"
            },
            {
                "type": "Starship",
                "full-id": "Starship-22",
                "name": "Imperial shuttle",
                "model": "Lambda-class T-4a shuttle",
                "cost": "240000"
            }
        ]
    }
    ```
    

# Congratulations!

You just connected your first Azure Function App to Creator Studio. [Check out this guide]() to configure Azure Multi-Factor Authentication (MFA) Reset in Creator Studio.
---
name: SAP Concur   # The name of the guide
description: Connect Creator Studio to SAP Concur   # Brief description of the guide
time_in_minutes: 20   # Time in minutes to complete the guide
difficulty_level: Beginner  # Difficulty level: "Beginner", "Intermediate", or "Advanced"
---


# **Introduction**

SAP Concur is a leading provider of integrated travel, expense, and invoice management solutions. This guide will demonstrate how to create an **OAuth Client** in SAP Concur, authenticate with SAP Concur’s API, and test it in Creator Studio.

# **Prerequisites**

- Access to Authentication Admin in Concur
- [Install Postman](https://www.postman.com/downloads/)

# Walkthrough

You will be authenticating your Concur system with Creator Studio via the **Company Request Token Method**. This lets us generate a 1-time Company Request Token (valid for 24 hours) followed by refreshable access tokens which we’ll use to authenticate any interactions.

> **Refresh token expiration**
> 
> 
> For security reasons, Concur’s Refresh Tokens expire every 6 months & you will have to update the Refresh Token in the Connector every 6 months. You will have to generate a new Company Request Token and then use that Token to generate another valid Refresh token for the next 6 months.
> 

## **Step 1: Create a new OAuth 2.0 App with the required scopes**

1. Navigate to OAuth 2.0 Application Management under Authentication Admin
    
    ![https://files.readme.io/1ff0321-Untitled_-_2023-08-22T143932.802.png](https://files.readme.io/1ff0321-Untitled_-_2023-08-22T143932.802.png)
    
2. Client Create New App
    
    ![https://files.readme.io/8a9530b-Untitled_-_2023-08-22T143934.898.png](https://files.readme.io/8a9530b-Untitled_-_2023-08-22T143934.898.png)
    
3. Fill in the following details:
    1. App Name: `Moveworks Integration Application`
    2. App Type: `Client`
    3. App Description: `Moveworks' Creator Studio uses this application to authenticate API calls to your Concur instance`
    4. Allowed Grants: `refresh_token`, `password`, & `client_credentials`
    5. Allowed Scopes: `openid`, `EXPRPT`, `expense.report.read`, etc (Based on your requirement for the use case you are trying to build)
4. ❗Note down the generated `Client ID` & `Client Secret`
    
    ![https://files.readme.io/9e7b982-Untitled_-_2023-08-22T144019.235.png](https://files.readme.io/9e7b982-Untitled_-_2023-08-22T144019.235.png)
    

## **Step 2: Create a Company Request Token (to authenticate into our application created above)**

1. Navigate to Company Request Token under Authentication Admin
    
    ![https://files.readme.io/c2bf9be-Untitled_-_2023-08-22T144132.535.png](https://files.readme.io/c2bf9be-Untitled_-_2023-08-22T144132.535.png)
    
2. Now Paste the `Client ID` into the `App ID` & hit submit.
    
    ![https://files.readme.io/a29a529-Untitled_-_2023-08-22T144220.741.png](https://files.readme.io/a29a529-Untitled_-_2023-08-22T144220.741.png)
    
3. ❗Note down the Company UUID & Company Request Token
    
    ![https://files.readme.io/1528a01-Untitled_-_2023-08-22T144234.692.png](https://files.readme.io/1528a01-Untitled_-_2023-08-22T144234.692.png)
    

## **Step 3: Generate the refresh token using Postman (or similar tools)**

1. Set up your request in Postman with your `Client Credentials` and `Password` grant to generate the Refresh token
    
    ```bash
    curl --location 'https://us2.api.concursolutions.com/oauth2/v0/token' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'grant_type=password' \
    --data-urlencode 'client_id={{concur_client_id}}' \
    --data-urlencode 'client_secret={{concur_client_secret}}' \
    --data-urlencode 'username={{concur_uuid}}' \
    --data-urlencode 'password={{concur_request_token}}' \
    --data-urlencode 'credtype=authtoken'
    ```
    
    ![Untitled](Authentication%20Tutorial%20SAP%20Concur%20e3dd2cd5964a448fa351c31b5d30c23d/Untitled.png)
    
2. Replace the values within `{{_}}` with the actual values you obtained from Step 1 and 2 and execute the API. You should get a successful response with the following information:
    
    ```json
    {
      "expires_in": "3600",
      "scope": "{{space separated app-scopes}}",
      "token_type": "Bearer",
      "access_token": "{{access_token}}",
      "refresh_token": "{{refresh_token}}",
      "id_token": "{{oidc_token}}",
      "geolocation": "https://us2.api.concursolutions.com"
    }
    ```
    
3. Use the `refresh_token` you obtained from the previous step to hit the same API endpoint but now with a different grant as follows:
    
    ```bash
    curl --location 'https://us2.api.concursolutions.com/oauth2/v0/token' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'grant_type=refresh_token' \
    --data-urlencode 'client_id={{concur_client_id}}' \
    --data-urlencode 'client_secret={{concur_client_secret}}' \
    --data-urlencode 'refresh_token={{concur_refresh_token}}'
    ```
    
4. Replace the values and execute this API. You would see the same response as previous but now we will use the `access_token` we got from this API to authenticate our API calls

## **Step 4: Integrate with Creator Studio**

1. In Creator Studio, create a new connector with the following configuration (please name it accordingly to identify while creating use cases):
    - Description: `Connect to Concur APIs`
    - Base URL: `https://us2.api.concursolutions.com`
    - Auth Config: `Oauth2`
    - Oauth2 Grant Type: `Refresh Token Grant`
    - Client ID: `{{concur_client_id}}`
    - Client Secret: `{{concur_client_secret}}`
    - Refresh Token Grant Refresh Token: `{{concur_refresh_token}}`
    - Oauth2 Token Url: `https://us2.api.concursolutions.com/oauth2/v0/token`
    
    Click on `Save` to submit the credentials and your connector will be ready.
    
2. Define your API action for looking up expense reports
    
    ```bash
    curl --location 'https://us2.api.concursolutions.com/api/v3.0/expense/reports?user=ALL&limit=1' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer {{concur_access_token}}'
    ```
    
    - Path: `/api/v3.0/expense/reports`
    - Method: `GET`
    - Headers:
        
        
        | Key | Value |
        | --- | --- |
        | Accept | application/json |
    - Query parameters:
        
        
        | Key | Value |
        | --- | --- |
        | user | ALL |
        | limit | 1 |
3. Test your setup in Creator Studio and look for a successful execution (Response code: 200)
    
    ![Untitled](Authentication%20Tutorial%20SAP%20Concur%20e3dd2cd5964a448fa351c31b5d30c23d/Untitled%201.png)
    

# **Congratulations!**

You've successfully integrated Concur’s API with Creator Studio. This opens up a variety of automation and integration possibilities within your Concur instance.
---
name: Coupa   # The name of the guide
description: Connect Creator Studio to Coupa   # Brief description of the guide
time_in_minutes: 15   # Time in minutes to complete the guide
difficulty_level: Beginner  # Difficulty level: "Beginner", "Intermediate", or "Advanced"
---

# **Introduction**

Coupa is a cloud-based platform that streamlines business spend management. It offers robust tools for procurement, invoicing, and expense management. This guide will demonstrate how to create an **OAuth Client** in Coupa, authenticate with Coupa’s API, and test it in Creator Studio.

# **Prerequisites**

- Access to the Setup module in a Coupa instance
- [Install Postman](https://www.postman.com/downloads/)

# Walkthrough

## **Step 1:** OAuth Client creation and scope assignment

1. Navigate to **Setup > Oauth2/OpenID Connect Clients** (/oauth2/clients).
    
    ![Untitled](Authentication%20Guide%20Coupa%208c3fd8aaf16e483d91739f56b817cad0/Untitled.png)
    
2. Click **Create** and select **Client Credentials** in the **Grant type** dropdown.
3. Complete the fields and select the scopes (access permissions) the Client needs.
    - **Name:** Moveworks Client
    - **Login Details** → The details of the account you are using to create the client
    - **Scopes** → Select the scopes based on the requirement of your use case. For example, if you want to build a use case that requires fetching expense reports, scroll down and select the **`core.expense.read`** scope.
    
    ![https://compass.coupa.com/Import/Integrate/Technical_Documentation/API/OAuth_Transition/01_Transition_Guide/create_client.jpg](https://compass.coupa.com/Import/Integrate/Technical_Documentation/API/OAuth_Transition/01_Transition_Guide/create_client.jpg)
    
4. Once you save the Client, you will get the Client credentials: **Identifier**, **Secret**, **Oidc Scopes**.
Copy all three of them and store in a secure place. We will need these later to generate the OAuth Token.
    
    ![https://compass.coupa.com/Import/Integrate/Technical_Documentation/API/OAuth_Transition/01_Transition_Guide/oath_client_info.jpg](https://compass.coupa.com/Import/Integrate/Technical_Documentation/API/OAuth_Transition/01_Transition_Guide/oath_client_info.jpg)
    

## **Step 2: Test with Postman**

1. Set up your request in Postman with your `Client Credentials`.
    
    ```bash
    curl --location 'https://{{INSTANCE_DOMAIN}}/oauth2/token' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'grant_type=client_credentials' \
    --data-urlencode 'client_id={{Identifier}}' \
    --data-urlencode 'client_secret={{Secret}}' \
    --data-urlencode 'scope={{SPACE_SEPARATED_LIST_OF_SCOPES}}'
    ```
    
2. Import this request into Postman and execute it. You should get a successful response of your user information.
    
    ![Untitled](Authentication%20Guide%20Coupa%208c3fd8aaf16e483d91739f56b817cad0/Untitled%201.png)
    

## **Step 3: Integrate with Creator Studio**

1. In Creator Studio, create a new connector with the following configuration:
    - **Connection Name:** Coupa Connector
    - Base URL: `https://{{INSTANCE_DOMAIN}}` (For example: `https://moveworks-usa-coupalink-demo.coupacloud.com`)
    - Auth Config: `Oauth2`
    - Oauth2 Grant Type: `Client Credentials Grant`
    - Client ID: `{{Identifier}}`
    - Client Secret: `{{Secret}}`
    - Client Credentials Grant Scope: `{{SPACE_SEPARATED_LIST_OF_SCOPES}}`
    - Oauth2 Token Url: `https://{{INSTANCE_DOMAIN}}/oauth2/token`
    Click on `Save` to submit the credentials and your connector will be ready.
2. Add your API details. You can read more about setting up API actions from our [API configuration reference](https://developer.moveworks.com/creator-studio/integrations/outbound/api-configuration/).
    
    ```bash
    curl --location 'https://{{INSTANCE_DOMAIN}}/api/expense_reports' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer {{generated_bearer_token}}'
    ```
    
    - API endpoint Path: `/api/expense_reports`
    - Method: `GET`
    - Headers:
        
        
        | Key | Value |
        | --- | --- |
        | Accept | application/json |
    - Query parameters:
        
        
        | Key | Value |
        | --- | --- |
        | limit | 1 |
3. Test your setup in Creator Studio and look for a successful execution.
    
    ![Untitled](Authentication%20Guide%20Coupa%208c3fd8aaf16e483d91739f56b817cad0/Untitled%202.png)
    

# **Congratulations!**

You've successfully integrated Coupa’s API with Creator Studio. This opens up a variety of automation and integration possibilities within your Coupa instance.
---
name: GitHub   # The name of the guide
description: Connect Creator Studio to GitHub   # Brief description of the guide
time_in_minutes: 10   # Time in minutes to complete the guide
difficulty_level: Beginner  # Difficulty level: "Beginner", "Intermediate", or "Advanced"
---

# **Introduction**

GitHub provides a powerful API that allows developers to interact with GitHub services programmatically. To safeguard access and ensure that only authorized users can perform actions via the API, GitHub employs authentication mechanisms, including Personal Access Tokens (PATs). This guide will explain how to create and use a Personal Access Token for GitHub's APIs and connect it to Creator Studio.

# **Prerequisites**

- A GitHub account. If you do not have one, sign up at **[GitHub](https://github.com/join)**.
- [Install Postman](https://www.postman.com/downloads/)

# Walkthrough

## **Step 1: Create a Personal Access Token**

1. **Log in** to your GitHub account.
2. Navigate to **Settings** > **Developer settings** > **Personal access tokens > Tokens (classic)** ([https://github.com/settings/tokens](https://github.com/settings/tokens))
    
    ![Untitled](Authentication%20Tutorial%20GitHub%2089effaebc900474193ba55ebb85340d6/Untitled.png)
    
3. Click on **Generate new token > Generate new token (classic)**
    
    ![Untitled](Authentication%20Tutorial%20GitHub%2089effaebc900474193ba55ebb85340d6/Untitled%201.png)
    
4. Set the Note, Expiration and the Scopes based on your use case and click on **Generate Token**. By default, grant `repo:status` and `public_repo` scopes.
    
    ![Untitled](Authentication%20Tutorial%20GitHub%2089effaebc900474193ba55ebb85340d6/Untitled%202.png)
    
5. If your organization is protected by SAML enforcement you must grant your Personal Access token access to this organization. Click on **Configure SSO** and Authorize the organizations that you want to access through the token.
    
    ![Untitled](Authentication%20Tutorial%20GitHub%2089effaebc900474193ba55ebb85340d6/Untitled%203.png)
    
6. You will receive a confirmation like the following once its configured:
    
    ![Untitled](Authentication%20Tutorial%20GitHub%2089effaebc900474193ba55ebb85340d6/Untitled%204.png)
    

> Note: Using this token, you will be able to access information from your GitHub Account as well as the Organizations you have authorized the token to access.
> 

## **Step 2: Test with Postman**

We will be testing out the [List all Public Repositories of a User](https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-organization-repositories) API

1. Set up your request in Postman with your `Personal access token`.
    
    ```bash
    curl --location 'https://api.github.com/users/{{github_username}}/repos' \
    --header 'Authorization: Bearer {{github_classic_token}}'
    ```
    
    Set up the following:
    
    - `github_username`: The username of your GitHub account
2. Import this request into Postman and execute it. You should get a successful response of your repositories’ information.
    
    ![Postman-response](Authentication%20Tutorial%20GitHub%2089effaebc900474193ba55ebb85340d6/Untitled%205.png)
    

## **Step 3: Integrate with Creator Studio**

1. In Creator Studio, create a new connector with the following configuration:
    - Base URL: `https://api.github.com`
    - Auth Config: `Api Key Auth`
    - Api Key Auth Auth Type: `Header Auth`
    - Header Auth Key: `Authorization`
    - Header Auth Value Pattern: `Bearer %s`
    - Api Key: `{{github_classic_token}}`
2. Define your API action for channel creation.
    
    ```bash
    curl --location 'https://api.github.com/users/{{github_username}}/repos' \
    --header 'Authorization: Bearer {{github_classic_token}}'
    ```
    
    - Path: `/users/{{github_username}}/repos`
    - Method: `GET`
3. Test your setup in Creator Studio and look for a successful execution.
    
    ![CreatorStudio-test](Authentication%20Tutorial%20GitHub%2089effaebc900474193ba55ebb85340d6/Untitled%206.png)
    

# **Congratulations!**

You've successfully integrated GitHub’s API with Creator Studio. This opens up a variety of automation and integration possibilities within your GitHub organization.
---
name: Jira
description: Connect Creator Studio to Jira
time_in_minutes: 15
difficulty_level: Beginner
---

# Introduction

This authentication guide has not yet been written, but we've published use case guides that connect with Jira. You can learn from those in the interim.
---
name: Microsoft Graph
description: Connect Creator Studio to Microsoft Graph
time_in_minutes: 30
difficulty_level: Intermediate
---

# Introduction

The Microsoft Graph API allows you to access all your Microsoft data through one unified API. 

In this guide, we will demonstrate how to authenticate with the Microsoft Graph API from Creator Studio. We will walk through identifying permissions needed, creating a Microsoft Graph API key with those permissions, testing an endpoint in Postman, and connecting it to Creator Studio.

# Prerequisites

- Admin Access to Microsoft Tenant ([Get an Instant Sandbox](https://developer.microsoft.com/en-US/microsoft-365/dev-program))
- [Postman](https://www.postman.com/downloads/) or your API tester of choice

# Steps

## Step 1: Identify Permissions Needed

1. Open the [Graph API Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)
2. Find the APIs you want to use. 
3. Click on the `Modify permissions` tab. There, you’ll see the permissions you need to create an API key for.
    
    ![Untitled](Authentication%20Guide%20Microsoft%20Graph%20API%20822c8b4935bd47a6b7b5c633bd75a3a6/Untitled.png)
    

## Step 2: Get an API Key

### Grant Permissions

1. Open [App Registrations in the Azure Portal](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)
2. Register a `Creator Studio` app, or select an existing one.
    
    ![Untitled](Authentication%20Guide%20Microsoft%20Graph%20API%20822c8b4935bd47a6b7b5c633bd75a3a6/Untitled%201.png)
    
3. Under `API permissions`, click `Add a permission`, then add the permissions you identified in the previous step.
    
    ![Untitled](Authentication%20Guide%20Microsoft%20Graph%20API%20822c8b4935bd47a6b7b5c633bd75a3a6/Untitled%202.png)
    
4. Click `Grant admin consent for {Tenant}`. This formally assigns the entitlements to your API key.
    
    ![Untitled](Authentication%20Guide%20Microsoft%20Graph%20API%20822c8b4935bd47a6b7b5c633bd75a3a6/Untitled%203.png)
    

### Create Key

1. Create a client secret and jot it down.
    
    ![Untitled](Authentication%20Guide%20Microsoft%20Graph%20API%20822c8b4935bd47a6b7b5c633bd75a3a6/Untitled%204.png)
    
2. Note the app & tenant IDs from your App Overview
    
    ![Untitled](Authentication%20Guide%20Microsoft%20Graph%20API%20822c8b4935bd47a6b7b5c633bd75a3a6/Untitled%205.png)
    

## Step 3: Test in Postman

1. Craft your cURL import, replace the values as needed
    
    ```bash
    curl --location 'https://login.microsoftonline.com/{{tenant_id}}/oauth2/token' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'client_id={{application_id}}' \
    --data-urlencode 'client_secret={{client_secret}}' \
    --data-urlencode 'resource=https://graph.microsoft.com' \
    --data-urlencode 'grant_type=client_credentials'
    ```
    
2. Import to Postman (using `Import`)
    
    ![Untitled](Authentication%20Guide%20Microsoft%20Graph%20API%20822c8b4935bd47a6b7b5c633bd75a3a6/Untitled%206.png)
    
    ![Untitled](Authentication%20Guide%20Microsoft%20Graph%20API%20822c8b4935bd47a6b7b5c633bd75a3a6/Untitled%207.png)
    
3. Execute the API call and get an `access_token`. You’ll use this to authenticate the actual actions you want to take.
    
    ![Untitled](Authentication%20Guide%20Microsoft%20Graph%20API%20822c8b4935bd47a6b7b5c633bd75a3a6/Untitled%208.png)
    
4. Use the API endpoint from the graph explorer in Postman. Make sure you pass your new access token as a “Bearer Token” to the Graph API.
    
    ![Untitled](Authentication%20Guide%20Microsoft%20Graph%20API%20822c8b4935bd47a6b7b5c633bd75a3a6/Untitled%209.png)
    

## Step 4: Connect to Creator Studio

1. In your API editor, create a new connector. You can read more about the supported auth types on [our connector reference](https://developer.moveworks.com/creator-studio/connector-configuration/).
    - Base Url: `https://graph.microsoft.com`
    - Auth Config: `Oauth`
    - OAuth Grant Type: `Client Credentials Grant`
    - Client ID: `{{application_id}}`
    - Client Secret: `{{client_secret}}`
    - OAuth Token Url: `https://login.microsoftonline.com/{{tenant_id}}/oauth2/token`
    - OAuth2 Client Authorization: `OAuth 2.0 with Request Body`
    - OAuth2 Custom Oauth Response Response Type: `Json`
    - Json Expires In Key: `expires_in`
    - Json Access Token Key: `access_token`
    - Json Expires In Format: `CUSTOM_OAUTH2_EXPIRES_IN_FORMAT_SECONDS`
    - Oauth2 Custom Oauth Request Options Additional Request Data:
        
        
        | Key | Value |
        | --- | --- |
        | resource | https://graph.microsoft.com |
2. Add your API details. You can read more about setting up API actions from our [API configuration reference](https://developer.moveworks.com/creator-studio/api-configuration/).
    
    ```python
    curl --location 'https://graph.microsoft.com/v1.0/users/{{user.primary_email_address}}/authentication/phoneMethods' \
    --data ''
    ```
    
3. Hit test & celebrate!
    
    ```bash
    {
        "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users('amerchia%406x2pb8.onmicrosoft.com')/authentication/phoneMethods",
        "value": [
            {
                "id": "e37fc753-ff3b-4958-9484-eaa9425c82bc",
                "phoneNumber": "+1 2065555555",
                "phoneType": "office",
                "smsSignInState": "notSupported"
            },
            {
                "id": "3179e48a-750b-4051-897c-87b9720928f7",
                "phoneNumber": "+1 2065555555",
                "phoneType": "mobile",
                "smsSignInState": "notAllowedByPolicy"
            }
        ]
    }
    ```
    

# Congratulations!

You just connected your Microsoft Graph API to Creator Studio.
---
name: Nexthink   # The name of the guide
description: Connect Creator Studio to Nexthink   # Brief description of the guide
time_in_minutes: 15   # Time in minutes to complete the guide
difficulty_level: Beginner  # Difficulty level: "Beginner", "Intermediate", or "Advanced"
---

# **Introduction**

Accessing features using the Nexthink APIs gives you the flexibility to create integrations from external third-party tools. Using APIs helps remove complexity, as IT teams do not have to access multiple consoles to carry out their work. This guide will demonstrate how to create API credentials, authenticate with Nexthink’s API, and test it in Creator Studio.

# **Prerequisites**

- Access to a Nexthink workspace
- [Install Postman](https://www.postman.com/downloads/)

# Walkthrough

To set up an integration with a Nexthink API, you must first create a set of API credentials for your instance that Creator Studio will use to access the API and send requests.

## **Step 1: Create API Credentials**

1. Log in to the Nexthink web interface.
2. Select **Administration** from the main menu.
3. Click on **API credentials** in the navigation panel from the Account Management section.
    
    ![Untitled](Authentication%20Tutorial%20Nexthink%20f0799a5634704e0587dead9284041f00/Untitled.png)
    
4. Click on the **New OAuth client credentials** button located in the top-right of the API credentials page.
    
    ![Untitled](Authentication%20Tutorial%20Nexthink%20f0799a5634704e0587dead9284041f00/Untitled%201.png)
    
5. Fill up the details based on the below instructions:
    - **Name**: provide a meaningful name for the credential. Nexthink recommends using the name of the application you are configuring to call the API.
    - **Description**: enter a description to inform users what applications and services use the credentials and why.
    - **Permissions**: select the features you want to enable the permissions for. Some permissions are related to features that may not be available to you, for example, features in technical preview or those not included in your license. For most starting Creator Studio use cases, enable the permissions check for the "Remote Actions API".
        - **Remote Actions API** Select the checkbox to send API calls to trigger and query remote actions.
        - **Enrichment API** Select the checkbox to send API calls to operate the enrichment feature.
        - **Campaigns API** Select the checkbox to send API calls to trigger campaigns.
        - **Workflows API** Select the checkbox to send API calls to trigger and query workflows.
        - **NQL API** Select the checkbox to send API calls to extract data from your Nexthink platform.
    - Click on **Save and generate credentials** to generate the credentials. A new modal appears with the OAuth client credentials.
        
        ![Untitled](Authentication%20Tutorial%20Nexthink%20f0799a5634704e0587dead9284041f00/Untitled%202.png)
        

1. For security reasons, the credentials appear only once. Copy and save them securely, as you cannot access them beyond this point.
    
    ![Untitled](Authentication%20Tutorial%20Nexthink%20f0799a5634704e0587dead9284041f00/Untitled%203.png)
    

## **Step 2: Test with Postman**

1. Set up your request in Postman with your `API Credentials`.
    
    ```bash
    curl --location --request POST 'https://{{nexthink_instance}}.api.{{region}}.nexthink.cloud/api/v1/token' 
    		 --header 'Authorization: Basic <Base64 encoded {{nexthink_clientId}}:{{nexthink_clientSecret}}>'
    ```
    
2. Import this request into Postman and execute it. You should get a successful response of generating an access token.
    
    ![Untitled](Authentication%20Tutorial%20Nexthink%20f0799a5634704e0587dead9284041f00/Untitled%204.png)
    
3. Try using this generated `access_token` to execute the following API to check if it has the correct access.
    
    ```bash
    curl --request GET 'https://{{nexthink_instance}}.api.{{region}}.nexthink.cloud/api/v1/workflows' \
      --header 'Accept: application/json' \
      --header 'Authorization: Bearer {{access_token}}'
    ```
    
    ![Untitled](Authentication%20Tutorial%20Nexthink%20f0799a5634704e0587dead9284041f00/Untitled%205.png)
    

## **Step 3: Integrate with Creator Studio**

1. In Creator Studio, create a new connector with the following configuration:
    - Base URL: `https://{{nexthink_instance}}.api.{{region}}.nexthink.cloud`
    - Auth Config: `Oauth2`
    - Oauth2 Grant Type: `Client Credentials Grant`
    - Client ID: `{{nexthink_clientId}}`
    - Client Secret: `{{nexthink_clientSecret}}`
    - Oauth2 Token Url: `https://{{nexthink_instance}}.api.{{region}}.nexthink.cloud/api/v1/token`
    - Oauth2 Client Authentication: `OAuth 2.0 with Basic Auth Header set to username and password`
2. Define your API action for listing workflows.
    
    ```bash
    curl --request GET 'https://{{nexthink_instance}}.api.{{region}}.nexthink.cloud/api/v1/workflows' \
      --header 'Accept: application/json' \
      --header 'Authorization: Bearer {{access_token}}'
    ```
    
    - Path: `/api/v1/workflows`
    - Method: `GET`
3. Test your setup in Creator Studio and look for a successful execution.
    
    ```bash
    
    [
    	{
    		"id": "license_reclamation",
    		"lastUpdateTime": "2023-12-07T16:26:36Z",
    		"name": "License reclamation",
    		"status": "ACTIVE",
    		.....
    	}
    ]
    ```
    

# **Congratulations!**

You've successfully integrated Nexthink’s API with Creator Studio. This opens up a variety of automation and integration possibilities within your Nexthink workspace.
---
name: OpenAI   # The name of the guide
description: Connect Creator Studio to OpenAI   # Brief description of the guide
time_in_minutes: 10   # Time in minutes to complete the guide
difficulty_level: Beginner  # Difficulty level: "Beginner", "Intermediate", or "Advanced"
---


# **Introduction**

OpenAI offers a comprehensive set of APIs that allow developers to integrate advanced AI capabilities into their applications. To maintain security and ensure only authorized access, OpenAI requires authentication for all API requests. This guide will walk you through the process of authenticating with OpenAI's APIs and test it in Creator Studio.

# **Prerequisites**

- An OpenAI account. If you do not have one, you can create an account at **[OpenAI](https://openai.com/)**.
- [Install Postman](https://www.postman.com/downloads/)

# Walkthrough

We will be following the [Authentication method](https://platform.openai.com/docs/api-reference/authentication) used by OpenAI to create an API Key and authenticate our API calls.

## **Step 1: Generate an API Key**

1. Go to the [OpenAI's Documentation](https://platform.openai.com/docs/overview) and login using the account you created.
2. Click on `API Keys` after hovering over the left navigation bar
    
    ![OpenAI API Home Page](Authentication%20Tutorial%20OpenAI%20c764b9c442a64a469cc4c80d60f54190/Untitled.png)
    
3. Click on `Create new secret key` 
    
    ![OpenAI API Keys Page](Authentication%20Tutorial%20OpenAI%20c764b9c442a64a469cc4c80d60f54190/Untitled%201.png)
    
4. Set the name of the Secret key and the permissions based on your requirement. Then click on `Create secret key` .
    
    ![Create New Secret Key](Authentication%20Tutorial%20OpenAI%20c764b9c442a64a469cc4c80d60f54190/Untitled%202.png)
    
5. Copy and save the secret key in a safe and accessible place.
    
    ![Save Secret Key](Authentication%20Tutorial%20OpenAI%20c764b9c442a64a469cc4c80d60f54190/Untitled%203.png)
    

## **Step 2: Test with Postman**

1. Set up your request in Postman with your `API Key`.
    
    ```bash
    curl https://api.openai.com/v1/models \
      -H "Authorization: Bearer $OPENAI_API_KEY"
    ```
    
2. Import this request into Postman and execute it. You should get a successful response of your user information.
    
    ![Postman Successful Response](Authentication%20Tutorial%20OpenAI%20c764b9c442a64a469cc4c80d60f54190/Untitled%204.png)
    

## **Step 3: Integrate with Creator Studio**

1. In Creator Studio, create a new connector with the following configuration:
    - Base URL: `https://api.openai.com`
    - Auth Config: `Api Key Auth`
    - Api Key Auth Auth Type: `Header Auth`
    - Header Auth Key: `Authorization`
    - Header Auth Value Pattern: `Bearer %s`
    - Api Key: `{{OPENAI_API_KEY}}`
2. Define your API action for fetching OpenAI models.
    
    ```bash
    curl https://api.openai.com/v1/models \
      -H "Authorization: Bearer $OPENAI_API_KEY"
    ```
    
    - Path: `/v1/models`
    - Method: `GET`
3. Test your setup in Creator Studio and look for a successful execution.
    
    ![Untitled](Authentication%20Tutorial%20OpenAI%20c764b9c442a64a469cc4c80d60f54190/Untitled%205.png)
    

# **Congratulations!**

You've successfully integrated OpenAI’s API with Creator Studio. This opens up a variety of AI automation and integration possibilities within your Moveworks bot.
---
name: Perplexity
description: Connect Creator Studio to Perplexity
time_in_minutes: 5
difficulty_level: Beginner
---

# **Introduction**

Perplexity’s API hosts LLMs that have access to information scraped from the web. This guide will demonstrate how to create a Perplexity API Key, authenticate with the Perplexity API, and test in Creator Studio

# **Prerequisites**

- A Perplexity Account (with API credits)

# Walkthrough

## **Step 1: Create a Personal Access Token**

1. Go to the [Perplexity API console](https://www.perplexity.ai/settings/api)
2. Click on `Generate` under `API Keys`
    
    ![Untitled](Authentication%20Guide%20Perplexity%20e925c5c4cdb443b28e7c28bb26e8245e/Untitled.png)
    
3. Copy the API Key & store it somewhere safe.
    
    ![Untitled](Authentication%20Guide%20Perplexity%20e925c5c4cdb443b28e7c28bb26e8245e/Untitled%201.png)
    

## **Step 2: Authenticate with Perplexity**

1. Go to [Perplexity’s API reference](https://docs.perplexity.ai/reference/post_chat_completions). 
2. Add your API Key to the Authorization window
    
    ![Untitled](Authentication%20Guide%20Perplexity%20e925c5c4cdb443b28e7c28bb26e8245e/Untitled%202.png)
    
3. Hit `Try It!`, you should get a content response.
    
    ![Untitled](Authentication%20Guide%20Perplexity%20e925c5c4cdb443b28e7c28bb26e8245e/Untitled%203.png)
    

## **Step 3: Integrate with Creator Studio**

1. In Creator Studio, create a new connector with the following configuration:
    - Base URL: `https://api.perplexity.ai`
    - Auth Config: `Api Key Auth`
    - Api Key Auth Auth Type: `Header Auth`
    - Header Auth Key: `Authorization`
    - Header Auth Value Pattern: `Bearer %s`
    - Api Key: `{{your_api_key}}`
2. Define your API action for chat completion.
    
    ```bash
    curl --request POST \
         --url https://api.perplexity.ai/chat/completions \
         --header 'accept: application/json' \
         --header 'content-type: application/json' \
         --data '
    {
      "model": "mistral-7b-instruct",
      "messages": [
        {
          "role": "system",
          "content": "Be precise and concise."
        },
        {
          "role": "user",
          "content": "How many stars are there in our galaxy?"
        }
      ]
    }
    '
    ```
    
    - Path: `/chat/completions`
    - Method: `POST`
    - Request Body:
        
        ```json
        {
          "model": "mistral-7b-instruct",
          "messages": [
            {
              "role": "system",
              "content": "Be precise and concise."
            },
            {
              "role": "user",
              "content": "How many stars are there in our galaxy?"
            }
          ]
        }
        ```
        
    - Headers:
        
        
        | Key | Value |
        | --- | --- |
        | accept | application/json |
        | content-type | application/json |
3. Test your setup in Creator Studio and look for a successful execution.
    
    ![Untitled](Authentication%20Guide%20Perplexity%20e925c5c4cdb443b28e7c28bb26e8245e/Untitled%204.png)
    

# **Congratulations!**

You've successfully integrated Perplexity’s API with Creator Studio. You can now access their LLMs from Creator Studio.
---
name: Salesforce   # The name of the guide
description: Connect Creator Studio to Salesforce   # Brief description of the guide
time_in_minutes: 60   # Time in minutes to complete the guide
difficulty_level: Intermediate  # Difficulty level: "Beginner", "Intermediate", or "Advanced"
---



# **Introduction**

**Salesforce** is a leader in cloud-based services, specializing in comprehensive customer relationship management (CRM) solutions, empowering businesses with data-driven decision-making.

This guide will step you through creating a connector within Creator Studio to make API calls to Salesforce's SOQL and sObjects APIs. This guide has been organized into three main sections:

1. Set up OAuth Password Grant Flow
2. Test with Postman
3. Create a Connector in Creator Studio

# **Prerequisites**

- Salesforce account with Admin privileges so we can create a new Connected App and manage User and Permissions
- [Install Postman](https://www.postman.com/downloads/) for testing the API connection

# **Set up Salesforce**

To connect to Salesforce from within Creator Studio, we are going to be using [OAuth2 with Username/Password](https://oauth.net/2/grant-types/password/). This requires the following:

- Consumer Key
- Consumer Secret
- Service Account Email
- Service Account Password
- Service Account Security Token

The following will walk you through how to set up a Connected App with a Service Account and necessary Permission Sets so we can set up the connector within Creator Studio.

## **Step 1:** Set up OAuth Password Grant Flow

1. **Create Connected App** in Salesforce

    ![https://files.readme.io/3170a09-small-Screen_Shot_2023-01-24_at_3.20.14_PM.png](https://files.readme.io/3170a09-small-Screen_Shot_2023-01-24_at_3.20.14_PM.png)

    1. Under **Setup > App Manager** and click `New Connected App`
    2. Fill basic info: {Connected App Name: `Moveworks_Server`, API Name: `Moveworks_Server`, Contact Email: [support@moveworks.ai](mailto:support@moveworks.ai)}
    3. Select *enable oAuth settings* under API (Enable oAuth Settings) & add {Callback URL: [https://login.salesforce.com/](https://login.salesforce.com/)}
    4. Add oAuth scopes to:
        1. api
        2. refresh_token, offline_access

            ![Untitled](Authentication%20Guide%20Salesforce%20d7869a374e2940dea9ad3ba1af20ab92/Untitled.png)

    5. Check the following:
        1. **Enable Authorization Code and Credentials Flow**
        2. **Require user credentials in the POST body for Authorization Code and Credentials Flow**

            ![Untitled](Authentication%20Guide%20Salesforce%20d7869a374e2940dea9ad3ba1af20ab92/Untitled%201.png)

    6. Click *`Save` > `Manage Consumer Details`(Under **API (Enable OAuth Settings)**)*
        1. Note down the `Consumer Key` and the `Consumer Secret`
    7. After saving, click *`Manage` > `Edit Policies`*
        1. In the *OAuth policies* section, change to *Permitted Users* to *Admin approved users are pre-authorized*
        2. In the Session policies section, change *Timeout Value* to *24 hours*
        3. Click *Save*
2. **Create a Permission Set** to interact with the Connected App

    ![https://files.readme.io/e110dc6-small-Screen_Shot_2023-01-24_at_3.28.08_PM.png](https://files.readme.io/e110dc6-small-Screen_Shot_2023-01-24_at_3.28.08_PM.png)

    1. Navigate to **Users > Permission Sets** and click on `New`
    2. Add `moveworks_connected_app` as the Label & Api Names & click Save
    3. Now click on the `moveworks_connected_app` Permission Set and click Assigned Connected Apps
    4. Click Edit and add `Moveworks_Server` to list of Enabled Connected Apps & click Save
3. Create **New Service Account** (if it doesn’t exist)

    ![https://files.readme.io/cf02e32-small-Screen_Shot_2023-01-24_at_3.29.33_PM_1.png](https://files.readme.io/cf02e32-small-Screen_Shot_2023-01-24_at_3.29.33_PM_1.png)

    1. Navigate to **Users > Users** and click on `New User`
    2. Enter the following information & click *Save*:
        1. Last Name: `Moveworks`
        2. Alias: `moveworks`
        3. Email, Username & Nickname: `moveworks@{{customer-domain}}.com`. Please also create and enable the Email on your Mailing system because you will receive emails for the 5th step mentioned below.
        4. Setup role as `Admin` (or any custom role that you have which allows access to view or modify certain objects)
        5. Setup profile as `Salesforce Admin` (or any custom profile that you have which allows access to view or modify certain objects)
4. **Assign our service user the connected app**
    1. Navigate to **Users > Users** & click on our service user account that was just created.
    2. Click on **Permission Set Assignment** and then **Edit Assignments**
    3. Now add `moveworks_connected_app` to list of **Enabled Permission Sets** & click **Save**
5. **Get the Username, Password and the Security Token for the Service User**
    1. Navigate to **Users > Users** & click on *Login* for service user account that was just created.
    2. After logging in as the service user account, click on *`View Profile` > `Settings`*
        1. Go to ***Change My Password*** and set up a new password for the account. Note down the password after saving it.
        2. Go to ***Reset My Security Token*** and click on `Reset Security Token` button. You will receive an email with the new security token. Note down the security token too.
        
            >Note: If you are unable to see the Reset Security Token option, follow [these steps](https://help.salesforce.com/s/articleView?id=000386179&type=1).

## **Step 2: Test with Postman**

Once you have all the required credentials from the above process, please move on to test the OAuth API and try to fetch the token.

1. [Salesforce OAuth Authentication API](https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_endpoints.htm&type=5): An API for Salesforce Connected Apps to request an OAuth token required to authenticate API calls

    ```bash
    curl --location 'https://login.salesforce.com/services/oauth2/token' \
     --header 'Accept: application/json' \
     --header 'Content-Type: application/x-www-form-urlencoded' \
     --data-urlencode 'grant_type=password' \
     --data-urlencode 'client_id={{salesforce_consumer_key}}’ \
     --data-urlencode 'client_secret={{salesforce_consumer_secret}}' \
     --data-urlencode 'username={{salesforce_username}}' \
     --data-urlencode 'password={{salesforce_password}}{{salesforce_security_token}}' \
     --data-urlencode 'redirect_uri=https://login.salesforce.com/'
    ```

    > The API URL used here is `https://login.salesforce.com` which signifies a Production instance of Salesforce. If you are using a Sandbox instance, please modify the `URL` to the following:
    `https://test.salesforce.com`
    >
2. Import this request into Postman, replace the credentials and execute it. You should get a successful response and a token.

    ![Untitled](Authentication%20Guide%20Salesforce%20d7869a374e2940dea9ad3ba1af20ab92/Untitled%202.png)

## **Step 3: Integrate with Creator Studio**

1. In Creator Studio, create a new connector with the following configuration (please name it accordingly to identify while creating use cases):
    - Description: `Connect to Salesforce SOQL APIs`
    - Base URL: `https://{your-salesforce-domain}.my.salesforce.com`
    - Auth Config: `Oauth2`
    - Oauth2 Grant Type: `Password Grant`
    - Client ID: `{{salesforce_consumer_key}}`
    - Client Secret: `{{salesforce_consumer_secret}}`
    - Password Grant Username: `{{salesforce_username}}`
    - Password Grant Password: `{{salesforce_password}}{{salesforce_security_token}}`
    - Oauth2 Token Url: `https://login.salesforce.com/services/oauth2/token` (Or, `https://test.salesforce.com/services/oauth2/token` if you’re configuring for a Sandbox instance)

    Click on `Save` to submit the credentials and your connector will be ready.

2. Add your API details. You can read more about setting up API actions from our [API configuration reference](https://developer.moveworks.com/creator-studio/integrations/outbound/api-configuration/).

    ```bash
    curl --location 'https://{{your-salesforce-instance}}.my.salesforce.com/services/data/v58.0/query?q=SELECT%20Name%20FROM%20Contact%20LIMIT%2010' \
    --header 'Authorization: Bearer {{generated_bearer_token}}'
    ```

    - API endpoint Path: `/services/data/v58.0/query`
    - Method: `GET`
    - Query Parameters

        | Key | Value |
        | --- | --- |
        | q | SELECT Name FROM Contact LIMIT 10 |
3. Test your setup in Creator Studio and look for a successful execution.

    ![Untitled](Authentication%20Guide%20Salesforce%20d7869a374e2940dea9ad3ba1af20ab92/Untitled%203.png)

# **Congratulations!**

You've successfully integrated Salesforce’s API with Creator Studio. This opens up a variety of automation and integration possibilities within your Salesforce instance.
---
name: Slack
description: Connect Creator Studio to Slack
time_in_minutes: 15
difficulty_level: Beginner
---

# **Introduction**

Slack's API provides a powerful way to automate tasks in your Slack workspace. This guide will show you how to create a Slack app, authenticate with Slack's API, and use it for channel creation in your workspace, all through Creator Studio.

# **Prerequisites**

- Admin access to a Slack workspace ([Create a Slack Workspace](https://slack.com/get-started#/create))
- [Install Postman](https://www.postman.com/downloads/)

# **Walkthrough**

## **Step 1: Set Up Your Slack App**

1. Go to [Your Apps](https://api.slack.com/apps) on Slack API's website.
2. Click on `Create New App` and choose `From scratch`.
3. Name your app (e.g., `Creator Studio Bot`) and select your Slack workspace.
    
    ![Untitled](Authentication%20Guide%20Slack%20API%203f2aff0ceb4041d697444d8585eb3357/Untitled.png)
    

## **Step 2: Obtain API Credentials**

### Identify Permissions

1. Go to [Slack API Methods](https://api.slack.com/methods) and find the APIs you want to execute. Each API endpoint specifies exactly what scopes you will need.

![Untitled](Authentication%20Guide%20Slack%20API%203f2aff0ceb4041d697444d8585eb3357/Untitled%201.png)

### **Add Permissions**

1. In your app settings, navigate to `OAuth & Permissions`.
2. Under `Bot Token Scopes`, add necessary permissions like `channels:manage` to create channels.
    
    ![Untitled](Authentication%20Guide%20Slack%20API%203f2aff0ceb4041d697444d8585eb3357/Untitled%202.png)
    

### **Install App to Workspace**

1. Click `Install App to Workspace`.

## **Step 3: Test with Postman**

1. Set up your request in Postman with your `Bot User OAuth Access Token`.
    
    ```bash
    curl -X POST 'https://slack.com/api/conversations.create' \
    --header 'Authorization: Bearer {{xoxb_your_bot_access_token}}' \
    --data-urlencode 'name=test-channel'
    ```
    
2. Import this request into Postman and execute it.
    
    ![Untitled](Authentication%20Guide%20Slack%20API%203f2aff0ceb4041d697444d8585eb3357/Untitled%203.png)
    
3. Check for a successful response with details of the newly created channel.
    
    ![Untitled](Authentication%20Guide%20Slack%20API%203f2aff0ceb4041d697444d8585eb3357/Untitled%204.png)
    

## **Step 4: Integrate with Creator Studio**

1. In Creator Studio, create a new connector with the following configuration:
    - Base URL: `https://slack.com/api`
    - Auth Config: `Api Key Auth`
    - Api Key Auth Auth Type: `Header Auth`
    - Header Auth Key: `Authorization`
    - Header Auth Value Pattern: `Bearer %s`
    - Api Key: `{{xoxb_your_bot_access_token}}`
2. Define your API action for channel creation.
    
    ```bash
    curl -X POST '{{base_url}}/conversations.create' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'name={{channel-name}}'
    ```
    
    - Path: `/conversations.create`
    - Method: `POST`
    - Headers
        
        
        | Key | Value |
        | --- | --- |
        | Content-Type | application/x-www-form-urlencoded |
    - Body:
        
        ```text
        name=channel-name
        ```
        
    
3. Test your setup in Creator Studio and look for a successful execution.
    
    ```json
    
    {
        "ok": true,
        "channel": {
            "id": "C1234567890",
            "name": "channel-name",
            "is_channel": true,
            ...
        }
    }
    ```
    

# **Congratulations!**

You've successfully integrated Slack's API with Creator Studio. This opens up a variety of automation and integration possibilities within your Slack workspace.
---
name: Snowflake   # The name of the guide
description: Connect Creator Studio to Snowflake   # Brief description of the guide
time_in_minutes: 60   # Time in minutes to complete the guide
difficulty_level: Advanced  # Difficulty level: "Beginner", "Intermediate", or "Advanced"
---

# **Introduction**

Connecting Snowflake to Creator Studio allows for robust data management, analysis, and integration capabilities by leveraging Snowflake's powerful cloud data platform within Creator Studio's automation and workflow environment. This guide will walk you through the process of using OAuth for secure authentication, detailing how to configure OAuth clients in Snowflake, obtain necessary credentials, and establish a secure connection within Creator Studio. By following these steps, you'll enable seamless data workflows that optimize your data-driven projects with efficiency and security.

# **Prerequisites**

- ACCOUNTADMIN access to your Snowflake instance to create OAuth clients and roles
- [Install Postman](https://www.postman.com/downloads/)

# Walkthrough

Snowflake enables OAuth for clients through integrations. An integration is a Snowflake object that provides an interface between Snowflake and third-party services. Administrators configure OAuth using a [Security integration](https://docs.snowflake.com/en/user-guide/admin-security-fed-auth-security-integration), which enables clients that support OAuth to redirect users to an authorization page and generate access tokens (and optionally, refresh tokens) for accessing Snowflake.

Snowflake supports the [OAuth 2.0](https://oauth.net/2/) protocol for authentication and authorization using one of the options below:

- [Snowflake OAuth](https://docs.snowflake.com/en/user-guide/oauth-snowflake-overview)
- [External OAuth](https://docs.snowflake.com/en/user-guide/oauth-ext-overview)

For this tutorial, we are going to use the [Custom client integration](https://docs.snowflake.com/en/user-guide/oauth-custom) under the Snowflake OAuth to connect Creator Studio to your Snowflake instance.

## **Step 1: Preparing Snowflake for OAuth**

> 💡 Hitting `cmd + enter` while highlighting a given block in Snowflake ensures you only attempt to execute the highlighted block.


1. Create a Custom Client Integration in Snowflake
    1. Navigate to the Snowflake Web Interface, switch to the **`Worksheets`** tab and create a new SQL Worksheet to run the following SQL statement for creating an OAuth Security Integration using the [CREATE SECURITY INTEGRATION](https://docs.snowflake.com/en/sql-reference/sql/create-security-integration-oauth-snowflake) command:
        
        ```sql
        CREATE or REPLACE SECURITY INTEGRATION oauth_moveworks_connector
          TYPE = OAUTH
          ENABLED = TRUE
          OAUTH_CLIENT = CUSTOM
          OAUTH_CLIENT_TYPE = 'CONFIDENTIAL'
          OAUTH_REDIRECT_URI = 'https://moveworks.com'
          OAUTH_ISSUE_REFRESH_TOKENS = TRUE
          OAUTH_REFRESH_TOKEN_VALIDITY = 86400;
        ```
        
        > **Note: Only account administrators (users with the ACCOUNTADMIN role) or a role with the global CREATE INTEGRATION privilege can execute this SQL command.**
        > 
    2. You will see the following confirmation if everything is correctly set up:
        
        ![Untitled](Authentication%20Tutorial%20Snowflake%2080f48383283545edaa968ced07eacca3/Untitled.png)
        
2. Retrieve the OAuth details for client configuration
    1. Describe the above Security Integration and note down the below details, they will be used in the following steps:
        - `OAUTH_CLIENT_ID`
        - `OAUTH_REDIRECT_URI`
        - `OAUTH_AUTHORIZATION_ENDPOINT`
        - `OAUTH_TOKEN_ENDPOINT`
        
        ```sql
        DESCRIBE SECURITY INTEGRATION oauth_moveworks_connector;
        ```
        
    2. Note down the Client Secret by running the below command:
        
        ```sql
        SELECT SYSTEM$SHOW_OAUTH_CLIENT_SECRETS('OAUTH_MOVEWORKS_CONNECTOR');
        ```
        
        > Note: You will get 2 secrets, note down either one.
        > 
3. Request an Auth Code Grant
    1. To request an Auth Code Grant, the client needs to hit the Authorization Endpoint by providing the required query parameters
    2. All the query parameters must be URL Encoded, an online tool like [urlencoder.io](https://www.urlencoder.io/) can be used for that purpose (this is not a recommendation, you can use any method to correctly encode the URL). Encode the below parameters that you gathered from the previous step
        1. `OAUTH_CLIENT_ID`
        2. `OAUTH_REDIRECT_URI`
    3. Prepare the Authorization URL in the below format
        
        ```bash
        <OAUTH_AUTHORIZATION_ENDPOINT>?response_type=code&client_id=<encoded value of OAUTH_CLIENT_ID>&redirect_uri=<encoded value of OAUTH_REDIRECT_URI>
        ```
        
    4. Go to your browser and hit the above Authorization URL. This URL will take you to the Login Window of your Snowflake account, a user must log in and the default role of the user must not be `ACCOUNTADMIN`, `SECURITYADMIN`, or `ORGADMIN`
    5. After successful authentication, the below message will appear for Consent. Please read it carefully to understand the operation that is being performed.
        
        ![Untitled](Authentication%20Tutorial%20Snowflake%2080f48383283545edaa968ced07eacca3/Untitled%201.png)
        
    6. After allowing the above consent, the Authorization URL would be redirected to the `OAUTH_REDIRECT_URI` location and you will be able to see the Auth Code Grant in the following format. Please note it may take some time:
    `https://www.moveworks.com/?code=<.......81BB573502BB8C.....>`
    7. The code value is the **Auth Code Grant**, please note it down as it will be used in the next step to request an Access Token.

## **Step 2: Request Access Token and Refresh Token using Postman**

1. Now the client can request an Access Token by hitting the Token endpoint and providing the **Auth Code Grant** along with `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET`
    
    ```bash
    curl --location '{{OAUTH_TOKEN_ENDPOINT}}' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --header 'Authorization: Basic <Base64 encoded {{OAUTH_CLIENT_ID}}:{{OAUTH_CLIENT_SECRET}}>' \
    --data-urlencode 'grant_type=authorization_code' \
    --data-urlencode 'code={{Auth Code Grant}}' \
    --data-urlencode 'redirect_uri={{OAUTH_REDIRECT_URI}}'
    ```
    
2. Import this request into Postman and execute it. You should get a successful response of an `access_token` and a `refresh_token`.
    
    ![Untitled](Authentication%20Tutorial%20Snowflake%2080f48383283545edaa968ced07eacca3/Untitled%202.png)
    
    ![Untitled](Authentication%20Tutorial%20Snowflake%2080f48383283545edaa968ced07eacca3/Untitled%203.png)
    
    You will receive a response like the following:
    
    ```bash
    {
        "access_token": "ver:1-hint:8498279991--------------wGgCp++/eZK+",
        "refresh_token": "ver:2-hint:12967350277-di------------------------------IpYi//im1u+/N9Kd//+==",
        "token_type": "Bearer",
        "username": "<USERNAME>",
        "scope": "refresh_token session:role:PUBLIC",
        "refresh_token_expires_in": 86400,
        "idpInitiated": false,
        "expires_in": 600
    }
    ```
    
    This refresh_token will be your `OAUTH_REFRESH_TOKEN` for the next step.
    
3. Use the Refresh Token to create a new request to get the `access_token`.
    
    ```bash
    curl --location '{{OAUTH_TOKEN_ENDPOINT}}' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --header 'Authorization: Basic <Base64 encoded {{OAUTH_CLIENT_ID}}:{{OAUTH_CLIENT_SECRET}}>' \
    --data-urlencode 'grant_type=refresh_token' \
    --data-urlencode 'refresh_token={{OAUTH_REFRESH_TOKEN}}' \
    --data-urlencode 'redirect_uri={{OAUTH_REDIRECT_URI}}'
    ```
    
    ![Untitled](Authentication%20Tutorial%20Snowflake%2080f48383283545edaa968ced07eacca3/Untitled%204.png)
    
    You will receive a response like the following:
    
    ```bash
    {
        "access_token": "ver:2-hint:12967350277-di------------------------------IpYi//im1u+/N9Kd//+==",
        "token_type": "Bearer",
        "idpInitiated": false,
        "expires_in": 600
    }
    ```
    
    The `access_token` here is the one you can use to authenticate further API calls to your Snowflake instance.
    

## **Step 3: Integrate with Creator Studio**

1. In Creator Studio, create a new connector with the following configuration:
    - Base URL:
        - This will be your Snowflake account URL
        - For example, you might use the endpoints `https://myorg-account_xyz.snowflakecomputing.com/oauth/authorize` and `https://myorg-account_xyz.snowflakecomputing.com/oauth/token-request`
        - `https://myorg-account_xyz.snowflakecomputing.com` will be the Base URL here
    - Auth Config: `Oauth2`
    - Oauth2 Grant Type: `Refresh Token Grant`
    - Client ID: `OAUTH_CLIENT_ID`
    - Client Secret: `OAUTH_CLIENT_SECRET`
    - Refresh Token Grant Refresh Token: `OAUTH_REFRESH_TOKEN`
    - Oauth2 Token Url: `OAUTH_TOKEN_ENDPOINT`
    - Oauth2 Client Authentication: `OAuth 2.0 with Basic Auth Header set to client id and client secret`
    - Oauth2 Custom Oauth Response Response Type: `Json`
    - Json Expires In Key: `expires_in`
    - Json Expires In Format: `CUSTOM_OAUTH2_EXPIRES_IN_FORMAT_SECONDS`
2. Define your API action for channel creation.
    
    ```bash
    curl --location '{{Base_URL}}/api/v2/statements' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer {{snowflake_access_token}}' \
    --data '{
      "statement": "SHOW DATABASES;"
    }'
    ```
    
    - Path: `/api/v2/statements`
    - Method: `POST`
    - Request Body:
        
        ```json
        {
          "statement": "SHOW DATABASES;"
        }
        ```
        
    - Headers:
        
        
        | Key | Value |
        | --- | --- |
        | Accept | application/json |
3. Test your setup in Creator Studio and look for a successful execution.
    
    ```json
    
    {
    	"code": "*****",
    	"createdOn": 1716349584556,
    	"data": [
    		[
    			"***********",
    			"SNOWFLAKE",
    			"N",
    			"N",
    			....
    			....
    			....
    		]
    	]
    	...
    	...
    }
    ```
    

# **Congratulations!**

You've successfully integrated Snowflake’s API with Creator Studio. This opens up a variety of integration possibilities within your Snowflake workspace.
---
name: Workato
description: Connect Creator Studio to Workato
time_in_minutes: 30
difficulty_level: Beginner
---

# Introduction

Workato is a low-code, no-code tool that allows you to build “recipes” as custom APIs.

In this guide, we will demonstrate how to trigger a Workato API endpoint from Creator Studio and return data back to Creator Studio. We will walk through creating & publishing a recipe, testing it in Postman, and connecting it to Creator Studio.

We are going to build a simple “Reverse Echo” API that returns the value sent to the API, but backwards.

# Prerequisites

- Workato Account with Workato API Platform

# Walkthrough

## Step 1: Setup Trigger

1. Create a new recipe
    
    ![Untitled](Authentication%20Guide%20Workato%20c6344fa56dd748e9bc3f0c58d1abe8d3/Untitled.png)
    
    - **Name:** `EchoReverse`
    - **Starting Point:** `Build an API endpoint`
2. In your trigger configuration, click `Use JSON` under 
    
    ![Untitled](Authentication%20Guide%20Workato%20c6344fa56dd748e9bc3f0c58d1abe8d3/Untitled%201.png)
    
3. Provide the sample payload, then click `Generate Schema`
    
    ```json
    {
    	"name": "Luke"
    }
    ```
    
4. Add a response for the reversed name
    
    ![Untitled](Authentication%20Guide%20Workato%20c6344fa56dd748e9bc3f0c58d1abe8d3/Untitled%202.png)
    

## Step 2: Implement Recipe

1. Add an action to your recipe to `Create variable`, we’ll calculate the reversed name and store it here.
    
    ![Untitled](Authentication%20Guide%20Workato%20c6344fa56dd748e9bc3f0c58d1abe8d3/Untitled%203.png)
    
2. Create a new variable (`Reversed Name`), and enter `Formula` mode.
    
    ![Untitled](Authentication%20Guide%20Workato%20c6344fa56dd748e9bc3f0c58d1abe8d3/Untitled%204.png)
    
3. Calculate the reverse of the input string using Workato formulas
    
    ![Untitled](Authentication%20Guide%20Workato%20c6344fa56dd748e9bc3f0c58d1abe8d3/Untitled%205.png)
    
4. Return the value in the API Response. Select the Trigger response you configured above and pass the `Reversed Name` value 
    
    ![Untitled](Authentication%20Guide%20Workato%20c6344fa56dd748e9bc3f0c58d1abe8d3/Untitled%206.png)
    
5. Save the recipe.
6. Exit the recipe editor and start the recipe.
    
    ![Untitled](Authentication%20Guide%20Workato%20c6344fa56dd748e9bc3f0c58d1abe8d3/Untitled%207.png)
    

## Step 3: Connect to an API Endpoint

1. Go to [API Collections](https://app.workato.com/api_management/groups), select your API collection, and click `Create new endpoint`
    
    ![Untitled](Authentication%20Guide%20Workato%20c6344fa56dd748e9bc3f0c58d1abe8d3/Untitled%208.png)
    
2. Set up your endpoint
    
    ![Untitled](Authentication%20Guide%20Workato%20c6344fa56dd748e9bc3f0c58d1abe8d3/Untitled%209.png)
    
    - Name: `Reverse Echo`
    - Recipe: `Reverse Echo` this is the recipe we created in steps 1 & 2
    - Endpoint Path: `reverse-echo`
    - HTTP method: `POST`
3. Mark the endpoint as active
    
    ![Untitled](Authentication%20Guide%20Workato%20c6344fa56dd748e9bc3f0c58d1abe8d3/Untitled%2010.png)
    

## Step 4: Create an API Key

1. Go to [API Clients](https://app.workato.com/api_management/clients), create a new client. This is how you will authenticate with Moveworks.
    
    ![Untitled](Authentication%20Guide%20Workato%20c6344fa56dd748e9bc3f0c58d1abe8d3/Untitled%2011.png)
    
2. Create an Access Profile
    
    ![Untitled](Authentication%20Guide%20Workato%20c6344fa56dd748e9bc3f0c58d1abe8d3/Untitled%2012.png)
    
3. Setup the access profile
    
    ![Untitled](Authentication%20Guide%20Workato%20c6344fa56dd748e9bc3f0c58d1abe8d3/Untitled%2013.png)
    
    - Name: Any
    - API Collections: Select the API collection where you created your endpoint
    - Authentication Method: Use `Auth Token` for this guide.
4. Copy your access token & save it for future use
    
    ![Untitled](Authentication%20Guide%20Workato%20c6344fa56dd748e9bc3f0c58d1abe8d3/Untitled%2014.png)
    

## Step 5: Test in Postman

1. Go back to your API endpoint & copy the endpoint URL
    
    ![Untitled](Authentication%20Guide%20Workato%20c6344fa56dd748e9bc3f0c58d1abe8d3/Untitled%2015.png)
    
2. Build a cURL request to import to Postman
    
    ```bash
    curl --location '{{recipe_url}}' \
    --header 'Content-Type: application/json' \
    --header 'api-token: {{access_token}}' \
    --data '{
        "name": "Luke"
    }'
    ```
    
3. Run your request. It should return the name you provided, but reversed!
    
    ![Untitled](Authentication%20Guide%20Workato%20c6344fa56dd748e9bc3f0c58d1abe8d3/Untitled%2016.png)
    

## Step 6: Connect to Creator Studio

1. In your API editor, create a new connector. You can read more about the supported auth types on [our connector reference](https://developer.moveworks.com/creator-studio/connector-configuration/).
    - Base Url: `https://apim.workato.com`
    - Auth Config: `Api Key Auth`
    - Api Key Auth Auth Type: `Header Auth`
    - Header Auth Key: `api-token`
    - API Key: `{{access_key}}`
2. Add your API details. You can read more about setting up API actions from our [API configuration reference](https://developer.moveworks.com/creator-studio/api-configuration/).
    
    ```bash
    curl --location '{{base_url}}/mw/ajay-merchia-vv1/reverse-echo' \
    --data ''
    ```
    
    - Path: `/{{workato_tenant_name}}/{{collection_name}}/{{endpoint_name}}`
    - Method: `POST`
    - Body:
        
        ```json
        {
          "name": "{{query}}"
        }
        ```
        
    - Example Value: `Luke`
3. Hit test & celebrate!
    
    ```json
    {
        "reversed_name": "ekuL"
    }
    ```
    

# Congratulations!

You just connected your first Workato API to Creator Studio.
---
name: Workday
description: Connect Creator Studio to Workday
time_in_minutes: 30
difficulty_level: Intermediate
---

# Introduction

Workday is a cloud-based software vendor that specializes in human capital management (HCM), enterprise resource planning (ERP), and financial management applications.

This guide will walk you through creating a connector within Creator Studio to make API calls to Workday. We have separated this guide into three main sections:
- [Prerequisites](#prerequisites)
- [Set up Workday](#set-up-workday)
- [Create a Connector in Creator Studio](#create-a-connector-and-test-in-creator-studio)



# Prerequisites
- Workday account with admin privileges so we can create an API account
- [Install Postman](https://www.postman.com/downloads/) for testing the API connection

# Set up Workday
To connect to Workday from within Creator Studio, we are going to be using [OAuth2 with the Refresh Token](https://oauth.net/2/grant-types/refresh-token/). This requires a client_id, a client_secret and a refresh_token. The following will walk you through how to set up a user and create the necessary ids so we can set up the connector within Creator Studio.


1. Create an Integration Systems User (ISU)
2. Create Security Group
3. Add ISU to Security Group
4. Add Domain Security Policies to the Integration Systems Security Group
5. Create API Client for Integrations
6. Provision a Refresh Token for the ISU

## Step 1: Create Integration System User (ISU)

The first step is to create an Integration System User, this user can be used for all integration requests to the back-end API.

Use the universal search to find the **`Create Integration System User`** (ISU) Workday Task

![Untitled](images/Untitled%2016.png)

Use the **`Create Integration System User`** (ISU) Workday Task to create a user following these settings. Write down the username and password that you use.

![Untitled](images/Untitled%2017.png)

Validate that the ISU has these default permissions after creation.

![Untitled](images/Untitled%2018.png)

---

## Step 2: Create Security Group

Next we need to create a security group that we can put users into for integrations.

Access **`Create Security Group`** task (from Workday’s Universal Search) and create an **`Integration System Security Group (Unconstrained)`**.

![Untitled](images/Untitled%2019.png)

![Untitled](images/Untitled%2020-1.png)

Call the Integration Systems Security Group name **`Moveworks ISSG`**

![Untitled](images/Untitled%2021-1.png)

## Step 3: Add Integration Systems User to Security Group

We need to add our new user to the new security group we created.

Use the **`All Workday Accounts`** report to find the account again.

![Untitled](images/Untitled%2022.png)

Click on **`Security Profile`** > **`Assign Integration System Security Groups`**

![Untitled](images/Untitled%2023.png)

Assign the ISU to the ISSG

![Untitled](images/Untitled%2024.png)

## Step 4: Add Domain Security Policies to the Integration Systems Security Group

We need to give the apporpriate permissions to this security group so that we can call the api and any reports therein. By default, we just add everything but you may want to limit your api calls to only certain aspects of Workday.

Navigate to the ISSG using the **`View Security Group`** Report

![Untitled](images/Untitled%2025.png)

Use the menu item to access **`Security Group`** > **`Maintain Domain Permissions for Security Group`**

![Untitled](images/Untitled%2026.png)

Add any permissions that are needed for your Moveworks bot which will be dependent on what you plan on needing access to, the permissions we typically look for are shown [here](https://help.moveworks.com/docs/workday-access-requirements#permissions). 

Click Ok.

![Untitled](images/Untitled%2027.png)

Run the **`Activate Pending Security Policy Changes`** task to activate permissions

![Untitled](images/Untitled%2028.png)



## Step 5: Create API Client for Integrations

Universal search for **`Register API Client for Integrations`**

![search box to find api client for integrations](images/Untitled_10.png)

Set the name to **Moveworks** and add the scopes required.

![https://developer.moveworks.com/static/4c87b5210013217701570e0558eec348/c6bbc/registration.png](https://developer.moveworks.com/static/4c87b5210013217701570e0558eec348/c6bbc/registration.png)

Note your **`Client ID`** & **`Client Secret`**

![https://developer.moveworks.com/static/5011d27344ce82ae7d3b2ddc283b1e65/c6bbc/client_secret.png](images/client_secret.png)

Navigate to **`View API Clients`**. Note the **`Token Endpoint`** and **`Workday REST API Endpoint`**

![https://developer.moveworks.com/static/f83407419897649f501e24707114ec46/c6bbc/token_and_api.png](images/token_and_api.png)

## Step 6: Provision a Refresh Token for the ISU

From the **`View API Clients`** view, click on the **`API Clients for Integrations`** tab. Pick out the API Client you just created

![https://developer.moveworks.com/static/703d5272d024109eb4b30d808292e8a6/c6bbc/inspect_client.png](images/inspect_client.png)

From the related actions menu, select **`Manage Refresh Tokens for Integrations`**

![Manage refresh tokens page](images/Untitled_14.png)

Add the ISU Account you created earlier to the API Client

![manage refresh tokens for integrations page](images/isu_to_client.png)

Select **`Generate Refresh Token`**

![Generate a refresh token page](images/gen_refresh_token.png)

Note your  new refresh token.

![successfully regenerated refresh token page](images/refresh_token.png)



## Test the Connection

To test the connection, we need to first use the client_id and client_secret against the token api to get a bearer token. We then use that bearer token to run a query against the api.

We will use Postman to run these queries.

### Get a Bearer Token in Postman

1. Set up your request to import into Postman with your `CLIENT_ID`, `CLIENT_SECRET` and `REFRESH_TOKEN`.
    
    ```bash
    curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=refresh_token&refresh_token=YOUR_REFRESH_TOKEN" https://wd2-impl-services1.workday.com/ccx/oauth2/YOUR_TENANT_NAME/token
    ```
    
2. Import this request into Postman by clicking `file` -> `import`.

    ![Alt text](images/image.png)

3. Notice that the url and properties are filled in automatically. Execute by clicking `send`

    ![Alt text](images/image-1.png)
    
4. If the execution is successful, yous hould see the an access_token in the response.

![Alt text](images/image-2.png)
    
Copy the access_token string for the next step, note that some of the access_token is blurred out in the screenshot for security purposes!


### Test a Query
 This is a simple WQL query to get five employees (in no particular order) from Workday.

---
****NOTE:****

This query works because you gave our user access to Workday Query Language and Worker Data in [step 4](#step-4:-add-domain-security-policies-to-the-integration-systems-security-group)

---

1. Set up your request to import into Postman with your `TENANT_NAME` and `BEARER_TOKEN` in the below with the values from previous steps:

```bash
curl --location 'https://wd2-impl-services1.workday.com/ccx/api/wql/v1/YOUR_TENANT_NAME/data?limit=5&offset=0' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_BEARER_TOKEN' \
--data '{
    "query": "SELECT worker, fullName, employeeID  FROM allActiveEmployees"
}'
```

2. Import into Postman as you did in the previous section by going to `file` -> `import` and pasting your curl command

3. Confirm the values have been filled in properly by the import, if they have, you can run the command by hitting `send`

The above command should return the top five employees in your Workday database. If successful, you are done with the hardest part of connecting Creator Studio to Workday! 

![Alt text](images/image-3.png)

Next, let's take the above and create a connector within Creator Studio so we can query directly from within Moveworks.

# Create a Connector and Test in Creator Studio

Now that we have created everything within Workday and we have tested with our curl command, we can create duplicate our test in Creator Studio.

## Create a Connector

Since we are going to be running a query to test, we can start the connector creation from there. 

1. Let's start by going into the Queries workspace and creating a new query. You can follow the steps for creating a new query [here](https://developer.moveworks.com/creator-studio/quickstart/queries/) only instead of choosing an existing connector, choose to create a new one.

![Create a new connector](images/2024-01-05_21-49-22.png)

2. In your API editor, create a new connector. You can read more about the supported auth types on [our connector reference](https://developer.moveworks.com/creator-studio/connector-configuration/). 
Fill in the following for the connection information while replacing YOUR_CLIENT_ID, YOUR_CLIENT_SECRET, YOUR_REFRESH_TOKEN and YOUR_TENANT_NAME with the values from the above steps where you set up the Workday connection.

    - Base Url: `https://wd2-impl-services1.workday.com`
    - Auth Config: `Oauth2`
    - Oauth2 Grant Type: `Refresh Token Grant`
    - Client ID: `YOUR_CLIENT_ID`
    - Client Secret: `YOUR_CLIENT_SECRET`
    - Refresh Token Grant Refresh Token: `YOUR_REFRESH_TOKEN`
    - Oauth2 Token Url: `https://wd2-impl-services1.workday.com/ccx/oauth2/YOUR_TENANT/token`



Click Save

## Test the Connection

1. You can continue following the guide [here](https://developer.moveworks.com/creator-studio/quickstart/queries/) to create your query with the newly created connector. To test the same command from curl, you can enter the following on the `API Connection` screen.

API endpoint path: `/ccx/api/wql/v1/YOUR_TENANT/data`
Method: `POST`
Request body: `{
    "query": "SELECT worker, fullName, employeeID  FROM allActiveEmployees"
}`
Headers: `Content-Type` : `application/json`
Query parameters: `limit` : `5`

![Untitled](images/2024-01-06_06-52-59-1.png)

![Untitled](images/2024-01-06_06-53-17.png)

![Untitled](images/2024-01-05_21-49-22.png)



2. Click test, if you get the same output from your curl command, you have sucessfully created a connector into Workday and tested it! 

# **Congratulations!**

You've successfully integrated Workday's API with Creator Studio. This opens up a variety of automation and integration possibilities to Workday.
 




# Welcome to our guides
### Important disclaimers
 - This code is provided as an example only and is not designed for production use. You should fully understand the code and consider all the security implications before using it in a live environment.
 - API keys / tokens are examples and not live
---
id: 11
name: Custom RAG Query
description: Search information in a custom LLM that does its own retrieval-augmented generation
workspace: queries
purple_chat_link: https://developer.moveworks.com/creator-studio/developer-tools/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22botSettings%22%3A%7B%7D%2C%22mocks%22%3A%5B%7B%22id%22%3A6159%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22%3Cp%3EWho+won+the+Superbowl+2024%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22%3Cp%3EMoveworks+rephrases+query+to+%5C%22Who+won+the+Superbowl+in+2024%5C%22%3Cbr%3E%3Cbr%3ERequest+to+RAG+model%3A%3Cbr%3E%7B%3Cbr%3E++%5C%22prompt%5C%22%3A+%5C%22Who+won+the+Superbowl+in+2024%5C%22%3Cbr%3E%7D%3Cbr%3E%3Cbr%3EOutbound+Response%3A%3Cbr%3E%7B%3Cbr%3E++%5C%22result%5C%22%3A+%5C%22The+Kansas+City+Chiefs+won+Super+Bowl+LVIII+in+the+year+2024%2C+defeating+the+San+Francisco+49ers+with+a+final+score+of+25-22+in+overtime.%5C%22%3Cbr%3E%7D%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Cp%3EThe+Kansas+City+Chiefs+won+Super+Bowl+LVIII+in+the+year+2024%2C+defeating+the+San+Francisco+49ers+with+a+final+score+of+25-22+in+overtime.%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22%3Cp%3EWho+was+the+QB+for+the+opposing+team%3F%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22%3Cp%3EMoveworks+rephrases+query+to+%5C%22Who+was+the+quarterback+for+the+San+Francisco+49ers+in+Super+Bowl+LVIII+in+2024%3F%5C%22++%3Cbr%3E%3Cbr%3ERequest+to+RAG+model%3A+%3Cbr%3E%7B%3Cbr%3E+%5C%22prompt%5C%22%3A+%5C%22Who+was+the+quarterback+for+the+San+Francisco+49ers+in+Super+Bowl+LVIII+in+2024%3F%5C%22+%3Cbr%3E%7D++%3Cbr%3E%3Cbr%3EOutbound+Response%3A+%3Cbr%3E%7B%3Cbr%3E+%5C%22result%5C%22%3A+%5C%22Brock+Purdy%5C%22+%3Cbr%3E%7D+%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Cp%3EThe+quarterback+for+the+San+Francisco+49ers+in+Super+Bowl+LVIII%2C+which+was+held+in+2024%2C+was+Brock+Purdy%3Cbr%3E%3C%2Fp%3E%22%7D%5D%7D%7D%5D%7D
time_in_minutes: 10
difficulty_level: Beginner
---

# What does this pattern do?

Search information in a custom LLM that does its own retrieval-augmented generation.

[View Purple Chat](https://developer.moveworks.com/creator-studio/developer-tools/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22botSettings%22%3A%7B%7D%2C%22mocks%22%3A%5B%7B%22id%22%3A6159%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22%3Cp%3EWho+won+the+Superbowl+2024%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22%3Cp%3EMoveworks+rephrases+query+to+%5C%22Who+won+the+Superbowl+in+2024%5C%22%3Cbr%3E%3Cbr%3ERequest+to+RAG+model%3A%3Cbr%3E%7B%3Cbr%3E++%5C%22prompt%5C%22%3A+%5C%22Who+won+the+Superbowl+in+2024%5C%22%3Cbr%3E%7D%3Cbr%3E%3Cbr%3EOutbound+Response%3A%3Cbr%3E%7B%3Cbr%3E++%5C%22result%5C%22%3A+%5C%22The+Kansas+City+Chiefs+won+Super+Bowl+LVIII+in+the+year+2024%2C+defeating+the+San+Francisco+49ers+with+a+final+score+of+25-22+in+overtime.%5C%22%3Cbr%3E%7D%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Cp%3EThe+Kansas+City+Chiefs+won+Super+Bowl+LVIII+in+the+year+2024%2C+defeating+the+San+Francisco+49ers+with+a+final+score+of+25-22+in+overtime.%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22%3Cp%3EWho+was+the+QB+for+the+opposing+team%3F%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22%3Cp%3EMoveworks+rephrases+query+to+%5C%22Who+was+the+quarterback+for+the+San+Francisco+49ers+in+Super+Bowl+LVIII+in+2024%3F%5C%22++%3Cbr%3E%3Cbr%3ERequest+to+RAG+model%3A+%3Cbr%3E%7B%3Cbr%3E+%5C%22prompt%5C%22%3A+%5C%22Who+was+the+quarterback+for+the+San+Francisco+49ers+in+Super+Bowl+LVIII+in+2024%3F%5C%22+%3Cbr%3E%7D++%3Cbr%3E%3Cbr%3EOutbound+Response%3A+%3Cbr%3E%7B%3Cbr%3E+%5C%22result%5C%22%3A+%5C%22Brock+Purdy%5C%22+%3Cbr%3E%7D+%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Cp%3EThe+quarterback+for+the+San+Francisco+49ers+in+Super+Bowl+LVIII%2C+which+was+held+in+2024%2C+was+Brock+Purdy%3Cbr%3E%3C%2Fp%3E%22%7D%5D%7D%7D%5D%7D)

# Example Use Cases

1. **Perplexity**: Search the internet
2. **Manufacturing**: Search machine manuals
3. **Pharmaceuticals**: Answer questions about prescription drugs

# Design Considerations

## Design time

1. Start in the Queries workspace.
2. Define a wide-reaching name & short description for your query
3. Set up an [API Action](https://developer.moveworks.com/creator-studio/api-configuration/) to your RAG model.
4. [Label the API response](https://developer.moveworks.com/creator-studio/conversation-design/guidelines/api-labeling/). The ID is arbitrary, but you should mark the LLM response as your description.
5. For your trigger phrases, provide wide-reaching queries that showcase the different types of information your RAG model can serve.
6. During [slot extraction](https://developer.moveworks.com/creator-studio/conversation-design/slots/smart-extraction/#training-moveworks-to-recognize-your-slot), use the entire trigger phrase as your utterance.
7. Launch!


## Run time

- You SHOULD be on the [Next Gen Copilot](https://developer.moveworks.com/creator-studio/conversation-design/creator-studio-in-copilot/) for optimal results.
- Your Next Gen Copilot will write a question for your RAG model that considers the previous conversation history.
---
id: 28
name: Filter By ID
description: Filters a dataset on one column using an exact match.
workspace: queries
purple_chat_link: https://developer.moveworks.com/creator-studio/developer-tools/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22mocks%22%3A%5B%7B%22id%22%3A750%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%2C%22botName%22%3A%22%22%2C%22botImageUrl%22%3A%22%22%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22I%27m+in+building+86+--+where%27s+the+nearest+printer%3F%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22Moveworks+converts+%5C%22building+86%5C%22+to+%5C%2286%5C%22+and+passes+to+to+API%3A%5Cn%5Cn%3Ccode%3E%7B%5C%22building%5C%22%3A+%5C%2286%5C%22%7D%3C%2Fcode%3E%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22API+returns+a+list+of+printer+objects+matching+the+criteria%3A%5Cn%3Ccode%3E%5B%7B%5C%22printer%5C%22%3A+%5C%22Calisto%5C%22%2C+...%7D%2C+%7B%5C%22printer%5C%22%3A+Titan%5C%22%2C+...%7D%5D%3C%2Fcode%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Ci%3EOne+moment%2C+fetching+your+results.+This+may+take+%7E10+seconds%3C%2Fi%3E%5Cn%22%2C%22cards%22%3A%5B%7B%22title%22%3A%22Calista%3A+Canon+PIXMA%22%7D%2C%7B%22title%22%3A%22Titan%3A+Epson+Workforce%22%7D%5D%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22Show+me+Titan.%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22Sure%2C+here+is+Titan.%22%2C%22cards%22%3A%5B%7B%22title%22%3A%22Titan%3A+Epson+Workforce%22%2C%22text%22%3A%22%3Cb%3EPaper+Level%3C%2Fb%3E%3A+Full%5Cn%3Cb%3EDriver+Installation%3C%2Fb%3E%3A+%3Ca%3EClick+here%3C%2Fa%3E%22%7D%5D%7D%5D%7D%7D%5D%2C%22botSettings%22%3A%7B%22name%22%3A%22%22%2C%22imageUrl%22%3A%22%22%7D%7D
time_in_minutes: 15
difficulty_level: Beginner
---

# What does this pattern do?

Filter a dataset on one column using an exact match.

[View Purple Chat](https://developer.moveworks.com/creator-studio/developer-tools/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22mocks%22%3A%5B%7B%22id%22%3A750%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%2C%22botName%22%3A%22%22%2C%22botImageUrl%22%3A%22%22%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22I%27m+in+building+86+--+where%27s+the+nearest+printer%3F%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22Moveworks+converts+%5C%22building+86%5C%22+to+%5C%2286%5C%22+and+passes+to+to+API%3A%5Cn%5Cn%3Ccode%3E%7B%5C%22building%5C%22%3A+%5C%2286%5C%22%7D%3C%2Fcode%3E%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22API+returns+a+list+of+printer+objects+matching+the+criteria%3A%5Cn%3Ccode%3E%5B%7B%5C%22printer%5C%22%3A+%5C%22Calisto%5C%22%2C+...%7D%2C+%7B%5C%22printer%5C%22%3A+Titan%5C%22%2C+...%7D%5D%3C%2Fcode%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Ci%3EOne+moment%2C+fetching+your+results.+This+may+take+%7E10+seconds%3C%2Fi%3E%5Cn%22%2C%22cards%22%3A%5B%7B%22title%22%3A%22Calista%3A+Canon+PIXMA%22%7D%2C%7B%22title%22%3A%22Titan%3A+Epson+Workforce%22%7D%5D%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22Show+me+Titan.%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22Sure%2C+here+is+Titan.%22%2C%22cards%22%3A%5B%7B%22title%22%3A%22Titan%3A+Epson+Workforce%22%2C%22text%22%3A%22%3Cb%3EPaper+Level%3C%2Fb%3E%3A+Full%5Cn%3Cb%3EDriver+Installation%3C%2Fb%3E%3A+%3Ca%3EClick+here%3C%2Fa%3E%22%7D%5D%7D%5D%7D%7D%5D%2C%22botSettings%22%3A%7B%22name%22%3A%22%22%2C%22imageUrl%22%3A%22%22%7D%7D)

# Example Use Cases

1. **Finance**: Find invoices by their linked PO ID
2. **IT**: View watches on an incident

# Design Considerations

## Design time

1. Start in the Queries workspace.
2. Provide a descriptive name & short description
3. Set up an [API Action](https://developer.moveworks.com/creator-studio/api-configuration/) to your endpoint. Make sure to use `{{query}}` as the filtered value.
4. [Label the API response](https://developer.moveworks.com/creator-studio/conversation-design/guidelines/api-labeling/).
5. For your trigger phrases, provide examples of ways that users might ask to filter on the specified value
6. During [slot extraction](https://developer.moveworks.com/creator-studio/conversation-design/slots/smart-extraction/#training-moveworks-to-recognize-your-slot), specify the ID / keyword that will be passed to your API from the trigger phrases.
7. Launch!

## Run time

### All Experiences

- Your copilot will [limit the number of records shown](https://developer.moveworks.com/creator-studio/conversation-design/guidelines/api-labeling/#select-additional-fields)

### Classic Copilot

- Your copilot will make an API call for each possible ID detected.
- Your copilot will pass the slot value exactly as specified in the utterance
- Your copilot will not ask for the ID if it is omitted from the utterance
---
id: 20
name: Id-Based Action Path
description: Take an action on a business object, referencing the ID of the object.
workspace: paths
purple_chat_link: https://developer.moveworks.com/creator-studio/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22mocks%22%3A%5B%7B%22id%22%3A1636%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%2C%22botName%22%3A%22%22%2C%22botImageUrl%22%3A%22%22%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22I+just+got+off+a+call+with+a+vendor+and+we+need+to+add+some+funds+to+their+PO.%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22Which+PO+do+you+need+to+add+funds+to%3F%22%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22PO123%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22What%27s+the+new+dollar+value+of+the+PO%3F%22%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22%244567.89%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22%3Cp%3EInbound+Request+to+Middleware%3A%3Cbr%3E%3Cbr%3E%7B%3Cbr%3E%5C%22purchase_order%5C%22%3A+%5C%22PO123%5C%22%2C%3Cbr%3E%5C%22funds%5C%22%3A+%5C%22%244567.89%5C%22%3Cbr%3E%7D%3Cbr%3E%3Cbr%3EProcess%3A%3Cbr%3E1.+Validate+PO123+exists+in+System+X%3Cbr%3E2.+Parse+%5C%22funds%5C%22+as+cents%3Cbr%3E3.+Add+the+funds+to+PO123%3Cbr%3E%3Cbr%3EOutbound+Response%3A%3Cbr%3E%7B%5C%22status%5C%22%3A+%5C%22ok%5C%22%7D%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22Thanks.+I%27ve+submitted+your+request+for+more+funds+to+be+added+to+that+purchase+order.%22%7D%5D%7D%7D%5D%2C%22botSettings%22%3A%7B%22name%22%3A%22%22%2C%22imageUrl%22%3A%22%22%7D%7D
time_in_minutes: 15
difficulty_level: Beginner
---

# What does this pattern do?

Update specific business records within a system by specifying their ID & the details of the change. Inform the user about any success or fail.

[View Purple Chat](https://developer.moveworks.com/creator-studio/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22mocks%22%3A%5B%7B%22id%22%3A1636%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%2C%22botName%22%3A%22%22%2C%22botImageUrl%22%3A%22%22%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22I+just+got+off+a+call+with+a+vendor+and+we+need+to+add+some+funds+to+their+PO.%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22Which+PO+do+you+need+to+add+funds+to%3F%22%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22PO123%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22What%27s+the+new+dollar+value+of+the+PO%3F%22%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22%244567.89%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22%3Cp%3EInbound+Request+to+Middleware%3A%3Cbr%3E%3Cbr%3E%7B%3Cbr%3E%5C%22purchase_order%5C%22%3A+%5C%22PO123%5C%22%2C%3Cbr%3E%5C%22funds%5C%22%3A+%5C%22%244567.89%5C%22%3Cbr%3E%7D%3Cbr%3E%3Cbr%3EProcess%3A%3Cbr%3E1.+Validate+PO123+exists+in+System+X%3Cbr%3E2.+Parse+%5C%22funds%5C%22+as+cents%3Cbr%3E3.+Add+the+funds+to+PO123%3Cbr%3E%3Cbr%3EOutbound+Response%3A%3Cbr%3E%7B%5C%22status%5C%22%3A+%5C%22ok%5C%22%7D%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22Thanks.+I%27ve+submitted+your+request+for+more+funds+to+be+added+to+that+purchase+order.%22%7D%5D%7D%7D%5D%2C%22botSettings%22%3A%7B%22name%22%3A%22%22%2C%22imageUrl%22%3A%22%22%7D%7D)

# Example Use Cases

1. **Finance**: Add funds to a purchase order
2. **T&E**: Cancel a flight booking
3. **Project Management**: Mark Jira ticket as complete

# Design Considerations

## Design time

1. Start in the Paths workspace.
2. Start collecting slots from your user. You can collect any of our [slot types](https://developer.moveworks.com/creator-studio/paths/slot-types/)
3. Set up an [API Action](https://developer.moveworks.com/creator-studio/api-configuration/). All your slots and any [user attributes](https://developer.moveworks.com/creator-studio/user-attributes-reference/) will be available.
4. Run any additional validation in your [automation tools](https://developer.moveworks.com/creator-studio/automation-tools).
5. Set up your generative intent & launch rules.


## Run time

- Your copilot will assume the name or ID is an exact match
- Your copilot will ask all questions sequentially & will not "shortcut"
- Your copilot will only inform the user if the API action succeeded or failed.
---
id: 10
name: Notification with link
description: Send an actionable alert to users with deep links that track clickthrough & completion.
workspace: events
purple_chat_link: https://developer.moveworks.com/creator-studio/developer-tools/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22mocks%22%3A%5B%7B%22id%22%3A1636%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%2C%22botName%22%3A%22%22%2C%22botImageUrl%22%3A%22%22%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22iPaaS%3A+Scheduled+job+that+runs+once+a+month+at+the+end+of+the+month.%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22It%27s+time+to+prep+for+month+end+close%21+We+need+your+help+to+ensure+our+financials+accurately+represent+our+business+activity.+%5Cn%5Cn%F0%9F%91%89+Please+look+through+your+inbox+and+forward+any+invoices+that+may+have+been+missed+to+%3Ca+href%3D%5C%22mailto%3Aap%40moveworks.ai%5C%22%3Eap%40moveworks.ai%3C%2Fa%3E.%5Cn%5Cn%F0%9F%91%89+We+also+need+your+expense+reports+submitted+in+%3Ca+href%3D%5C%22expensify.com%5C%22%3EExpensify%21%3C%2Fa%3E%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22Emoji+codes+are+supported+across+all+platforms.+Links+all+work+with+link+tracking+analytics.%22%7D%5D%7D%7D%5D%2C%22botSettings%22%3A%7B%22name%22%3A%22%22%2C%22imageUrl%22%3A%22%22%7D%7D
time_in_minutes: 10
difficulty_level: Beginner
---

# What does this pattern do?

Send an actionable alert to users with trackable deep links to measure click through & completion.

[View Purple Chat](https://developer.moveworks.com/creator-studio/developer-tools/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22mocks%22%3A%5B%7B%22id%22%3A1636%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%2C%22botName%22%3A%22%22%2C%22botImageUrl%22%3A%22%22%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22iPaaS%3A+Scheduled+job+that+runs+once+a+month+at+the+end+of+the+month.%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22It%27s+time+to+prep+for+month+end+close%21+We+need+your+help+to+ensure+our+financials+accurately+represent+our+business+activity.+%5Cn%5Cn%F0%9F%91%89+Please+look+through+your+inbox+and+forward+any+invoices+that+may+have+been+missed+to+%3Ca+href%3D%5C%22mailto%3Aap%40moveworks.ai%5C%22%3Eap%40moveworks.ai%3C%2Fa%3E.%5Cn%5Cn%F0%9F%91%89+We+also+need+your+expense+reports+submitted+in+%3Ca+href%3D%5C%22expensify.com%5C%22%3EExpensify%21%3C%2Fa%3E%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22Emoji+codes+are+supported+across+all+platforms.+Links+all+work+with+link+tracking+analytics.%22%7D%5D%7D%7D%5D%2C%22botSettings%22%3A%7B%22name%22%3A%22%22%2C%22imageUrl%22%3A%22%22%7D%7D)

# Example Use Cases

1. **Finance**: Ask employees to submit any expense reports they need to submit at the end of the month
2. **Recruiting**: Run employee referral drives with deep-links to applicant tracking system
3. **Sales**: Remind sales representatives to add call summary to notes if not completed within 24 hours

# Design Considerations

## Design time

1. Start in the Events workspace.
2. Generate an [event ID](https://developer.moveworks.com/creator-studio/conversation-design/triggers/event-triggers)
3. Prepare a message using our [chat markup](https://developer.moveworks.com/creator-studio/reference/markup). You can prepare your chat markup using our [message tester tool](https://developer.moveworks.com/creator-studio/developer-tools/message-tester/)
4. Send it to the user.


## Run time

- Your copilot will provide a wrapped URL which will redirect through Moveworks services for analytics
---
id: 12
name: Static Lookup
description: Performs a lookup in a system without requiring any parameters
workspace: queries
purple_chat_link: https://developer.moveworks.com/creator-studio/developer-tools/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22botSettings%22%3A%7B%7D%2C%22mocks%22%3A%5B%7B%22id%22%3A8533%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22Are+there+any+upcoming+birthdays+within+the+company%3F%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22%3Cp%3ERun+report+in+Workday+to+get+any+upcoming+birthdays%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Ci%3EOne+moment%2C+fetching+your+results.+This+may+take+%7E10+seconds%3C%2Fi%3E%5Cn%22%2C%22cards%22%3A%5B%7B%22title%22%3A%22John+Mouse%3A+March+25%22%7D%2C%7B%22title%22%3A%22Julia+Gargonzo%3A+April+1%22%7D%2C%7B%22title%22%3A%22Lilly+Lucy%3A+April+2%22%7D%5D%7D%5D%7D%7D%5D%7D
time_in_minutes: 10
difficulty_level: Beginner
---

# What does this pattern do?

Request information in an external system without filtering.

[View Purple Chat](https://developer.moveworks.com/creator-studio/developer-tools/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22botSettings%22%3A%7B%7D%2C%22mocks%22%3A%5B%7B%22id%22%3A8533%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22Are+there+any+upcoming+birthdays+within+the+company%3F%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22%3Cp%3ERun+report+in+Workday+to+get+any+upcoming+birthdays%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Ci%3EOne+moment%2C+fetching+your+results.+This+may+take+%7E10+seconds%3C%2Fi%3E%5Cn%22%2C%22cards%22%3A%5B%7B%22title%22%3A%22John+Mouse%3A+March+25%22%7D%2C%7B%22title%22%3A%22Julia+Gargonzo%3A+April+1%22%7D%2C%7B%22title%22%3A%22Lilly+Lucy%3A+April+2%22%7D%5D%7D%5D%7D%7D%5D%7D)

# Example Use Cases

1. **HR**: Get upcoming birthdays
2. **Legal**: Get latest NDA
3. **IT**: Get system outages

# Design Considerations

## Design time

1. Start in the Queries workspace.
2. Define a name & short description that identifies the usecase, keep this as specific as possible to remove ambiguity
3. Set up an [API Action](https://developer.moveworks.com/creator-studio/api-configuration/) to your query.
4. [Label the API response](https://developer.moveworks.com/creator-studio/conversation-design/guidelines/api-labeling/). 
5. For your trigger phrases, provide a couple of queries that you think might be asked to get this information.
6. Launch!


## Run time

- Your copilot will only return the items you have labeled during step 4 above
---
id: 2
name: User-Based Action Path
description: Update or submit information using the current user's information.
workspace: paths
purple_chat_link: https://developer.moveworks.com/creator-studio/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22mocks%22%3A%5B%7B%22id%22%3A1636%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%2C%22botName%22%3A%22%22%2C%22botImageUrl%22%3A%22%22%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22I+just+got+married+and+would+like+to+update+my+emergency+contact+to+my+spouse.%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22Okay%2C+I+can+help+you+update+your+emergency+contact.%22%2C%22cards%22%3A%5B%7B%22title%22%3A%22What+is+your+emergency+contact%27s+full+name%3F%22%7D%5D%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22John+Doe%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22If+the+HRIS+requires+first+%26+last+name+to+be+stored+separately%2C+then+the+questions+must+be+split+up.%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22Okay%2C+their+full+name+is+%5C%22John+Doe%5C%22%22%2C%22cards%22%3A%5B%7B%22title%22%3A%22What+is+your+emergency+contact%27s+phone+number%3F%22%7D%5D%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22123-456-7890%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22Phone+numbers+are+not+validated.+They+must+be+validated+by+the+iPaaS.%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22Thank+you+for+providing+the+phone+number.%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22API+Call%3A%5CnUpdate+Emergency+Contact%5Cn%5Cn%7B%5Cn++%5C%22new_contact_phone_number%5C%22%3A+%5C%22123-456-7890%5C%22%2C%5Cn++%5C%22new_contact_name%5C%22%3A+%5C%22John+Doe%5C%22%2C%5Cn++%5C%22for_user%5C%22%3A+%5C%22gwen%40moveworks.ai%5C%22%5Cn%7D%22%7D%5D%7D%7D%5D%2C%22botSettings%22%3A%7B%22name%22%3A%22%22%2C%22imageUrl%22%3A%22%22%7D%7D
time_in_minutes: 30
difficulty_level: Beginner
---

# What does this pattern do?

Change personal structured data within a system, and inform the user if it succeeded or failed based on the user details.

[View Purple Chat](https://developer.moveworks.com/creator-studio/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22mocks%22%3A%5B%7B%22id%22%3A1636%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%2C%22botName%22%3A%22%22%2C%22botImageUrl%22%3A%22%22%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22I+just+got+married+and+would+like+to+update+my+emergency+contact+to+my+spouse.%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22Okay%2C+I+can+help+you+update+your+emergency+contact.%22%2C%22cards%22%3A%5B%7B%22title%22%3A%22What+is+your+emergency+contact%27s+full+name%3F%22%7D%5D%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22John+Doe%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22If+the+HRIS+requires+first+%26+last+name+to+be+stored+separately%2C+then+the+questions+must+be+split+up.%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22Okay%2C+their+full+name+is+%5C%22John+Doe%5C%22%22%2C%22cards%22%3A%5B%7B%22title%22%3A%22What+is+your+emergency+contact%27s+phone+number%3F%22%7D%5D%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22123-456-7890%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22Phone+numbers+are+not+validated.+They+must+be+validated+by+the+iPaaS.%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22Thank+you+for+providing+the+phone+number.%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22API+Call%3A%5CnUpdate+Emergency+Contact%5Cn%5Cn%7B%5Cn++%5C%22new_contact_phone_number%5C%22%3A+%5C%22123-456-7890%5C%22%2C%5Cn++%5C%22new_contact_name%5C%22%3A+%5C%22John+Doe%5C%22%2C%5Cn++%5C%22for_user%5C%22%3A+%5C%22gwen%40moveworks.ai%5C%22%5Cn%7D%22%7D%5D%7D%7D%5D%2C%22botSettings%22%3A%7B%22name%22%3A%22%22%2C%22imageUrl%22%3A%22%22%7D%7D)

# Example Use Cases

1. **HR**: Update my emergency contacts
2. **Operations**: Register myself for a company event
3. **Sales**: Create a new lead assigned to me
4. **Security**: Reset MFA for user

# Design Considerations

## Design time

1. Start in the Paths workspace.
2. Start collecting slots which need to be changed or submitted to a service. You can collect any of our [slot types](https://developer.moveworks.com/creator-studio/paths/slot-types/)
3. Configure any [custom attributes](https://developer.moveworks.com/creator-studio/user-attributes-reference/) that are needed if your API does not accept email addresses.
4. Add an [API Action](https://developer.moveworks.com/creator-studio/api-configuration/) using your slots. Make sure to include an email or user attribute so your system knows which user is executing this action.
5. Run any additional validation in your [automation tools](https://developer.moveworks.com/creator-studio/automation-tools).
6. Set up your generative intent & launch rules.

## Run time

- Your copilot will ask all questions sequentially & will not "shortcut"
- Your copilot will only inform the user if the API action succeeded or failed.
# Welcome to our guides
### Important disclaimers
 - This code is provided as an example only and is not designed for production use. You should fully understand the code and consider all the security implications before using it in a live environment.
 - API keys / tokens are examples and not live
---
design_pattern_id: 28
name: Concur Expense Reports Lookup
description: Query your Expense Reports details from Concur within your bot
systems: [concur]
purple_chat_link: https://developer.moveworks.com/creator-studio/developer-tools/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22botSettings%22%3A%7B%7D%2C%22mocks%22%3A%5B%7B%22id%22%3A2617%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22Show+me+my+expense+reports%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22Running+Creator+Studio+plugin+to+retrieve+Expense+Reports+from+Concur%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22You+have+two+expense+reports%3A%22%2C%22cards%22%3A%5B%7B%22title%22%3A%22New+test+report%22%2C%22text%22%3A%22Submitted+%26+Pending+Approval%3Cbr%3E%3Cb%3ETotal+Claimed+Amount%3A%3C%2Fb%3E+%2460.00%3Cbr%3EStatus%3A+%3Ci%3ECurrently+not+paid%3C%2Fi%3E%22%7D%2C%7B%22title%22%3A%22Internet+Reimbursement%22%2C%22text%22%3A%22Not+submitted%3Cbr%3E%3Cb%3ETotal+Claimed+Amount%3A%3C%2Fb%3E+%2425.00%3Cbr%3EStatus%3A+%3Ci%3ENot+paid%3C%2Fi%3E%22%7D%5D%7D%5D%7D%7D%5D%7D
time_in_minutes: 15
difficulty_level: Beginner
---


# Introduction

SAP Concur is a widely used platform for managing travel and expense reports in many organizations. While navigating through the Concur platform to access expense reports can be time-consuming, integrating it with your bot streamlines the process, allowing you to access your expense reports conveniently through simple conversational queries.

In this guide, we'll walk you through the process of integrating Concur Expense Reports lookup functionality into your bot using Creator Studio.

Let's get started!

# Prerequisites

- [Postman](https://www.postman.com/) or an API Testing Tool
- Concur Connector built in Creator Studio (follow the [Concur Authentication](https://developer.moveworks.com/creator-studio/resources/authentication-guide?id=concur) guide to create your connector)

# What are we building?

## Conversation Design

[This purple chat](https://developer.moveworks.com/creator-studio/developer-tools/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22botSettings%22%3A%7B%7D%2C%22mocks%22%3A%5B%7B%22id%22%3A2617%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22Show+me+my+expense+reports%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22Running+Creator+Studio+plugin+to+retrieve+Expense+Reports+from+Concur%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22You+have+two+expense+reports%3A%22%2C%22cards%22%3A%5B%7B%22title%22%3A%22New+test+report%22%2C%22text%22%3A%22Submitted+%26+Pending+Approval%3Cbr%3E%3Cb%3ETotal+Claimed+Amount%3A%3C%2Fb%3E+%2460.00%3Cbr%3EStatus%3A+%3Ci%3ECurrently+not+paid%3C%2Fi%3E%22%7D%2C%7B%22title%22%3A%22Internet+Reimbursement%22%2C%22text%22%3A%22Not+submitted%3Cbr%3E%3Cb%3ETotal+Claimed+Amount%3A%3C%2Fb%3E+%2425.00%3Cbr%3EStatus%3A+%3Ci%3ENot+paid%3C%2Fi%3E%22%7D%5D%7D%5D%7D%7D%5D%7D) shows the experience we are going to build. 

## Creator Studio Components

- **Triggers:**
    1. Natural Language
- **Slots**:
    1. None
- **Actions:**
    1. Query Concur Expense Reports for the User
- **Guidelines:**
    1. None

Based on the needs of this use case, we should build a [Lookup Single Record by ID / Keyword](https://developer.moveworks.com/creator-studio/design-patterns/dp-6/)**.**

## API Research

There’s only 1 API needed to build this use case

### API #1: Expense Report Lookups

Since we want to integrate with Concur Expense, we should look into their [Expense v3 APIs](https://developer.concur.com/api-reference/expense/expense-report/v3.reports.html). For this use case, we will need only 1 API call.

![Untitled](Use%20Case%20Tutorial%20Lookup%20Expense%20Reports%20in%20Concur%200ad48c0ab26047b1bab45a82557a0bda/Untitled.png)

1. [Expense v3 APIs](https://developer.concur.com/api-reference/expense/expense-report/v3.reports.html): An API for Concur to retrieve expense reports owned by the user.
    
    Here is the API we used to fetch 10 expense reports for the given user’s email address
    
    ```bash
    curl --location 'https://us2.api.concursolutions.com/api/v3.0/expense/reports?user={{user_email_address}}&limit=10' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer {{generated_bearer_token}}'
    ```
    

> In the above API, we have used email address as the user identifier because during User setup in Concur the `Use Email as Username` checkbox was checked out.
> This is required for building this use case since we will be leveraging the User’s email address from the [User Attributes](https://developer.moveworks.com/creator-studio/reference/user-attributes/#user-attributes-reference) mapping in your Moveworks configuration. 
>
> ![Untitled](Use%20Case%20Tutorial%20Lookup%20Expense%20Reports%20in%20Concur%200ad48c0ab26047b1bab45a82557a0bda/Untitled%201.png)
> 
>To check which Email Address is configured for your Moveworks bot, follow the steps in [How to find your User Profile](https://help.moveworks.com/docs/control-centre-identity#how-to-find-your-user-profile) in Moveworks Setup and check if the value of the `Email Address` is the same as the one setup as the login username for your Concur instance.
>
>If you don't have access to Moveworks Setup, you can request to get access to it by discussing with your Customer Support team or raising a request in our [Community portal](https://community.moveworks.com/moveworks-setup-83).

> If the username that is setup in your Concur instance is not the same as your email address, then you would need to build a workflow to first fetch the username using the email address and then fetch the expense reports based on that username.

# Steps

## Step 1: Build in Creator Studio

### Setup use case

1. Start in the Queries Workspace and create a new query.
2. Provide the Basic Info so the Next Gen Copilot knows how to use this plugin:
    1. **Query Label**: `Lookup Expenses from Concur` 
    2. **Short Description:** `Lookup your Expense Reports from Concur. This includes looking up any information regarding the name, status, approver, total to be paid, and more.`

### Setup the API

1. Select the Concur connector that you set up earlier in the [Authentication Guide](https://developer.moveworks.com/creator-studio/resources/authentication-guide?id=concur)
    
    ![Untitled](Use%20Case%20Tutorial%20Lookup%20Expense%20Reports%20in%20Concur%200ad48c0ab26047b1bab45a82557a0bda/Untitled%202.png)
    
2. Define your API action for querying the Expense Reports data from Concur:
    - Path: `/api/v3.0/expense/reports`
    - Method: `GET`
    - Headers:
        
        
        | KEY | VALUE |
        | --- | --- |
        | Accept | application/json |
    - Query parameters:
        
        
        | KEY | VALUE |
        | --- | --- |
        | user | {{user.email_addr}} |
        | limit | 10 |
        - Selecting `user.email_addr` would ensure that the bot picks up the the email address that is currently mapped to the Bot for the user, and use that as the query parameter in the above API.
3. Test your setup in Creator Studio and look for a successful execution. A 200 Response Code represents that the API was successfully executed.
If you check the `OwnerLoginID` or `OwnerName` from the returned API response, you will see that it contains your Email ID and Name respectively. 
    
    ![Untitled](Use%20Case%20Tutorial%20Lookup%20Expense%20Reports%20in%20Concur%200ad48c0ab26047b1bab45a82557a0bda/Untitled%203.png)
    

### Label the API Response

1. Select the `Name` as the Identifier.
2. Select any of the fields as the Description. In this example, we have selected `Approval Status Name` as the Description.
3. From among the Additional Fields, select the fields that you want users to query on and label them accordingly.
    
    ![Untitled](Use%20Case%20Tutorial%20Lookup%20Expense%20Reports%20in%20Concur%200ad48c0ab26047b1bab45a82557a0bda/Untitled%204.png)
    
4. No follow-up action needed.

### Build your Generative Intent

1. Since we want to capture the email ID of the User who is using the Bot, which is further used to filter the Expense Reports API, we will need to provide accurate examples when to trigger this Use Case. Creator Studio will automatically generate utterances which will trigger the Use Case to execute the API and fetch details for your expense reports.
    
    ![Untitled](Use%20Case%20Tutorial%20Lookup%20Expense%20Reports%20in%20Concur%200ad48c0ab26047b1bab45a82557a0bda/image4.png)

    We want to provide different kinds of utterances here based on our Use Case. We want the bot to trigger the Expense Reports Use Case whenever a user asks anything related to their expense reports. Here are some examples you can use:
    - What are my expense reports?
    - Get me the status of my expense reports.
    - What are the approval statuses of my expense reports?
    - When were my expense reports created?
    

### Launch the use case

Use our [Launch Rules](https://developer.moveworks.com/creator-studio/launch-options/) to launch your use case to your Copilot. 

## Step 2: See it in action!

Trigger the use case by asking for it from your Copilot. Find interesting ways to combine it with your own enterprise data.

Note: It could take a couple minutes before your flow shows up in your copilot. If it doesn’t show up after five minutes, follow [our troubleshooting guides](https://developer.moveworks.com/creator-studio/troubleshooting/support) to further debug.

# Congratulations!

You just added Concur Expense Report lookup to your Copilot! Check out our other guides for inspiration on what to build next.
---
design_pattern_id: 10  # The ID of the associated design pattern
name: Jira Approvals   # The name of the guide
description: Send Proactive Jira Approval Notifications   # Brief description of the guide
systems: [jira]  # List of systems involved in the use case
purple_chat_link: https://developer.moveworks.com/creator-studio/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22botSettings%22%3A%7B%7D%2C%22mocks%22%3A%5B%7B%22id%22%3A7525%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22Hi%2C+Can+you+please+help+me+reset+my+Azure+MFA.%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22Sure%2C+do+you+want+to+proceed+with+resetting+the+MFA+as+this+cannot+be+reverted+%3F%22%2C%22cards%22%3A%5B%7B%22buttons%22%3A%5B%7B%22style%22%3A%22PRIMARY%22%2C%22text%22%3A%22Yes%22%7D%2C%7B%22text%22%3A%22No%22%7D%5D%7D%5D%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22Inbound+Request+to+Middleware+%5C%22Azure+Functions%5C%22+%5Cn%5Cn%7B%5Cn+%5C%22email%5C%22+%3A+%3Cuser_email%3E%5Cn%7D%5Cn+%5CnProcess%3A%5Cn1.+Generate+Bearer+Token+for+Authentication%5Cn2.+LIST+the+existing+MFA+for+the+user%5Cn3.+Delete+the+MFA+for+the+user%5Cn%5CnOutbound+Response%3A%5Cn%7B%5Cn+++%5C%22Status%5C%22%3A+%5C%22OK+%28200%29%5C%22%5Cn%7D%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22I%27ve+successfully+reset+the+MFA+on+Azure%22%7D%5D%7D%7D%5D%7D](https://developer.moveworks.com/creator-studio/developer-tools/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22botSettings%22%3A%7B%7D%2C%22mocks%22%3A%5B%7B%22id%22%3A1557%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22Bot%22%2C%22text%22%3A%22Hi+Neal%2C%5CnYou+have+a+new+pending+approval+in+JIRA.+It+has+been+requested+by+nmoran%40moveworks.us+and+is+of+type+%5C%22Request+a+budget+allocation%5C%22.+Please+view+it+%3Ca+href%3D%5C%22www.jira.com%5C%22%3Ehere%3C%2Fa%3E%22%7D%5D%7D%7D%5D%7D  # URL of the linked chat
time_in_minutes: 60   # Time in minutes to complete the guide
difficulty_level: Intermediate  # Difficulty level: "Beginner", "Intermediate", or "Advanced"
accreditations: [npmoran21, DEFAULT]
---

# Introduction

[JIRA Automation](https://www.atlassian.com/software/jira/features/automation) is a feature that allows you to build automations and workflows based on events that occur within JIRA Service Desk.

In this tutorial, we will explore how to use Creator Studio to notify approvers in-bot in near-real time when a new approval is pending.

Let's get started!

# 🛠 **Prerequisites**

- The JIRA Automation Feature enabled in JIRA Service Desk
- Moveworks Creator Studio
- Moveworks Events API Key
- Postman or an API Testing Tool
- A Request Item in JIRA that requires an Approval


# What are we building?

## Conversation Design

[This purple chat](https://developer.moveworks.com/creator-studio/developer-tools/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22botSettings%22%3A%7B%7D%2C%22mocks%22%3A%5B%7B%22id%22%3A1557%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22Bot%22%2C%22text%22%3A%22Hi+Neal%2C%5CnYou+have+a+new+pending+approval+in+JIRA.+It+has+been+requested+by+nmoran%40moveworks.us+and+is+of+type+%5C%22Request+a+budget+allocation%5C%22.+Please+view+it+%3Ca+href%3D%5C%22www.jira.com%5C%22%3Ehere%3C%2Fa%3E%22%7D%5D%7D%7D%5D%7D) shows the experience we are going to build.

**This use case is made up of:**

✨ **Triggers:** Initiated by JIRA

🤲 **Slots**: None

🏃‍♂️ **Actions: None - Link to JIRA Approval record**

📚 **Guidelines:** None

Based on the needs of this use case, we should build a [Actionable Updates](https://developer.moveworks.com/creator-studio/design-patterns/dp-10).

## API Research

There’s only 1 API needed to build this use case - Which is the Moveworks Events API

### API #1: The Moveworks Events API

Since most of the work is actually done in JIRA Automations, the only API call we will be making is to the Moveworks Events API

![Screenshot 2024-01-09 at 5.20.18 PM.png](Use%20Case%20Guide%20JIRA%20Approvals%20f1ce3fe611e644a99a97f00cfb719fbb/Screenshot_2024-01-09_at_5.20.18_PM.png)

1. [Moveworks API](https://developer.moveworks.com/openapi/reference/#operation/sendMessageForEvent)**:** An API to send proactive events to a Moveworks user
2. [JIRA Retrieve Issue API](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issues/#api-rest-api-2-issue-issueidorkey-get)**:** A JIRA API to retrieve a given issue and fields

Although we will only be using the Moveworks API in the actual implementation, it is important to use Postman in order to be able to view a given issue, as we will be leveraging a feature called [Smart Values](https://support.atlassian.com/cloud-automation/docs/jira-smart-values-issues/) to dynamically introspect details about the issue and approvers in order to send a comprehensive message

- Authenticating to the Moveworks API (follow [our guide](https://developer.moveworks.com/openapi/reference/#operation/testAuth))
    - Authenticating is relatively easy - you can obtain your Bearer Token from you Moveworks Customer Success Team
- Authenticating to the JIRA API (follow [JIRAs Guide](https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/))
    - You’ll notice this link is for Basic Auth - the simplest way to authenticate for ad-hoc calls and the recommended approach for this exercise
- [Install Postman](https://www.postman.com/downloads/)

# Steps

## Step 1: Build the Event in Creator Studio

The first step is to build the Event in Moveworks that we want receive the notification for.  This will be a webhook-type architecture which will listen for events that are sent to it.

### Create the event

1. Open Creator Studio and click Events. If you need more info, [follow our quickstart guide](https://developer.moveworks.com/creator-studio/quickstart/events/).
2. Simply name the event whatever you like, and choose “No” for follow up actions as seen here.  Choose “Next” and deploy to yourself or others for testing.

    ![Screenshot 2024-01-09 at 5.37.20 PM.png](Use%20Case%20Guide%20JIRA%20Approvals%20f1ce3fe611e644a99a97f00cfb719fbb/Screenshot_2024-01-09_at_5.37.20_PM.png)

3. Once it has been created, go back and click into the Event you just created.  You should now see an Event ID.  Copy that to your clipboard - ‼️ we will refer to this as the EventID going forward and will use it later in the exercise.

    ![Screenshot 2024-01-09 at 5.39.03 PM.png](Use%20Case%20Guide%20JIRA%20Approvals%20f1ce3fe611e644a99a97f00cfb719fbb/Screenshot_2024-01-09_at_5.39.03_PM.png)


## Step 2: JIRA - Identify a Project with Approvals

In this step we will do the required research in order to not only identify which project we are targeting to notify approvals for, but also to inspect the payload for issues within that project in order to build out the JIRA Automation effectively.

### Identify the project and Request Types with Approvals

1. Login to your JIRA ServiceDesk and choose a project that has request types with approvals.
2. You can then choose “Project Settings” within the project to view the Request Types.
3. Those with approvals should have a workflow under “Edit Workflow” that looks something like the screenshots below

    ![Screenshot 2024-01-09 at 5.45.06 PM.png](Use%20Case%20Guide%20JIRA%20Approvals%20f1ce3fe611e644a99a97f00cfb719fbb/Screenshot_2024-01-09_at_5.45.06_PM.png)


![Screenshot 2024-01-09 at 5.46.41 PM.png](Use%20Case%20Guide%20JIRA%20Approvals%20f1ce3fe611e644a99a97f00cfb719fbb/Screenshot_2024-01-09_at_5.46.41_PM.png)

### Create a new issue of the identified request type

The point of this step is to create a new issue type that will generate pending approvals.  This will allow us to view a fresh instance of that issue knowing that all the proper approvals can be read.

1. Create an issue of the type you inspected in step 1.

    ![Screenshot 2024-01-09 at 5.51.36 PM.png](Use%20Case%20Guide%20JIRA%20Approvals%20f1ce3fe611e644a99a97f00cfb719fbb/Screenshot_2024-01-09_at_5.51.36_PM.png)

    ![Screenshot 2024-01-09 at 5.52.08 PM.png](Use%20Case%20Guide%20JIRA%20Approvals%20f1ce3fe611e644a99a97f00cfb719fbb/Screenshot_2024-01-09_at_5.52.08_PM.png)

2. You can now see I have an issue of identifier “LEG-54”.  It also has a pending approval attached to it.  Now I can leverage the JIRA API with Basic Auth in Postman to inspect the details of this issue using the API endpoint in the screenshot below which is also referenced in the [JIRA API Specification](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issues/#api-rest-api-2-issue-issueidorkey-get).  Copy and paste this JSON response into a JSON editor or simply leave it up in Postman so we can reference it later.

![Screenshot_2024-01-09_at_5.56.10_PM.png](Use%20Case%20Guide%20JIRA%20Approvals%20f1ce3fe611e644a99a97f00cfb719fbb/Screenshot_2024-01-09_at_5.56.10_PM.png)

1. ‼️ - One thing that is very important to note is that depending on your Administrative settings, a user’s email may not show up by default due to JIRA’s GDPR settings.  More can be read about here in the [JIRA Community](https://community.developer.atlassian.com/t/get-users-email-as-system-admin-in-jira/33322).  Please see these recommendations to see what best fits your organization.  We will require the ability to read this email via API so we can send the message to the identified approver(s).

    ![Screenshot 2024-01-09 at 6.00.44 PM.png](Use%20Case%20Guide%20JIRA%20Approvals%20f1ce3fe611e644a99a97f00cfb719fbb/Screenshot_2024-01-09_at_6.00.44_PM.png)


## Step 4: Build the Flow in JIRA Automation

This is the step where the bulk of the automation and work will take place.  Luckily JIRA makes this very simple for us to leverage.  Keep in mind this exercise will turn on approval notifications for ALL issue and request types that require approvals in the identified project.  Further tuning can occur for specific types but do require additional logic and fall outside the scope of this guide.

### Build the Wofklow in JIRA Automation

1. For the project you have identified, choose “Project Settings”, then “Automation”.
2. On the top right select “Create Rule”.
3. The first thing you will see is “Add a Trigger”.  There are many operations that can trigger an automation to run here, but we are looking for “Approval Required” as seen below.

![Screenshot 2024-01-09 at 6.07.36 PM.png](Use%20Case%20Guide%20JIRA%20Approvals%20f1ce3fe611e644a99a97f00cfb719fbb/Screenshot_2024-01-09_at_6.07.36_PM.png)

1. We will now click “Add Component” as a next step and you will see these choices.  We need to choose “FOR EACH: Add a branch”.  This is because there could be multiple approvers on a single issue.  This will allow us to loop through all approvers and send a message to each of them individually

    ![Screenshot 2024-01-09 at 6.12.16 PM.png](Use%20Case%20Guide%20JIRA%20Approvals%20f1ce3fe611e644a99a97f00cfb719fbb/Screenshot_2024-01-09_at_6.12.16_PM.png)

2. You will now see input fields for “Smart value” and “Variable name”.  The Smart value is the dynamic reference to the JSON fields from the body we retrieved in the Postman call.  Keep in mind this will probably be different in every JIRA instance due to custom field names.  You can see in the following screenshot and code snippet how I am referencing the array of approvers via custom field name.  This operation takes the approvers JSON array and puts in the variable name “approvers” so I can reference it later.

    ![Screenshot 2024-01-09 at 6.14.34 PM.png](Use%20Case%20Guide%20JIRA%20Approvals%20f1ce3fe611e644a99a97f00cfb719fbb/Screenshot_2024-01-09_at_6.14.34_PM.png)

    ```jsx
    "customfield_10026": [
                {
                    "id": "60",
                    "name": "To Do",
                    "finalDecision": "pending",
                    "canAnswerApproval": false,
                    "approvers": [
                        {
                            "approver": {
                                "accountId": "621e8911db58c1006878ed63",
                                "emailAddress": "nmoran@moveworks.us",
                                "displayName": "Neal Moran",
                                "active": true,
                                "timeZone": "America/Danmarkshavn",
                                "_links": {
                                    "jiraRest": "https://moveworksus.atlassian.net/rest/api/2/user?accountId=621e8911db58c1006878ed63",
                                    "avatarUrls": {
                                        "48x48": "https://secure.gravatar.com/avatar/ad2cba6d794a9e650017c027a7a55d23?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FNM-1.png",
                                        "24x24": "https://secure.gravatar.com/avatar/ad2cba6d794a9e650017c027a7a55d23?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FNM-1.png",
                                        "16x16": "https://secure.gravatar.com/avatar/ad2cba6d794a9e650017c027a7a55d23?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FNM-1.png",
                                        "32x32": "https://secure.gravatar.com/avatar/ad2cba6d794a9e650017c027a7a55d23?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FNM-1.png"
                                    },
                                    "self": "https://moveworksus.atlassian.net/rest/api/2/user?accountId=621e8911db58c1006878ed63"
                                }
                            },
                            "approverDecision": "pending"
                        }
                    ],
                    "createdDate": {
                        "iso8601": "2024-01-10T00:51:48+0000",
                        "jira": "2024-01-10T00:51:48.461+0000",
                        "friendly": "Today 12:51 AM",
                        "epochMillis": 1704847908461
                    },
                    "_links": {
                        "self": "https://moveworksus.atlassian.net/rest/servicedeskapi/request/161173/approval/60"
                    }
                }
            ]
    ```

3. Now that we have access to all approvers and can loop through them, we can add the final pieces for validation and leverage the Event Webhook we created earlier.  As a validation precaution, add a new component “IF: Add a Condition”.  Then choose {{smart values}} condition.  We can now reference fields within the variable we captured above so let’s check and make the sure the emailAddress is “not null” before sending the message to the user.

    ![Screenshot 2024-01-09 at 6.29.25 PM.png](Use%20Case%20Guide%20JIRA%20Approvals%20f1ce3fe611e644a99a97f00cfb719fbb/Screenshot_2024-01-09_at_6.29.25_PM.png)

    ![Screenshot 2024-01-09 at 6.29.48 PM.png](Use%20Case%20Guide%20JIRA%20Approvals%20f1ce3fe611e644a99a97f00cfb719fbb/Screenshot_2024-01-09_at_6.29.48_PM.png)

4. Now for the final step we will send the approval message to the user.  Select new component and “Send Web Request”.  For the Web Request URL enter where EventID is the value you copied when you created the event in Creator Studio

```text
https://api.moveworks.ai/rest/v1/events/{{EventID}}/messages/send
```

1. Your HTTP method will be POST and your Web Request Body will be “Custom Data”

    ![Screenshot 2024-01-09 at 6.33.17 PM.png](Use%20Case%20Guide%20JIRA%20Approvals%20f1ce3fe611e644a99a97f00cfb719fbb/Screenshot_2024-01-09_at_6.33.17_PM.png)

2. Within the custom data body we will formulate the message you are going to send to the user.  One thing to note - you can reference ANY field in the issue that came back from the JSON response in the Postman call.  You’ll notice I’m referencing the creator’s email address {{creator.emailAddress}} and the issue type {{issueType.name}} so I can show the approver this info, but it is not limited to this.  See the code snipped below - we are also referencing the {{issueKey}} which allows us to dynamically build the link to the issue, as well as the {{approvers.approver.emailAddress}} so Moveworks knows who to send this message to as the approver

```json
{
    "message": "You have a new pending approval in JIRA.  It has been requested by {{creator.emailAddress}} and is of type \"{{issueType.name}}\".  Please view it <a href=\"https://moveworksus.atlassian.net/jira/servicedesk/projects/LEG/queues/custom/58/{{issue.key}}\">here</a>",
    "recipients": ["{{approvers.approver.emailAddress}}"]
}
```

1. Once this is done, the final piece is the Authorization.  You can create an Event API Key [here](https://developer.moveworks.com/creator-studio/integrations/inbound/credentials-management/)

![Screenshot 2024-01-09 at 6.38.32 PM.png](Use%20Case%20Guide%20JIRA%20Approvals%20f1ce3fe611e644a99a97f00cfb719fbb/Screenshot_2024-01-09_at_6.38.32_PM.png)

1. Your completed automation flow should look something like this.


    ![Screenshot 2024-01-09 at 6.39.21 PM.png](Use%20Case%20Guide%20JIRA%20Approvals%20f1ce3fe611e644a99a97f00cfb719fbb/Screenshot_2024-01-09_at_6.39.21_PM.png)


## Step 5: See it in action!

Trigger the use case by creating the issue with approval. Here’s a quick demo.

[https://www.loom.com/share/e2cdfc7cddd8402c8ff7226048c10bd5?sid=0e5f2dc9-3b6d-439a-bdf3-be0b275ba2c1](https://www.loom.com/share/e2cdfc7cddd8402c8ff7226048c10bd5?sid=0e5f2dc9-3b6d-439a-bdf3-be0b275ba2c1)

# Congratulations!

You just added JIRA Approval notifications with links to your Copilot! Say good-bye to those long waiting approvals that only get checked periodically or notified by email.
---
design_pattern_id: 2  # The ID of the associated design pattern
name: Microsoft MFA Reset  # Name of the use case
description: Add a use case to your copilot that can reset Microsoft MFA  # Brief description of the use case
systems: [ azure-function-app, microsoft-graph-api ]  # List of systems involved in the use case
purple_chat_link: https://developer.moveworks.com/creator-studio/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22botSettings%22%3A%7B%7D%2C%22mocks%22%3A%5B%7B%22id%22%3A7525%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22Hi%2C+Can+you+please+help+me+reset+my+Azure+MFA.%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22Sure%2C+do+you+want+to+proceed+with+resetting+the+MFA+as+this+cannot+be+reverted+%3F%22%2C%22cards%22%3A%5B%7B%22buttons%22%3A%5B%7B%22style%22%3A%22PRIMARY%22%2C%22text%22%3A%22Yes%22%7D%2C%7B%22text%22%3A%22No%22%7D%5D%7D%5D%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22Inbound+Request+to+Middleware+%5C%22Azure+Functions%5C%22+%5Cn%5Cn%7B%5Cn+%5C%22email%5C%22+%3A+%3Cuser_email%3E%5Cn%7D%5Cn+%5CnProcess%3A%5Cn1.+Generate+Bearer+Token+for+Authentication%5Cn2.+LIST+the+existing+MFA+for+the+user%5Cn3.+Delete+the+MFA+for+the+user%5Cn%5CnOutbound+Response%3A%5Cn%7B%5Cn+++%5C%22Status%5C%22%3A+%5C%22OK+%28200%29%5C%22%5Cn%7D%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22I%27ve+successfully+reset+the+MFA+on+Azure%22%7D%5D%7D%7D%5D%7D  # URL of the linked chat
time_in_minutes: 60  # Time in minutes to complete the use case
difficulty_level: Advanced  # Difficulty level: "Beginner", "Intermediate", or "Advanced"
---

### **Introduction**

Multi-Factor Authentication (MFA) is a security protocol that demands more than one method of authentication from independent categories of credentials to verify the user's identity for a login or other transaction. It creates a layered defense, making it more challenging for unauthorized users to access a target.

However, there are cases where an MFA reset would be required for users due to the following reasons:

- **Forgotten MFA Credentials**
- **Lost or New Device**
- **Suspicious Activity**
- **App Malfunctions**

In this tutorial, we will explore how to integrate Creator Studio with Microsoft Azure MFA for MFA Reset.

Let's get started!

# What are we building?

## Conversation Design

[This purple chat](https://developer.moveworks.com/creator-studio/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22botSettings%22%3A%7B%7D%2C%22mocks%22%3A%5B%7B%22id%22%3A7525%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22Hi%2C+Can+you+please+help+me+reset+my+Azure+MFA.%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22Sure%2C+do+you+want+to+proceed+with+resetting+the+MFA+as+this+cannot+be+reverted+%3F%22%2C%22cards%22%3A%5B%7B%22buttons%22%3A%5B%7B%22style%22%3A%22PRIMARY%22%2C%22text%22%3A%22Yes%22%7D%2C%7B%22text%22%3A%22No%22%7D%5D%7D%5D%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22Inbound+Request+to+Middleware+%5C%22Azure+Functions%5C%22+%5Cn%5Cn%7B%5Cn+%5C%22email%5C%22+%3A+%3Cuser_email%3E%5Cn%7D%5Cn+%5CnProcess%3A%5Cn1.+Generate+Bearer+Token+for+Authentication%5Cn2.+LIST+the+existing+MFA+for+the+user%5Cn3.+Delete+the+MFA+for+the+user%5Cn%5CnOutbound+Response%3A%5Cn%7B%5Cn+++%5C%22Status%5C%22%3A+%5C%22OK+%28200%29%5C%22%5Cn%7D%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22I%27ve+successfully+reset+the+MFA+on+Azure%22%7D%5D%7D%7D%5D%7D) shows the experience we are going to build.

**This use case is made up of:**

✨ **Triggers:** Natural Language

🤲 **Slots**: User-supplied confirmation to reset all devices

🏃‍♂️ **Actions:** Reset all MFA devices for a user

📚 **Guidelines:** None

Based on the needs of this use case, we should build a ****User-Based Action Path****

## API Design

There’s only 1 API needed to build this use case

### API #1: Reset all devices

Since we want to integrate with Azure MFA, we should look into their Graph APIs. For this use case, we will need two API calls:

![Untitled](Use%20Case%20Guide%20Microsoft%20MFA%20Reset%20ce908c78ba7e462db7a30c342050723d/Untitled.png)

1. **[List Authentication Methods API](https://learn.microsoft.com/en-us/graph/api/authentication-list-phonemethods?view=graph-rest-1.0&tabs=http):** An API to list MFA devices for the user
2. **[Delete Authentication Method API](https://learn.microsoft.com/en-us/graph/api/phoneauthenticationmethod-delete?view=graph-rest-1.0&tabs=http):** An API to delete an MFA device

Both these APIs are hosted on the Microsoft Graph API and should be authenticated with a bearer token. You can follow our [Microsoft Graph Guide](https://developer.moveworks.com/creator-studio/resources/authentication-guide?id=microsoft-graph-api) to create an API key with the right privileges.

- Access to the Microsoft Graph APIs (follow [our guide](https://developer.moveworks.com/creator-studio/resources/authentication-guide?id=microsoft-graph-api))
- An Azure Function App Deployment (follow [our guide](https://developer.moveworks.com/creator-studio/resources/authentication-guide?id=azure-function-app))
- [Install Postman](https://www.postman.com/downloads/)

# **Prerequisites**

- A Working Azure Function (follow [our guide](https://developer.moveworks.com/creator-studio/resources/authentication-guide?id=azure-function-app))
- Postman

# **Walkthrough**

## **Step 1: Build the “Reset MFA” API**

### Implement the Azure Function Code

1. Open your Azure Function App code. If you don’t have it handy, [follow our guide](https://developer.moveworks.com/creator-studio/resources/authentication-guide?id=azure-function-app).
2. Update your code with the API flowchart we outlined above:
    
    ```python
    def main(req: func.HttpRequest) -> func.HttpResponse:
        logging.info('Python HTTP trigger function processed a request.')
    
        # Part 1: Parse the current user email from the request
    
        # Part 2: Retrieve all MFA Auth Methods setup by the user
    
        # Part 3: Delete the MFA Auth Methods for the user
    
        # Part 4: Return success to the user
    ```
    
3. Implement code using the API calls researched above.
    
    ```python
    import logging
    import requests
    import azure.functions as func
    import json
    
    def main(req: func.HttpRequest) -> func.HttpResponse:
        logging.info('Python HTTP trigger function processed a request.')
    
        # Part 1: Parse the current user email from the request
        try:
            req_body = req.get_json()
            name = req_body.get('mail')
        except ValueError:
            pass
    
        if mail:
            token_url = 'https://login.microsoft.com/<tenant_ID>/oauth2/token'  # Replace with the token URL
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            data = {
                'grant_type': 'client_credentials',
                'client_id': '[Redacted]',
                'client_secret': '[Redacted]',
                'resource': 'https://graph.microsoft.com'
            }
    
            try:
                token_response = requests.post(token_url, headers=headers, data=data)
                token_response.raise_for_status()  # Raise an exception if the request was unsuccessful
                access_token = token_response.json().get('access_token')
            except Exception as e:
                logging.error(f'Error occurred during token retrieval: {str(e)}')
                return func.HttpResponse('Internal Server Error', status_code=500)
    
            # Use the access_token in subsequent API calls
            list_response = list_items(access_token, mail)
            delete_response = delete_item(access_token, list_response, mail)
            
            # Part 4: Return success to the user
            if delete_response == 204:
                return func.HttpResponse(status_code=200)
                # return func.HttpResponse(f"MFA has been deleted for the user {name} List Response: {list_response}\nDelete Response: {delete_response} \nEvent Response: {event_response}", status_code=200)
            else:
                return func.HttpResponse(f"Delete call failed for mail {mail} List Response: {list_response}\nDelete Response: {delete_response}", status_code=500)
        else:
            return func.HttpResponse(f"The 'mail' variable is not provided in the request body.")
    
    # Part 2: Retrieve all MFA Auth Methods setup by the user
    def list_items(access_token, mail):
    
        api_url = f'https://graph.microsoft.com/v1.0/users/{mail}/authentication/microsoftAuthenticatorMethods'  # Replace with the API endpoint for listing items
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.get(api_url, headers=headers)
            response.raise_for_status()  # Raise an exception if the request was unsuccessful
            json_data = response.json()  # Parse the response JSON
            value = json_data['value']  # Access the 'value' list
            if value:  # Check if the list is not empty
                first_item = value[0]  # Get the first item in the list
                item_id = first_item['id']  # Access the value of the 'id' attribute
                return item_id
            else:
                return 'No items found'
        except Exception as e:
            logging.error(f'Error occurred during list call: {str(e)}')
            return 'List Error'
    
    # Part 3: Delete the MFA Auth Methods for the user
    def delete_item(access_token, list_response, mail):
        api_url = f'https://graph.microsoft.com/v1.0/users/{mail}/authentication/microsoftAuthenticatorMethods/{list_response}'  # Replace with the API endpoint for deleting an item
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
    
        try:
            response = requests.delete(api_url, headers=headers)
            response.raise_for_status()  # Raise an exception if the request was unsuccessful
            status_code = response.status_code
            return status_code  # Return the response text
        except Exception as e:
            logging.error(f'Error occurred during delete call: {str(e)}')
            return 'Delete Error'
    ```
    

### ****Validating & Deploying the API****

You can follow our system guide on Azure Functions to [test & deploy](https://developer.moveworks.com/creator-studio/resources/authentication-guide?id=azure-function-app) your function. 

You may want to create some fictitious MFA devices for testing. The following API call will create an MFA device for the specified user.

```python
curl --location '[https://graph.microsoft.com/v1.0/users/{{your_email}](https://graph.microsoft.com/v1.0/users/%7B%7Byour_email%7D)}/authentication/phoneMethods' \
--header 'Content-Type: application/json' \
--data '{
"phoneNumber": "+1 2065555555",
"phoneType": "office"
}'
```

## ****Step 2: Build in Creator Studio****

![Screenshot 2023-07-09 at 10.23.24 AM.png](Use%20Case%20Guide%20Microsoft%20MFA%20Reset%20ce908c78ba7e462db7a30c342050723d/Screenshot_2023-07-09_at_10.23.24_AM.png)

### ****Setup use case****

1. Start in the Paths Workspace
2. Title your use case: `Microsoft MFA Reset`

### ****Build the conversation design****

1. Start with the Conversation flow here where we request confirmation using “Yes” and “No” as a multiple choice option.
    
    ![Untitled](Use%20Case%20Guide%20Microsoft%20MFA%20Reset%20ce908c78ba7e462db7a30c342050723d/Untitled%201.png)
    
2. Add an API Action to execute your Azure Function App.
    - Connector: Follow our [Microsoft Graph API guide](https://developer.moveworks.com/creator-studio/resources/authentication-guide?id=microsoft-graph-api).
    - Path: `/api/trigger_azure_zee`
    - Method: `POST`
    - Headers:
        
        
        | Key | Value |
        | --- | --- |
        | Content-Type | application/json |
    - Request Body:
        
        ```python
        {
            "name": "{{user_email_addr}}"
        }
        ```
        
    - Action Description: `API call to delete the Azure Auth Method`

### Build your generative intent & launch the use case

Build a [Generative Intent](https://developer.moveworks.com/creator-studio/paths/generative-intents/) and then use our [Launch Rules](https://developer.moveworks.com/creator-studio/launch-options/) to launch your use case to your Copilot. 

## Step 3: See it in action!

Trigger the use case by asking for it from your Copilot. [Here’s a quick demo](https://www.youtube.com/watch?v=OtjnspEnfAc).

# Congratulations!

You just added Microsoft MFA Reset to your Copilot! Say good-bye to those IT tickets. Check out our other guides for inspiration on what to build next.
---
design_pattern_id: 11
name: Perplexity Online Search
description: Searches online results from the Perplexity search engine
systems: [perplexity]
purple_chat_link: https://developer.moveworks.com/creator-studio/developer-tools/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22botSettings%22%3A%7B%7D%2C%22mocks%22%3A%5B%7B%22id%22%3A6159%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22%3Cp%3EWho+won+the+Superbowl+2024%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22%3Cp%3EMoveworks+rephrases+query+to+%5C%22Who+won+the+Superbowl+in+2024%5C%22%3Cbr%3E%3Cbr%3ERequest+to+Perplexity+%28abbrievated%29%3A%3Cbr%3E%7B%3Cbr%3E%5C%22prompt%5C%22%3A+%5C%22Who+won+the+Superbowl+in+2024%5C%22%3Cbr%3E%7D%3Cbr%3E%3Cbr%3EOutbound+Response+%28abbrievated%29%3A%3Cbr%3E%7B%3Cbr%3E%5C%22result%5C%22%3A+%5C%22The+Kansas+City+Chiefs+won+Super+Bowl+LVIII+in+the+year+2024%2C+defeating+the+San+Francisco+49ers+with+a+final+score+of+25-22+in+overtime.%5C%22%3Cbr%3E%7D%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Cp%3EThe+Kansas+City+Chiefs+won+Super+Bowl+LVIII+in+the+year+2024%2C+defeating+the+San+Francisco+49ers+with+a+final+score+of+25-22+in+overtime.%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22%3Cp%3EWho+was+the+QB+for+the+opposing+team%3F%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22%3Cp%3EMoveworks+rephrases+query+to+%5C%22Who+was+the+quarterback+for+the+San+Francisco+49ers+in+Super+Bowl+LVIII+in+2024%3F%5C%22%3Cbr%3E%3Cbr%3ERequest+to+Perplexity+%28abbrievated%29%3A%3Cbr%3E%7B%3Cbr%3E%5C%22prompt%5C%22%3A+%5C%22Who+was+the+quarterback+for+the+San+Francisco+49ers+in+Super+Bowl+LVIII+in+2024%3F%5C%22%3Cbr%3E%7D%3Cbr%3E%3Cbr%3EOutbound+Response+%28abbrievated%29%3A%3Cbr%3E%7B%3Cbr%3E%5C%22result%5C%22%3A+%5C%22Brock+Purdy%5C%22%3Cbr%3E%7D%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Cp%3EThe+quarterback+for+the+San+Francisco+49ers+in+Super+Bowl+LVIII%2C+which+was+held+in+2024%2C+was+Brock+Purdy%3Cbr%3E%3C%2Fp%3E%22%7D%5D%7D%7D%5D%7D
time_in_minutes: 5
difficulty_level: Beginner
---

# Introduction

[Perplexity](https://www.perplexity.ai/) is a search engine that continuously indexes the web and allows you to access LLMs that have access to that content. 

In this tutorial, we will demonstrate how to retrieve online search results from Perplexity through Creator Studio.

Let's get started!

# What are we building?

## Conversation Design

[This purple chat](https://developer.moveworks.com/creator-studio/developer-tools/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22botSettings%22%3A%7B%7D%2C%22mocks%22%3A%5B%7B%22id%22%3A6159%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22%3Cp%3EWho+won+the+Superbowl+2024%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22%3Cp%3EMoveworks+rephrases+query+to+%5C%22Who+won+the+Superbowl+in+2024%5C%22%3Cbr%3E%3Cbr%3ERequest+to+Perplexity+%28abbrievated%29%3A%3Cbr%3E%7B%3Cbr%3E%5C%22prompt%5C%22%3A+%5C%22Who+won+the+Superbowl+in+2024%5C%22%3Cbr%3E%7D%3Cbr%3E%3Cbr%3EOutbound+Response+%28abbrievated%29%3A%3Cbr%3E%7B%3Cbr%3E%5C%22result%5C%22%3A+%5C%22The+Kansas+City+Chiefs+won+Super+Bowl+LVIII+in+the+year+2024%2C+defeating+the+San+Francisco+49ers+with+a+final+score+of+25-22+in+overtime.%5C%22%3Cbr%3E%7D%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Cp%3EThe+Kansas+City+Chiefs+won+Super+Bowl+LVIII+in+the+year+2024%2C+defeating+the+San+Francisco+49ers+with+a+final+score+of+25-22+in+overtime.%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22%3Cp%3EWho+was+the+QB+for+the+opposing+team%3F%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22%3Cp%3EMoveworks+rephrases+query+to+%5C%22Who+was+the+quarterback+for+the+San+Francisco+49ers+in+Super+Bowl+LVIII+in+2024%3F%5C%22%3Cbr%3E%3Cbr%3ERequest+to+Perplexity+%28abbrievated%29%3A%3Cbr%3E%7B%3Cbr%3E%5C%22prompt%5C%22%3A+%5C%22Who+was+the+quarterback+for+the+San+Francisco+49ers+in+Super+Bowl+LVIII+in+2024%3F%5C%22%3Cbr%3E%7D%3Cbr%3E%3Cbr%3EOutbound+Response+%28abbrievated%29%3A%3Cbr%3E%7B%3Cbr%3E%5C%22result%5C%22%3A+%5C%22Brock+Purdy%5C%22%3Cbr%3E%7D%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Cp%3EThe+quarterback+for+the+San+Francisco+49ers+in+Super+Bowl+LVIII%2C+which+was+held+in+2024%2C+was+Brock+Purdy%3Cbr%3E%3C%2Fp%3E%22%7D%5D%7D%7D%5D%7D) shows the experience we are going to build.

## Creator Studio Components

- Triggers:
    1. Natural language
- Slots:
    1. A search query
- Actions
    1. Retrieve LLM output
- Guidelines
    1. None

Based on the needs of this use case, we should build a **Custom RAG Query**.

## API Research

There’s only 1 API needed to build this use case. If we look at Perplexity’s API reference, there’s only one endpoint: [Chat Completions](https://docs.perplexity.ai/reference/post_chat_completions).

Based on the [Supported Models](https://docs.perplexity.ai/docs/model-cards#online-llms) documentation, we want to do an online search, so we should use either `pplx-7b-online` or `pplx-70b-online`. We should be careful about [pricing](https://docs.perplexity.ai/docs/pricing) for these models.

# Prerequisites

- A Perplexity Connection (follow [our guide](https://developer.moveworks.com/creator-studio/resources/authentication-guide?id=perplexity))

# Steps

## Step 1: Build in Creator Studio

### Setup use case

1. Start in the Queries Workspace and create a new query.
2. Provide the Basic Info so the Next Gen Copilot knows how to use this plugin
    1. Label: `Browse the Internet`
    2. Short Description: `Uses Perplexity to search for up-to-date information on the web. Information is usually 1-3 days old.`

### Setup the API

1. Select [the perplexity integration](https://developer.moveworks.com/creator-studio/resources/authentication-guide?id=perplexity) you set up earlier.
    
    ![Untitled](Use%20Case%20Tutorial%20Perplexity%20Online%20Search%20f1697b887ee94a45a422a1c4e988bada/Untitled.png)
    
2. Define your API action for browsing the internet.
    
    ```bash
    curl --request POST \
         --url https://api.perplexity.ai/chat/completions \
         --header 'accept: application/json' \
         --header 'content-type: application/json' \
         --data '
    {
      "model": "pplx-70b-online",
      "messages": [
        {
          "role": "system",
          "content": "Use all available internet information to answer the question precisely, accurately, and concisely."
        },
        {
          "role": "user",
          "content": "{{query}}"
        }
      ]
    }
    '
    ```
    
    - Path: `/chat/completions`
    - Method: `POST`
    - Request Body:
        
        ```json
        {
          "model": "pplx-70b-online",
          "messages": [
            {
              "role": "system",
              "content": "Use all available internet information to answer the question precisely, accurately, and concisely."
            },
            {
              "role": "user",
              "content": "{{query}}"
            }
          ]
        }
        ```
        
    - Headers:
        
        
        | Key | Value |
        | --- | --- |
        | accept | application/json |
        | content-type | application/json |
3. Test your setup in Creator Studio and look for a successful execution.
    
    ![Untitled](Use%20Case%20Tutorial%20Perplexity%20Online%20Search%20f1697b887ee94a45a422a1c4e988bada/Untitled%201.png)
    

### Label the API Response

1. Select the `role` as the identifier
2. Select the `content` as the description
    
    ![Untitled](Use%20Case%20Tutorial%20Perplexity%20Online%20Search%20f1697b887ee94a45a422a1c4e988bada/Untitled%202.png)
    
3. No follow-up action is needed.

### Setup your Generative Intent

Since we want the full question to be sent to Perplexity, we need to disable smart extraction on the natural language slot. To do this, we need the `Keyword` to match the `User utterance example` for every example.

![Untitled](Use%20Case%20Tutorial%20Perplexity%20Online%20Search%20f1697b887ee94a45a422a1c4e988bada/Untitled%203.png)

We are going to want a pretty wide generative intent here since this can handle all internet queries. Here are some you can use

1. Who won the superbowl this week?
2. What are the top trending movies on Netflix?
3. What's the stock price of Apple?
4. What happened to Salesforce recently in the news?
5. Which movies are currently topping the box office?
6. Who are the headliners for Coachella this year?
7. Give me a list of the top 25 companies in the F500
8. Which companies IPO'ed recently?
9. What are the latest advancements in renewable energy?
10. Which countries have made it to space?

### Launch the use case

Use our [Launch Rules](https://developer.moveworks.com/creator-studio/launch-options/) to launch your use case to your Copilot. 

## Step 3: See it in action!

Trigger the use case by asking for it from your Copilot. Find interesting ways to combine it with your own enterprise data.

Check out [this example](https://www.linkedin.com/feed/update/urn:li:activity:7163521696874844160?updateEntityUrn=urn%3Ali%3Afs_feedUpdate%3A%28V2%2Curn%3Ali%3Aactivity%3A7163521696874844160%29):

1. Combines stock information with employee data
2. Combines public news with internal documentation

Note: It could take a couple minutes before your flow shows up in your copilot. If it doesn’t show up after five minutes, follow [our troubleshooting guides](https://developer.moveworks.com/creator-studio/troubleshooting/support) to further debug.

# Congratulations!

You just added Perplexity Online Search results to your Copilot! Check out our other guides for inspiration on what to build next.
---
name: Rename Slack Channel
description: Add a use case to your copilot that can rename a Slack channel.
design_pattern_id: 20
systems: [ workato, slack ]
purple_chat_link: https://developer.moveworks.com/creator-studio/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22mocks%22%3A%5B%7B%22id%22%3A1636%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%2C%22botName%22%3A%22%22%2C%22botImageUrl%22%3A%22%22%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22%3Cp%3EI+want+to+change+the+name+of+a+slack+channel%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Cp%3EWhich+slack+channel+do+you+want+to+change%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22%3Cp%3E%23prospect-visa%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Cp%3EWhat+is+the+new+channel+name%3F%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22%3Cp%3E%23customer-visa%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22%3Cp%3EInbound+Request+to+Middleware%3A%3Cbr%3E%3Cbr%3E%7B%3Cbr%3E%5C%22old_name%5C%22%3A+%5C%22prospect-visa%5C%22%2C%3Cbr%3E%5C%22new_name%5C%22%3A+%5C%22customer-visa%5C%22%2C%3Cbr%3E%7D%3Cbr%3E%3Cbr%3EProcess%3A%3Cbr%3E1.+Find+the+existing+channel+in+Slack%3Cbr%3E2.+Verify+the+channel+is+allowed+to+be+changed+%28not+a+special+channel%29%3Cbr%3E3.+Update+the+channel%3Cbr%3E%3Cbr%3EOutbound+Response%3A%3Cbr%3E%7B+%5C%22status%5C%22%3A+%5C%22ok%5C%22+%7D%2C+200%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Cp%3EThanks.+I%27ve+changed+the+channel+name.%3Cbr%3E%3C%2Fp%3E%22%7D%5D%7D%7D%5D%2C%22botSettings%22%3A%7B%22name%22%3A%22%22%2C%22imageUrl%22%3A%22%22%7D%7D
difficulty_level: Intermediate
time_in_minutes: 60
---

# Introduction

Slack is a collaboration platform that allows you to create various channels for different topics. However, there might be occasions when your users want to rename some channels, but these need to be restricted only to certain channels (e.g. no one should be able to rename “general”)

In this tutorial, we will explore how to integrate Creator Studio with Slack for channel renaming.

Let's get started!

# What are we building?

## Conversation Design

[This purple chat](https://developer.moveworks.com/creator-studio/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22mocks%22%3A%5B%7B%22id%22%3A1636%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%2C%22botName%22%3A%22%22%2C%22botImageUrl%22%3A%22%22%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22%3Cp%3EI+want+to+change+the+name+of+a+slack+channel%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Cp%3EWhich+slack+channel+do+you+want+to+change%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22%3Cp%3E%23prospect-visa%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Cp%3EWhat+is+the+new+channel+name%3F%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22%3Cp%3E%23customer-visa%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22%3Cp%3EInbound+Request+to+Middleware%3A%3Cbr%3E%3Cbr%3E%7B%3Cbr%3E%5C%22old_name%5C%22%3A+%5C%22prospect-visa%5C%22%2C%3Cbr%3E%5C%22new_name%5C%22%3A+%5C%22customer-visa%5C%22%2C%3Cbr%3E%7D%3Cbr%3E%3Cbr%3EProcess%3A%3Cbr%3E1.+Find+the+existing+channel+in+Slack%3Cbr%3E2.+Verify+the+channel+is+allowed+to+be+changed+%28not+a+special+channel%29%3Cbr%3E3.+Update+the+channel%3Cbr%3E%3Cbr%3EOutbound+Response%3A%3Cbr%3E%7B+%5C%22status%5C%22%3A+%5C%22ok%5C%22+%7D%2C+200%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Cp%3EThanks.+I%27ve+changed+the+channel+name.%3Cbr%3E%3C%2Fp%3E%22%7D%5D%7D%7D%5D%2C%22botSettings%22%3A%7B%22name%22%3A%22%22%2C%22imageUrl%22%3A%22%22%7D%7D) shows the experience we are going to build.

This use case is made up of:

- Triggers:
    1. Natural Language
- Slots:
    1. An existing Slack channel name
    2. A new Slack channel name
- Actions
    1. Rename a channel
- Guidelines
    1. None

Based on the needs of this use case, we should build a [ID-Based Action Path](https://developer.moveworks.com/creator-studio/resources/design-pattern?id=id-based-action-path).

## API Research

There’s only 1 API needed to build this use case

### API #1: Rename a channel

Since we want to integrate with Slack Channels, we should look into their Web APIs. For this use case, it seems we will need two APIs:

![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled.png)

1. **[List Conversations API](https://api.slack.com/methods/conversations.list):** An API to list channels in the workspace
2. **[Rename Conversation API](https://api.slack.com/methods/conversations.rename):** An API to rename a channel given its ID

Both these APIs are hosted on the Slack Web API and should be authenticated with a bearer token. You can follow our [Authentication Guide: Slack API](../../authentication-guides/slack/README.md) to create an API key with the right privileges.

# Prerequisites

- Access to the Slack Web APIs (follow [our guide](../../authentication-guides/slack/README.md))
- An Workato APIM Endpoint (follow [our guide](../../authentication-guides/workato/README.md))
- Postman

# Walkthrough

## Step 1: Build the “Rename Channel” API

### Setup Trigger

1. Open your Workato Recipe. If you don’t have it handy, [follow our guide](../../authentication-guides/workato/README.md).
2. Add a Request JSON Schema
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%201.png)
    
3. Add a Response JSON Schema for successes
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%202.png)
    
4. Add a Response JSON Schema for failures
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%203.png)
    

### Validate Channel Name

1. Add an `IF condition`
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%204.png)
    
2. Configure the condition to match cases where the `old_name` is one of the protected channels (e.g. `general`, or `random`)
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%205.png)
    
3. Add an error response
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%206.png)
    

### Find Channel ID

1. Connect to your Slack environment
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%207.png)
    
2. Choose the `Custom Action`
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%208.png)
    
3. Select your connection, or set up a new one to Slack
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%209.png)
    
4. Setup the `conversations.list` endpoint
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%2010.png)
    
5. It should return a list of channels to Workato
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%2011.png)
    
6. Use [Workato Formulas](https://docs.workato.com/formulas/array-list-formulas.html#first) for lists to extract the ID of the channel that matches `old_name`
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%2012.png)
    
7. Add an `IF condition` for if no `Target Channel ID` was found
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%2013.png)
    
8. Return an error message if the channel isn’t found
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%2014.png)
    

### Rename Channel

1. Add another Custom Slack Action for the `conversations.rename` endpoint
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%2015.png)
    
2. Send it a sample channel ID & channel name
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%2016.png)
    
3. Swap out the example values for your data pills
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%2017.png)
    
4. Return a success message
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%2018.png)
    

### Validate & Deploy API

You can follow our [system guide on Workato APIM](../../authentication-guides/workato/README.md) to test & deploy your recipe. You should make sure that:

1. Protected channels return an error
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%2019.png)
    
2. If a channel does not exist, the action fails
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%2020.png)
    
3. The API success if everything is valid
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%2021.png)
    
4. The channel name updates appropriately
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%2022.png)
    

## Step 2: Build in Creator Studio

### Setup use case

1. Start in the Paths Workspace
2. Title your use case: Rename Slack Channel

### Build the conversation design

1. Start with a text slot for the old name
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%2023.png)
    
2. Collect a text slot for the new name
    
    ![Untitled](Use%20Case%20Guide%20Rename%20Slack%20Channel%20da6e0d8cf5774fc397343685a5998988/Untitled%2024.png)
    
3. Add an API Action to execute your Workato Recipe.
    - Connector: Follow our [Workato APIM guide](../../authentication-guides/workato/README.md).
    - Path: `/mw/ajay-merchia-vv1/rename-channel`
    - Method: `POST`
    - Headers:
        
        
        | Key | Value |
        | --- | --- |
        | Content-Type | application/json |
    - Request Body:
        
        ```python
        {
        	"old_name": "{{previous channel name}}",
        	"new_name": "{{name of new channel}}"
        }
        ```
        
    - Action Description: `Renames the Slack Channel`

### Build your generative intent & launch the use case

Build a [Generative Intent](https://developer.moveworks.com/creator-studio/paths/generative-intents/) and then use our [Launch Rules](https://developer.moveworks.com/creator-studio/launch-options/) to launch your use case to your Copilot. 

## Step 3: See it in action!

Trigger the use case by asking for it from your Copilot. [Here’s a quick demo](https://www.youtube.com/watch?v=RfXXLWsqzE4).

# Congratulations!

You just added Slack Channel Renames to your Copilot! Say good-bye to those IT tickets. Check out our other guides for inspiration on what to build next.
---
design_pattern_id: 28
name: Salesforce Account Lookup
description: Lookup Account object details from Salesforce with your bot
systems: [salesforce]
purple_chat_link: https://developer.moveworks.com/creator-studio/developer-tools/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22botSettings%22%3A%7B%7D%2C%22mocks%22%3A%5B%7B%22id%22%3A8491%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22What+is+the+Renewal+date+for+ACME%3F%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22Query+Salesforce+Accounts+API+endpoint%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22The+renewal+date+for+ACME+is+on+February+25%2C+2026%22%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22Perfect%2C+thanks%21%22%7D%5D%7D%7D%5D%7D
time_in_minutes: 5
difficulty_level: Beginner
---

### Step : See it in action

<aside>
✨ Query Salesforce Account object details with your bot

</aside>

# Introduction

Salesforce allows you to manage the entire lifecycle of a customer relationship, from a prospect to a newly closed customer through multiple renewals. However, retrieving specific details of a customer’s account might take some time since you will need to you to login to the Salesforce portal and then navigate to the correct account before you can check on any such information.

In this tutorial, we will guide you through building an plugin on Creator Studio that simplifies this process and help you to swiftly pull up detailed information through a simple conversational query with your Moveworks’ bot.

Let's get started!

# Prerequisites

- [Postman](https://www.postman.com/) or an API Testing Tool
- Salesforce Connector built in Creator Studio (follow [our guide](https://developer.moveworks.com/creator-studio/resources/authentication-guide?id=salesforce))

# What are we building?

## Conversation Design

[This purple chat](https://developer.moveworks.com/creator-studio/developer-tools/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22botSettings%22%3A%7B%7D%2C%22mocks%22%3A%5B%7B%22id%22%3A8491%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22What+is+the+Renewal+date+for+ACME%3F%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22Query+Salesforce+Accounts+API+endpoint%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22The+renewal+date+for+ACME+is+on+February+25%2C+2026%22%7D%2C%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22Perfect%2C+thanks%21%22%7D%5D%7D%7D%5D%7D) shows the experience we are going to build.

## Creator Studio Components

- **Triggers:**
    1. Natural Language
- **Slots**:
    1. Name of the Salesforce Account
- **Actions:**
    1. Query Customer Account details
- **Guidelines:**
    1. None

Based on the needs of this use case, we should build a [Lookup Single Record by ID / Keyword](https://developer.moveworks.com/creator-studio/design-patterns/dp-6/)**.**

## API Research

There’s only 1 API needed to build this use case

### API #1: Account Lookups

Since we want to integrate with Salesforce, we should look into their SOQL Query APIs. For this use case, we will need only 1 API call.

![Untitled](Use%20Case%20Tutorial%20Salesforce%20Account%20Lookup%200b5238e472eb4113bbc51e0a65fa3e08/Untitled.png)

1. [Salesforce SOQL Query API](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_query.htm): An API for Salesforce to execute the specified SOQL Query. Here, our query would be related to the `Account` object
    1. Sample SOQL Query API: Here is an example of a sample query API using a SOQL query on the `Account` object.

        ```bash
        curl --location --globoff 'https://{{your-salesforce-instance}}.my.salesforce.com/services/data/v58.0/query?q=SELECT%20Name%2CType%2CDescription%2CId%2CWebsite%2COwner.Name%20FROM%20Account%20WHERE%20Name%20LIKE%20%27{{query}}%27' \
        --header 'Authorization: Bearer {{generated_bearer_token}}'
        ```

        The Query we used here is:

        ```sql
        SELECT
         Name,
         Type,
         Description,
         Id,
         Website,
         Owner.Name
        FROM
         Account
        WHERE
         Name LIKE '%25{{query}}%25'
        ```

        Use this Query to fetch all relevant details from your customer’s Salesforce account by replacing the `{{query}}` field with the name of the customer you’re trying to lookup for. The `%25` searches for the Account inside account names, instead of an exact keyword match (Example: matching `Acme` with "Acme Inc." and "Acme Semiconductors", instead of matching no results.

> In the above example, we have used only Standard Salesforce objects, however, you can also use the [Custom](https://help.salesforce.com/s/articleView?id=sf.basics_object_types.htm&type=5) objects that is defined in your Salesforce instance to build the Query. Custom objects can be identified by the trailing `__c` after their name.
You can visit [`https://workbench.developerforce.com/`](https://workbench.developerforce.com/) and explore the different fields present within the `Account` object. You can also try out different SOQL queries and use the one which you think is a best fit for the Use Case.
>
>
> ![Untitled](Use%20Case%20Tutorial%20Salesforce%20Account%20Lookup%200b5238e472eb4113bbc51e0a65fa3e08/Untitled%201.png)
>

# Steps

## Step 1: Build in Creator Studio

### Setup use case

1. Start in the Queries Workspace and create a new query.
2. Provide the Basic Info so the Next Gen Copilot knows how to use this plugin:
    1. **Query Label**: `Lookup Customer Account Details`
    2. **Short Description:** `Lookup Customer Account Details. This includes looking up any information regarding the description, owner, the website of the customer, and more.`

### Setup the API

1. Select the Salesforce connector that you set up earlier in the Authentication Guide

    ![Untitled](Use%20Case%20Tutorial%20Salesforce%20Account%20Lookup%200b5238e472eb4113bbc51e0a65fa3e08/Untitled%202.png)

1. Define your API action for querying the Accounts data from Salesforce:
    - Path: `/services/data/v58.0/query`
    - Method: `GET`
    - Query parameters:

        | KEY | VALUE |
        | --- | --- |
        | q | `SELECT Name, Type, Description, Id, Website, Owner.Name FROM Account WHERE Name LIKE '{{query}}'` |
    - Provide an example value for the `{{query}}` field based on any customer account you know. If you don’t have any of your customer’s name handy, please check `Accounts` section within your Salesforce instance to get the exact name of any of the customer accounts present there. For example:

        ![Untitled](Use%20Case%20Tutorial%20Salesforce%20Account%20Lookup%200b5238e472eb4113bbc51e0a65fa3e08/Untitled%203.png)

1. Test your setup in Creator Studio and look for a successful execution. A 200 Response Code represents that the API was successfully executed.

    ![Untitled](Use%20Case%20Tutorial%20Salesforce%20Account%20Lookup%200b5238e472eb4113bbc51e0a65fa3e08/Untitled%204.png)

### Label the API Response

1. Select the `Name` as the Identifier.
2. Select any of the fields as the Description. In this example, we have selected `Website` as the Description.
3. From among the Additional Fields, select the fields that you want users to query on and label them accordingly. For example, the field `Owner` contains the name of the Owner of a customer Account and we want the bot to pick up the abbreviation name of the Owner and map it to this field. Therefore, the Label should be something like - `Owner Name`

    ![Untitled](Use%20Case%20Tutorial%20Salesforce%20Account%20Lookup%200b5238e472eb4113bbc51e0a65fa3e08/Untitled%205.png)

4. No follow-up action needed.

### Setup your Generative Intent

1. Since we want to capture the name of the customer from the utterance, which is further used to filter the SOQL Query, we will need to utilize smart extraction on the natural language slot. To do this, we need to provide the name of the customer that will be present in the `User utterance example` field in the `Keyword` field as well for every example.

    ![Untitled](Use%20Case%20Tutorial%20Salesforce%20Account%20Lookup%200b5238e472eb4113bbc51e0a65fa3e08/Untitled%206.png)

We want to provide different kinds of utterances here based on the Accounts Lookup use case and the various fields present within the Accounts object within your Salesforce instance. Here are some examples you can use:

1. What is the description of ACME?
2. What is the website of Teamboost?
3. What is the SFDC Url for ChatBoost?
4. What information is available for ACME?

### Launch the use case

Use our [Launch Rules](https://developer.moveworks.com/creator-studio/launch-options/) to launch your use case to your Copilot.

## Step 2: See it in action

Trigger the use case by asking for it from your Copilot. Find interesting ways to combine it with your own enterprise data.

Note: It could take a couple minutes before your flow shows up in your copilot. If it doesn’t show up after five minutes, follow [our troubleshooting guides](https://developer.moveworks.com/creator-studio/troubleshooting/support) to further debug.

# Congratulations

You just added Salesforce Account Lookups to your Copilot! Check out our other guides for inspiration on what to build next.
---
design_pattern_id: 28
name: Sharepoint List Filtering
description: Filters a Sharepoint List by a single attribute.
systems: ["microsoft-graph-api"]
purple_chat_link: https://developer.moveworks.com/creator-studio/developer-tools/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22mocks%22%3A%5B%7B%22id%22%3A750%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%2C%22botName%22%3A%22%22%2C%22botImageUrl%22%3A%22%22%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22%3Cp%3ECan+you+show+me+Critical+priority+customer+feedback%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22%3Cp%3EMoveworks+extracts+%5C%22Critical%5C%22+from+natural+language%3A%3Cbr%3E%3Cbr%3EInbound+Request+to+Middleware%3A%3Cbr%3E%3Cbr%3E%7B%3Cbr%3E%5C%22%24filter%5C%22%3A+%5C%22fields%2FPriority+eq+%27Critical%27%5C%22%3Cbr%3E%7D%3Cbr%3E%3Cbr%3EProcess%3A%3Cbr%3E1.+Establish+a+connection+to+Sharepoint+List+over+Graph+API%3Cbr%3E2.+Retrieve+items+matching+the+filter+in+the+Sharepoint+List%3Cbr%3E%3Cbr%3EOutbound+Response%3A%3Cbr%3E%7B%3Cbr%3E%5C%22value%5C%22%3A+%5B%3Cbr%3E++%7B+Item1+%7D%2C%3Cbr%3E++%7B+Item2+%7D%2C%3Cbr%3E++...%3Cbr%3E%5D%3Cbr%3E%7D%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Ci%3EOne+moment%2C+fetching+your+results.+This+may+take+%7E10+seconds%3C%2Fi%3E%5Cn%22%2C%22cards%22%3A%5B%7B%22title%22%3A%22%3Cp%3E%3Cb%3EAccount+Login+Failure%3C%2Fb%3E%3A+New%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22title%22%3A%22%3Cp%3E%3Cb%3EWeb+Loading+Issue%3C%2Fb%3E%3A+In+Progress%3Cbr%3E%3C%2Fp%3E%22%7D%5D%7D%5D%7D%7D%5D%2C%22botSettings%22%3A%7B%22name%22%3A%22%22%2C%22imageUrl%22%3A%22%22%7D%7D
time_in_minutes: 30
difficulty_level: Intermediate
---


# Introduction

[Sharepoint Lists](https://support.microsoft.com/en-us/office/introduction-to-lists-0a1c3ace-def0-44af-b225-cfa8d92c52d7) let you create collections of data that you can share with team members in your Sharepoint instance

In this tutorial, we will demonstrate how to filter a Sharepoint List on a single attribute through Creator Studio.

Let's get started!

# What are we building?

## Conversation Design

[This purple chat](https://developer.moveworks.com/creator-studio/developer-tools/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22mocks%22%3A%5B%7B%22id%22%3A750%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%2C%22botName%22%3A%22%22%2C%22botImageUrl%22%3A%22%22%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22%3Cp%3ECan+you+show+me+Critical+priority+customer+feedback%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22%3Cp%3EMoveworks+extracts+%5C%22Critical%5C%22+from+natural+language%3A%3Cbr%3E%3Cbr%3EInbound+Request+to+Middleware%3A%3Cbr%3E%3Cbr%3E%7B%3Cbr%3E%5C%22%24filter%5C%22%3A+%5C%22fields%2FPriority+eq+%27Critical%27%5C%22%3Cbr%3E%7D%3Cbr%3E%3Cbr%3EProcess%3A%3Cbr%3E1.+Establish+a+connection+to+Sharepoint+List+over+Graph+API%3Cbr%3E2.+Retrieve+items+matching+the+filter+in+the+Sharepoint+List%3Cbr%3E%3Cbr%3EOutbound+Response%3A%3Cbr%3E%7B%3Cbr%3E%5C%22value%5C%22%3A+%5B%3Cbr%3E++%7B+Item1+%7D%2C%3Cbr%3E++%7B+Item2+%7D%2C%3Cbr%3E++...%3Cbr%3E%5D%3Cbr%3E%7D%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Ci%3EOne+moment%2C+fetching+your+results.+This+may+take+%7E10+seconds%3C%2Fi%3E%5Cn%22%2C%22cards%22%3A%5B%7B%22title%22%3A%22%3Cp%3E%3Cb%3EAccount+Login+Failure%3C%2Fb%3E%3A+New%3Cbr%3E%3C%2Fp%3E%22%7D%2C%7B%22title%22%3A%22%3Cp%3E%3Cb%3EWeb+Loading+Issue%3C%2Fb%3E%3A+In+Progress%3Cbr%3E%3C%2Fp%3E%22%7D%5D%7D%5D%7D%7D%5D%2C%22botSettings%22%3A%7B%22name%22%3A%22%22%2C%22imageUrl%22%3A%22%22%7D%7D) shows the experience we are going to build.


## Creator Studio Components

- Triggers:
    1. Natural language
- Slots:
    1. A priority level to filter on (exact match)
- Actions
    1. Retrieve Sharepoint List Results
- Guidelines
    1. None

Based on the needs of this use case, we should build a **Filter by ID Query**.

## API Research

There's only 1 API needed to build this use case. We can use the [Enumerate Items in List](https://learn.microsoft.com/en-us/graph/api/listitem-list?view=graph-rest-1.0&tabs=http) endpoint on the Graph API to return Sharepoint items matching a filter.

# Prerequisites

- A Microsoft Graph Connection (follow [our guide](https://developer.moveworks.com/creator-studio/resources/authentication-guide?id=microsoft-graph-api)). Make sure you request the `Sites.Read.All` permission for this use case.

# Steps

## Step 1: Get your IDs

To build this use case, there are a few IDs you need handy:

### Your Site ID

The list I'm trying to analzye can be found at `https://deepnets.sharepoint.com/sites/CustomerFeedback/Lists/Issue%20tracker/AllItems.aspx`. Based on that link, I know that my...

1. `domain_url` is `deepnets.sharepoint.com`
2. `site_name` is `CustomerFeedback`

I can head to the [Graph API Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer?request=sites%2F%7B%7Bdomain_url%7D%7D%3A%2Fsites%2F%7B%7Bsite_name%7D%7D&method=GET&version=v1.0&GraphUrl=https://graph.microsoft.com), replace the values, and `Run Query`.

![alt text](./images/image-10.png)

In the API response, there is a `site_id` that I can use going forward

### Your List ID

Go to your list in Sharepoint and click the gear in the top right. Then select `List Settings`

![alt text](./images/image-9.png)

You'll be redirected to a URL like

`https://deepnets.sharepoint.com/sites/CustomerFeedback/_layouts/15/listedit.aspx?List=%7B7144e89f-7793-4faf-a3f8-d81f9255cdad%7D`

From this link, our `list_id` is `7144e89f-7793-4faf-a3f8-d81f9255cdad`. You can also get this list ID from the [Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer?request=sites%2F%7B%7Bsite_id%7D%7D%2Flists&method=GET&version=v1.0&GraphUrl=https://graph.microsoft.com)

## Step 2: Build in Creator Studio

### Setup use case

1. Start in the Queries Workspace and create a new query that describes the list you're filtering as well as how you're filtering it.

    ![Basic Info](./images/image-5.png)

### Setup the API

1. Select the [Microsoft Graph integration](https://developer.moveworks.com/creator-studio/resources/authentication-guide?id=microsoft-graph-api) you set up earlier

    ![Select Connector](./images/image-1.png)

2. Define your API action for filtering from the list

    ![API Setup](./images/image-2.png)

    ```bash
    curl --location 'https://graph.microsoft.com/v1.0/sites/{{site_id}}/lists/{{list_id}}/items?%24expand=fields&%24filter=fields%2F{{FieldName}}%20eq%20%27{{query}}%27' \
    --header 'Prefer: HonorNonIndexedQueriesWarningMayFailRandomly'
    ```

    - Path: `/v1.0/sites/{{site_id}}/lists/{{list_id}}/items`
    - Method: `GET`
    - Headers: 

        | Key | Value |
        | --- | --- |
        | Prefer | HonorNonIndexedQueriesWarningMayFailRandomly |

You need the `Prefer` header if you're filtering on a non-indexed column, or [add the column to an index](https://support.microsoft.com/en-us/office/add-an-index-to-a-list-or-library-column-f3f00554-b7dc-44d1-a2ed-d477eac463b0).

    - Query parameters:

        | Key | Value |
        | --- | --- |
        | $expand | fields |
        | $filter | fields/{{FieldName}} eq '{{query}}' |

You can customize the filtering, sorting, and selection further using the [OData Standard](https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/use-odata-query-operations-in-sharepoint-rest-requests) for Sharepoint Lists.

3. Test your setup and look for a successful execution.

### Label the API Response

You can select whichever fields you want in your citation card.

![API Labeling](./images/image-3.png)

### Setup your Generative Intent

Provide a few examples that extract a variety of valid filter values. Here, I'm extracting "High," "Critical," and "Low" to make sure the API call succeeds.

![Triggering](./images/image-4.png)

### Launch the use case

Use our [Launch Rules](https://developer.moveworks.com/creator-studio/launch-options/) to launch your use case to your copilot.

## Step 3: See it in action!

Head over to your copilot and ask some questions about your list. Here’s [a quick demo](https://www.loom.com/share/9cf574ec0953455d8b2eb07ba5639814).

# Congratulations

You just added a Sharepoint List to your Copilot! Your organization likely has dozens of these, so go ahead and set another one up!
---
design_pattern_id: 12
name: Lookup upcoming birthdays
description: Uses the Workday reporting engine to fetch any upcoming birthdays
systems: [workday]
purple_chat_link: https://developer.moveworks.com/creator-studio/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22botSettings%22%3A%7B%7D%2C%22mocks%22%3A%5B%7B%22id%22%3A7525%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22Can+you+tell+me+of+any+upcoming+birthdadys%3F%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22%3Cp%3EGET+call+to+WorkDay+RaaS+report+for+upcoming+birthdays%3Cbr%3E%3Cbr%3EResponse%3A%3Cbr%3E%7B%3Cbr%3E%5Ct%5C%22Report_Entry%5C%22%3A+%5B%3Cbr%3E%5Ct%5Ct%7B%3Cbr%3E%5Ct%5Ct%5Ct%5C%22Next_Birthday%5C%22%3A+%5C%222024-01-17%5C%22%2C%3Cbr%3E%5Ct%5Ct%5Ct%5C%22Worker%5C%22%3A+%5C%22Emma+Hobson%5C%22%3Cbr%3E%5Ct%5Ct%7D%2C%3Cbr%3E%5Ct%5Ct%7B%3Cbr%3E%5Ct%5Ct%5Ct%5C%22Next_Birthday%5C%22%3A+%5C%222024-01-17%5C%22%2C%3Cbr%3E%5Ct%5Ct%5Ct%5C%22Worker%5C%22%3A+%5C%22Enrique+Vasquez%5C%22%3Cbr%3E%5Ct%5Ct%7D%2C%3Cbr%3E%5Ct%5Ct%7B%3Cbr%3E%5Ct%5Ct%5Ct%5C%22Next_Birthday%5C%22%3A+%5C%222024-01-18%5C%22%2C%3Cbr%3E%5Ct%5Ct%5Ct%5C%22Worker%5C%22%3A+%5C%22Min-gyu+Kang+%EF%BC%88%EA%B0%95%EB%AF%BC%EA%B7%9C%EF%BC%89%5C%22%3Cbr%3E%5Ct%5Ct%7D%2C%3Cbr%3E%5Ct%5Ct%7B%3Cbr%3E%5Ct%5Ct%5Ct%5C%22Next_Birthday%5C%22%3A+%5C%222024-01-19%5C%22%2C%3Cbr%3E%5Ct%5Ct%5Ct%5C%22Worker%5C%22%3A+%5C%22Maximilian+Schneider%5C%22%3Cbr%3E%5Ct%5Ct%7D%3Cbr%3E%5Ct%5D%3Cbr%3E%7D%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Cp%3ESure%2C+here+are+some+upcoming+birthdays%3A%3Cbr%3E%3Cbr%3E-+Emma+Hobson%27s+birthday+is+on+January+17th+%3Cbr%3E-+Enrique+Vasquez%27s+birthday+is+also+on+January+17th+%3Cbr%3E-+Min-gyu+Kang%27s+birthday+is+on+January+18th+%3Cbr%3E-+Maximilian+Schneider%27s+birthday+is+on+January+19th+%3Cbr%3E%3Cbr%3ELet+me+know+if+you+need+information+on+more+birthdays.%3C%2Fp%3E%22%7D%5D%7D%7D%5D%7D
time_in_minutes: 10
difficulty_level: Beginner
---

# **Introduction**

Workday's Reports-as-a-Service (RaaS) is a powerful feature that revolutionizes data access and integration in the Workday ecosystem. By allowing custom reports to be exposed as web services, RaaS facilitates seamless data interactions with external systems. 

By bringing these reports into Creator Studio, we can add a conversational interface to them, making it easier than ever for your users to get access to the data that lies within Workday.

In this tutorial, we will explore how to call RaaS from Creator Studio. To guide us, we will be using a pre-built report that gets the upcoming birthdays.

Let's get started!

# What are we building?

## Conversation Design

[This purple chat](https://developer.moveworks.com/creator-studio/purple-chat-builder/?workspace=%7B%22title%22%3A%22My+Workspace%22%2C%22botSettings%22%3A%7B%7D%2C%22mocks%22%3A%5B%7B%22id%22%3A7525%2C%22title%22%3A%22Mock+1%22%2C%22transcript%22%3A%7B%22settings%22%3A%7B%22colorStyle%22%3A%22LIGHT%22%2C%22startTime%22%3A%2211%3A43+AM%22%2C%22defaultPerson%22%3A%22GWEN%22%2C%22editable%22%3Atrue%7D%2C%22messages%22%3A%5B%7B%22from%22%3A%22USER%22%2C%22text%22%3A%22Can+you+tell+me+of+any+upcoming+birthdadys%3F%22%7D%2C%7B%22from%22%3A%22ANNOTATION%22%2C%22text%22%3A%22%3Cp%3EGET+call+to+WorkDay+RaaS+report+for+upcoming+birthdays%3Cbr%3E%3Cbr%3EResponse%3A%3Cbr%3E%7B%3Cbr%3E%5Ct%5C%22Report_Entry%5C%22%3A+%5B%3Cbr%3E%5Ct%5Ct%7B%3Cbr%3E%5Ct%5Ct%5Ct%5C%22Next_Birthday%5C%22%3A+%5C%222024-01-17%5C%22%2C%3Cbr%3E%5Ct%5Ct%5Ct%5C%22Worker%5C%22%3A+%5C%22Emma+Hobson%5C%22%3Cbr%3E%5Ct%5Ct%7D%2C%3Cbr%3E%5Ct%5Ct%7B%3Cbr%3E%5Ct%5Ct%5Ct%5C%22Next_Birthday%5C%22%3A+%5C%222024-01-17%5C%22%2C%3Cbr%3E%5Ct%5Ct%5Ct%5C%22Worker%5C%22%3A+%5C%22Enrique+Vasquez%5C%22%3Cbr%3E%5Ct%5Ct%7D%2C%3Cbr%3E%5Ct%5Ct%7B%3Cbr%3E%5Ct%5Ct%5Ct%5C%22Next_Birthday%5C%22%3A+%5C%222024-01-18%5C%22%2C%3Cbr%3E%5Ct%5Ct%5Ct%5C%22Worker%5C%22%3A+%5C%22Min-gyu+Kang+%EF%BC%88%EA%B0%95%EB%AF%BC%EA%B7%9C%EF%BC%89%5C%22%3Cbr%3E%5Ct%5Ct%7D%2C%3Cbr%3E%5Ct%5Ct%7B%3Cbr%3E%5Ct%5Ct%5Ct%5C%22Next_Birthday%5C%22%3A+%5C%222024-01-19%5C%22%2C%3Cbr%3E%5Ct%5Ct%5Ct%5C%22Worker%5C%22%3A+%5C%22Maximilian+Schneider%5C%22%3Cbr%3E%5Ct%5Ct%7D%3Cbr%3E%5Ct%5D%3Cbr%3E%7D%3C%2Fp%3E%22%7D%2C%7B%22from%22%3A%22BOT%22%2C%22text%22%3A%22%3Cp%3ESure%2C+here+are+some+upcoming+birthdays%3A%3Cbr%3E%3Cbr%3E-+Emma+Hobson%27s+birthday+is+on+January+17th+%3Cbr%3E-+Enrique+Vasquez%27s+birthday+is+also+on+January+17th+%3Cbr%3E-+Min-gyu+Kang%27s+birthday+is+on+January+18th+%3Cbr%3E-+Maximilian+Schneider%27s+birthday+is+on+January+19th+%3Cbr%3E%3Cbr%3ELet+me+know+if+you+need+information+on+more+birthdays.%3C%2Fp%3E%22%7D%5D%7D%7D%5D%7D) shows the experience we are going to build.

**This use case is made up of:**

✨ **Triggers:** Natural Language

🤲 **Slots**: None

🏃‍♂️ **Actions:** Retrieve data from workday report

📜 **Response Data:** The data from a RaaS report

📚 **Guidelines:** Select fields to render from RaaS report

Based on the needs of this use case, we should build a [Static Query](https://developer.moveworks.com/creator-studio/resources/design-pattern?id=static-query)

## API Design

There’s only 1 API needed to build this use case.

### API #1: Get RaaS Report

Since we want to get a RaaS report, we only need to reference the report in our API call and get the results from the report to display within Creator Studio.

# **Prerequisites**

- A connection to Workday, [follow our guide.](https://developer.moveworks.com/creator-studio/resources/authentication-guide?id=workday)
- A user login to Workday.

# **Walkthrough**

## **Step 1: Get the URL for the Report**

In this step, we will get the URL for the report we want to run within Creator Studio. We are using a pre-made report as part of this example but you can call any report that already exists or that you create using these steps.

We are going to use the *Alert - Birthdays for this week and next* report to get the upcoming birthdays for this example.

1. Login to Workday and search for “All Custom Reports” in the search bar.
    
    ![Search for all custom reports in workday](images/Untitled.png)
    
2. Filter *Custom Report Name* by “Birthday”.
3. Check the box next to “Alert - Birthdays for this week and next” and filter.
    
    ![choose the "Alert - birthdays for this week and next"](images/Untitled%201.png)
    
4. Click on the link for “Alert - Birthdays for this week and next”.
    
    ![shows the report from the search results](images/Untitled%202.png)
    
5. From the ellipse drop-down, go to *Web Service → View URLs.*
    
    ![the ellipse for the report to show custom actions](images/Untitled%203.png)
    
6. You will get a dialogue to sign in, press cancel and copy the URL after *[wd2-impl-services1.workday.com](http://wd2-impl-services1.workday.com)* 
    
    ![browser window showing url](images/Untitled%204.png)
    
    which should look something like this: `/ccx/service/customreport2/[your_tenant]/[your user_name]/Alert_-_Birthdays_for_this_week_and_next`
    

    
    **Note**: Don’t copy the *format* parameter on the end, we will put this in manually within Creator Studio. Your report may have other parameters as well if you have chosen one that takes inputs. Make note of these parameters and the format so you can call them in the next step.
    

## **Step 2: Build in Creator Studio**

We will now go into Creator Studio to create the query. You can follow [our guides](https://developer.moveworks.com/creator-studio/quickstart/queries/) for more complex setup however we will go into the specific areas of note for our sample report in the following.

1. Under Queries, click *CREATE* to create a new query.
    
    ![create button highlighted in creator studio queries page](images/Untitled%205.png)
    
2. Give it a name and description.
    
    ![basic info page of creating a query in creator studio](images/Untitled%206.png)
    
    **Note:** The description will be part of how Moveworks finds the query when a user is searching so try to use a description that makes sense.
    
    Click *Next.*
    
3. Choose the connector you created previously, [follow our guide](https://developer.moveworks.com/creator-studio/resources/authentication-guide?id=workday) if you haven’t already done so.
    
    ![choose a system with workday as the chosen system](images/Untitled%207.png)
    
    Click *Next*
    
4. Paste the URL you copied earlier and add any parameter(s) from earlier under *Query parameters*. In this example report, we only had one parameter - *format -* which had a value of “rss”. “rss” isn’t a format we support but “json” is, so we will use this in place.
    
    ![api connection parameters ](images/Untitled%208.png)
    
    Click *Next.*
    
5. Click *Test* to test the report call to ensure this will work as expected, you should see something similar to the following:
    
    ![additional query parameters for api connection](images/Untitled%209.png)
    
    Click *Next.*
    
6. Now we will choose the values of the json that we want to display when running this query. In this example, we only have two return values so our setup is quite simple however you can follow [our guides](https://developer.moveworks.com/creator-studio/quickstart/queries/) if your example is more complex and you want to understand the nuances of this screen.
    
    ![choose fields to return to the copilot](images/Untitled%2010.png)
    
    Click *Next.*
    
7. We have no follow up actions so just click *Next.*
    
    ![follow up actions is empty](images/Untitled%2011.png)
    
8. Fill in your sample utterances so we understand how we want to call this. I put in three:
    - What are the upcoming birthdays?
    - Who has the next birthday?
    - When is the next birthday in workday?
    
    ![utterances to trigger](images/Untitled%2012.png)
    
    Click *Next.*
    
9. From a testing perspective, you may want to launch to yourself first or you can launch to all users. Don’t forget to click the checkbox!
    
    ![launch screen showing launch to all users](images/Untitled%2013.png)
    
    Click *Launch.*
    

## Step 3: See it in action!

Trigger the use case by asking for it from your Copilot. 

![real image of copilot in action showing the query and upcoming birthdays](images/Untitled%2014.png)

# Congratulations!

Without having to write a line of code, you just added a RaaS report to query Workday from within your copilot! Now you might want to look at some of your other reports to apply what you have learned and pull even more data and use cases.
