# Followers Map


Followers Map is an app to provide map with markers of locations of followers of cetrain user.
## How to use

- Run "application.py" or go [here](http://kulyk.pythonanywhere.com)
- Enter nickname and Bearer Token
- Click "Find followers"
- The app will display a map with locations of followers

#### An error can occure if:
- username is incorrect
- token is expired or incorrect
- user's profile is private
- user doesn't follow anybody (will display empty map)


## Tech

Followers Map uses:
- Folium - to build a map
- Geopy - to get coordinates
- Flask - to realize backend processes
- HTML & CSS - to make start webpage
- Fragments of design styles by [СodingNepal](https://www.codingnepalweb.com/2020/05/light-neumorphism-login-form-ui-design-html-css.html) to make start page more attractive


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

