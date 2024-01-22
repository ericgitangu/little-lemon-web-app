# Little Lemon's Web App

This project is a web application for the Little Lemon restaurant, built using Django. It aims to transition the restaurant's website from a one-page design to a database-driven web application. The app will allow the owners to easily update the menu information as it changes seasonally.

## Features

- Home page: Provides an introduction to the Little Lemon restaurant and its concept.
- About page: Gives more details about the restaurant, its ambiance, and its offerings.
- Book page: Allows users to make a reservation at the restaurant.
- Menu page: Displays the restaurant's locally sourced menu items, including daily specials.
- Menu item page: Shows detailed information about each menu item, such as its name, description, price, and photo.

## Getting Started

To get started with this project, follow the steps below:

1. Clone the repository: `git clone https://github.com/erigitangu/little-lemon-web-app.git`
2. Change into the project directory: `cd little-lemon-web-app`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Set up the database: `python manage.py migrate`
5. (Optional) Load initial data: `python manage.py loaddata fixtures/initial_data.json`
6. Start the development server: `python manage.py runserver`
7. Open your web browser and visit: `http://localhost:8000`

## Usage

- Home page: Visit the homepage to learn about the Little Lemon restaurant and its concept.
- About page: Get more information about the restaurant's ambiance, offerings, and values.
- Book page: Make a reservation at the restaurant by selecting a date and time.
- Menu page: Browse through the restaurant's menu items, including daily specials.
- Menu item page: Click on a menu item to view detailed information, such as its name, description, price, and a photo.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on GitHub. You can also fork the repository, make your changes, and submit a pull request.

## Illustrations

Below are some illustrations showcasing the relationships between the Django models used in this project:

1. ![Home Page](/assets/6.png)
2. ![About Page](/assets/12.png)
3. ![Book Page](/assets/13.png)
4. ![Menu Page](/assets/10.png)
5. ![Menu Item Page](/assets/11.png)

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as per the terms of this license.

## Developer

- Eric Gitangu (Deveric)
- Website: [https://developer.ericgitangu.com](https://developer.ericgitangu.com)
- Email: <developer.ericgitangu@gmail.com>
- GitHub: [ericgitangu](https://github.com/ericgitangu)
