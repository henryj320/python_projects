# react_dashboard
Last update: 2023-01-12 23:08
<br><br>

## Changelog for react_dashboard

1. Created the project and README.

Following the tutorial [here](https://reactjs.org/docs/create-a-new-react-app.html):

2. Checking whether NPX (Package runner that comes with npm) or NPM are installed.
    - ` npm `
    - ` npx `
    - Neither are installed. 
3. Downloading the latest version of NodeJS 18.13.0 LTS.
    - ` sudo snap install node --classic `
4. Checking whether NPX and XPM are installed. Yep!
5. ` cd Git_Repos/python_projects/react_dashboard/initial_learning_react_app/ `
6. Creating the app.
    - ` npx create-react-app first_app `
    - Taking a while. Created 97 MB of files.
        - 96 MB of it are in node_modules
7. Running the app.
    - ` npm start `
    - Error: Could not find *package.json*.
    - ` cd first_app `
    - ` npm start `
    - Working fine! Sweet. Running at http://localhost:3000/.
8. Deciding a template from [here](https://www.creative-tim.com/templates/react-free?page=1)
    - Best is Material Dashboard 2 - [here](https://www.creative-tim.com/product/material-dashboard-react).
9. Trying to run it
    - Downloaded it
    - ` npm start `
    - sh: 1: react-scripts: not found
    - ` npm install`
    - Grabbing dependencies
    - ` npm start `
    - Worked but a lot of errors
10. Fixing the errors
    - Error: EMFILE: too many open files
    - Just closed things. Now works
11. Looking into how it works
    - App.js
    - index.js
        - Runs App.js
    - Look into "src/examples"
    - Lots of things in the *package.json*
12. How to view on another computer?
    - ` HOST=0.0.0.0 npm start `
    - Then I can connect to it with 192.168.1.101:3000
    - You can also set a specific port: ` HOST=0.0.0.0 PORT=5000 npm start `
13. Drawn rough designs
