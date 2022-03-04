# brick-friends
brick-friends is a command-line tool to massively add friends on [brick-hill](https://www.brick-hill.com/). This project was made for educational purposes only.
## Installation
Use the setup.py file to install brick-friends.
```bash
py setup.py install
```
## Usage
### Required
```bash
brick-friends session=<brick-hill session cookie> token=<brick-hill token>
```
### Optional
Minimum add range (Default is 0).
```bash
brick-friends [-m minrange]
```
Maximum add range (Default is 1000).
```bash
brick-friends [-M maxrange]
```
How many threads it should use.
```
brick-friends [-t threadamount]
```
Find and use proxy flag.
```bash
brick-friends [-a autoproxy]
```
## Get session and token
### Session
First you have to login to your brick-hill account. After that you go to inspect element -> Application -> Cookies -> https://www.brick-hill.com and you'll find brick_hill_session cookie which you copy and paste into the cli.
### Token
First go to a random profile and open inspect element. In there you go to the Network tab, filter by doc and then press the friend button on the user, you'll need to search for the friends post request in the network log. After finding it, copy _token, paste it into the cli and you're good to go.
## License
[MIT](https://choosealicense.com/licenses/mit/)