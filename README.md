# Udacity Item Catalog

A simple web application that provides a list of items within a variety of categories and integrate third party user registration and authentication. Authenticated users have the ability to post, edit, and delete their own items.

# Pre-requisite tools
1. Virtual Box https://www.virtualbox.org/wiki/Download_Old_Builds_5_2
2. Vagrant https://www.vagrantup.com/downloads.html
3. VM configuration https://github.com/udacity/OAuth2.0
	* or git clone from https://github.com/udacity/OAuth2.0.git
4. Put the item-catalog folder into the OAuth2.0 folder

# Steps to run the project
1. Launch the Vagrant VM from inside the *vagrant* folder with:
`vagrant up`
2. Access the shell with:
`vagrant ssh`
3. Move inside the catalog folder:
`cd /vagrant/item-catalog`
4. Run the application:
`python catalog.py`
5. Browse the application at this URL:
`http://localhost:5000/`

# Acknowledgement
* Hat tip to Ricardo Raphael Joson for using his templates and static files code
* Thanks to my mentor Tim Nelson for his webinar and help

# Author
Hunter Zhou
