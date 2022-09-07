# Auburn ACM Website
This repo contains the code for Auburn ACM's website. We are currently working to implement the design created by Cady Pridgeon.

If you want to contribute, shoot an ACM officer a message on Groupme or Discord, and we'll find something for you to help with.

---
## Running the software
### <b>Installing dependencies</b>
First, ensure that you have python 3.10 installed.  
<b>Recommended</b>: Create a virtual environment for this project. 
 1. `python -m venv venv` creates a new directory `venv` that contains the virtual environment.
 2. Activate the environment -- dependent on which terminal you are using. 
    - For bash, use `. venv/Scripts/activate`
    - For cmd, use `.\venv\Scripts\activate.bat`
    - For powershell, user `.\venv\Scripts\Activate.ps1`
 3. Now, install the dependencies for the project with  
  `pip install -r requirements.txt`  

<b>Not Recommended</b>: Installing directly though pip. If you use this method, be sure not to use any packages not listed in `requirements.txt`, or the project may not works for others.
 1. Install packages directly to your local python using   
 `pip install -r requirements.txt`  



To start a development server, run `python manage.py runserver`  
Open a browser to `localhost:8000`, and changes to the source code should be reflected after reload. If you figure out how to set up hot reload, let me know!