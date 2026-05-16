# Setting up a React Environment
#First, make sure you have Node.js installed. You can check by running this in your terminal:
#
#node -v
#If Node.js is installed, you will get a result with the version number:
#
#v22.15.0
#If not, you will need to install Node.js.

# Install a Build Tool (Vite)
#When you have Node.js installed, you can start creating a React application by choosing a build tool.
#
#We will use the Vite build tool in this tutorial.
#
#Run this command to install Vite:
#
#npm install -g create-vite
#If the installation was a success, you will get a result like this:
#
#added 1 package in 649ms

# Create a React Application
#Run this command to create a React application named my-react-app:
#
#npm create vite@latest my-react-app -- --template react
#If you get this message, just press y and press Enter to continue:

# Need to install the following packages:
#create-vite@6.5.0
#Ok to proceed? (y)
#If the creation was a success, you will get a result like this:
#
#
#> npx
#> create-vite my-react-app --template react
#
#|
#o  Scaffolding project in C:\Users\stale\my-react-app...
#|
#-  Done. Now run:
#
#  cd my-react-app
#  npm install
#  npm run dev
#

# Install Dependencies
#As the result above suggests, navigate to your new react application directory:
#
#cd my-react-app
#And run this command to install dependencies:
#
#npm install
#Which will result in this:
#
#added 154 packages, and audited 155 packages in 8s
#
#33 packages are looking for funding
#  run `npm fund` for details
#
#found 0 vulnerabilities
#Run the React Application
#Now you are ready to run your first real React application!
#
#Run this command to run the React application my-react-app:
#
#npm run dev
#Which will result in this:
#
#VITE v6.3.5  ready in 217 ms
#
#➜ Local: http://localhost:5173/
#➜ Network: use --host to expose
#➜ press h + enter to show help
#A new browser window will pop up with your newly created React App! If not, open your browser and type localhost:5173 in the address bar.
