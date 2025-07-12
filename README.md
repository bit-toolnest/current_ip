# CurrentIP
read the current public ip and if it was changed, need to update gist file in gitHub

git clone https://github.com/bitresearch2006/CurrentIP.git

🎯 1. Create a Public Gist
Go to https://gist.github.com.

Create a new gist.

In the visibility options, choose Public.

Save it—this gives you a permanent URL and a Gist ID (you’ll need it for automation).

cd CurrentIP

update ip_to_gist.py where it asks to add gist id

*/5 * * * * /usr/bin/python3 path_to_python_file/ip_to_gist.py
