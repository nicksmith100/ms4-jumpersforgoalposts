# Jumpers For Goalposts Website

![Jumpers For Goalposts logo](docs/logo.png)

This project creates an eCommerce website for a fictional business called Jumpers For Goalposts. It allows external users to browse and buy retro football shirts, and allows site admins to add, edit and update products. The site is designed to be responsive and accessible on a range of devices, making it easy to navigate for external users and site admins alike.

[View the live project here](https://jumpers-for-goalposts-13c54c4e6e2a.herokuapp.com/)

![Jumpers For Goalposts website displayed on various devices](docs/responsive_screens.png)


## Table of Contents

1. [Project Goals](#project-goals)
2. [Research](#research)
3. [User Stories](#user-stories)
4. [Design](#design)
5. [Features](#features)
6. [Testing](#testing)
7. [Tecnologies Used](#technologies-used)
8. [Deployment](#deployment)
9. [Credits](#credits)


## Project Goals

### Purpose

An e-commerce site selling retro football shirts, which allows customers to browse and buy such shirts, while allowing site admins to add, edit and delete products.

### Client Goals

The client is a fictional business called Jumpers For Goalposts. Their goals are to:
- Have an engaging site which attracts interest from buyers of retro football shirts.
- Drive sales of their retro football shirts by making the browsing and buying of products as straightforward as possible.
- Minimise avoidable contact by providing easy-to-find information to potential buyers. 

### User Goals

The primary goals of the user are to:
- Browse retro football shirts using a variety of methods such as keyword searching, browsing by feature and listing based on different criteria.
- Purchase selected shirts securely.
- Find information about previous orders they have made.

Detailed user stories are provided in the [User Stories](#user-stories) section below.

## User Stories

A. As a **first-time visitor** I want to:
1. Establish what products are available on the site.
2. Browse products using easy-to-follow navigation.
3. Find answers to my questions.
  
B. As a **returning visitor** I want to:
1. Browse and search for specific products using a variety of methods.
2. Purchase selected products.
3. View details of my previous orders.  

C. As an **admin user** I want to:
1. Add products to the inventory.
2. Edit or delete existing products in the inventory.
3. Receive details of customer orders to be fulfilled.
4. View sold items and mark them as unsold if necessary.

D. As a **superuser**, in addition to the admin functions outlined above, I want to:
1. Add or edit product categories.
2. Add or remove admins and amend their privileges. 

## Design

### Wireframes

Wireframes were created using the Figma platform: [Figma - Jumpers For Goalposts](https://www.figma.com/file/uwlFESlwKMuzSo25F4ccFt/Jumpers-For-Goalposts?type=design&node-id=0%3A1&mode=design&t=lA9PFoLqKGXvNOGx-1)

<details><summary>Desktop wireframes</summary>

![Desktop wireframes - public](docs/desktop_wireframes.png)

</details>

<details><summary>Mobile wireframes</summary>

![Mobile wireframes - public](docs/mobile_wireframes.png)

</details><br>

Based on prior experience I decided that desktop and mobile wireframes would be sufficient to keep the overall layout of the site on track, the expectation being that [Bootstrap's grid system](https://getbootstrap.com/docs/5.3/layout/grid/) would provide the responsiveness required at different device breakpoints in between (see [Layout and Styling](#layout-and-styling) section below).

Furthermore, I focused the wireframes on the main product purchase workflow, recognising that this was where design choices would be key. The other pages contain simple forms and tables, so I considered there to be little value in producing specific wireframes for those pages.

#### Differences between wireframes and final design

The wireframes include a separate product details page (shown in the desktop wireframes only and labelled "not used"). However, during development I realised that I could reduce unnecessary navigation and provide a smoother user experience by keeping the user on the same page and simply flipping the product card to display the product details.

Most other key features of the wireframes are retained in the final implementation, although aspects of the layout have evolved during the design and development process.

### Layout and Styling

#### Bootstrap

The site uses the [Bootstrap 5.3 Grid system](https://getbootstrap.com/docs/5.3/layout/grid/) to ensure it is fully responsive on all device and viewport sizes. Bootstrap 5.3 uses the following [breakpoints](https://getbootstrap.com/docs/5.3/layout/breakpoints/), the shorthand references for which are used throughout the rest of this document:

| Breakpoint        | Shorthand   | Dimensions |
|-------------------|-------------|------------|
| Extra small       | xs          | <576px     |
| Small             | sm          | ≥576px     |
| Medium            | md          | ≥768px     |
| Large             | lg          | ≥992px     |
| Extra large       | xl          | ≥1200px    |
| Extra extra large | xxl         | ≥1400px    |

In addition, the site uses the following specific components from the Bootstrap library:

- [Navbar](https://getbootstrap.com/docs/5.3/components/navbar/) for the header.
- [Cards](https://getbootstrap.com/docs/5.3/components/card/) to display product information on the products page.
- [Accordion](https://getbootstrap.com/docs/5.3/components/accordion/) to provide a collapsible menu for the FAQs.
- [Alerts](https://getbootstrap.com/docs/5.3/components/alerts/) to display status messages.
- [Modal plugin](https://getbootstrap.com/docs/5.3/components/modal/) to display enlarged product images on click.
- [Spacing](https://getbootstrap.com/docs/5.3/utilities/spacing/) and [typography](https://getbootstrap.com/docs/5.3/content/typography/) utility classes throughout, ensuring the layout and font are appropriate to the device in use.
- [Color](https://getbootstrap.com/docs/5.3/utilities/colors/) utility classes to provide specific meaning to text throughout.
- [Display property](https://getbootstrap.com/docs/5.3/utilities/display/) to toggle the visibility of some components at certain breakpoints.

#### Media queries

In addition to the responsive layout provided by Bootstrap, specific media queries are used to rotate the main background image to match the orientation of the device, and to change the sizes of the club badges on the home page.

### Imagery

- The **Logo** is a retro-looking football badge, created using a template by [Kulokale on Canva](https://www.canva.com/templates/EAFNwkE8v5Y-retro-and-vintage-football-club-logo). 

- The **Background image** is an aerial photo of a football pitch, courtesy of [Timothy Tan on Unsplash](https://unsplash.com/photos/green-sports-court-illustration-PAe2UhGo-S4). The image is displayed in portrait or landscape depending on the orientation of the device in use, and a partially opaque overlay is placed over it throughout the site to ensure clarity of site content.

- The **404 (Page Not Found)** error page includes a photo of a football going wide of a goal, courtesy of [Omar Ram on Unsplash](https://unsplash.com/photos/man-in-red-shirt-and-black-pants-playing-soccer-during-daytime-IvXnC7u6yD0)

- The **club badges** on the home page are sourced from [Wikipedia](https://en.wikipedia.org/). Their use in this instance for educational purposes is considered to represent fair use.
  
  <details><summary>Logo</summary>
  
  ![Logo](docs/logo.png)
  
  </details>

  <details><summary>Background image</summary>
  
  ![Background](docs/background.webp)
   
  </details>

  <details><summary>404 image</summary>
  
  ![404 image](docs/404.webp)
   
  </details>

### Colour Scheme
  
- The **main colours** used for site components (such as navigation items and buttons) are blue (#2C314F) and cream (#FFF2CD) to match the logo. These colours provide a contrast to the pale green background, and are distinctive enough to give the company a brand identity. Importantly, these colours are not associated with any major football team, and so will appear neutral to football fans visiting the site.  

- The **button hover** colour is dark blue (#0D0F18), which is different enough to provide the necessary effect without detracting from the overall colour scheme. 

- Body **text** is the same dark blue (#0D0F18), while Boostrap's utility classes are used to convey meaning to text throughout, such as .text-danger (#DC3545) for urgent warnings.

  <details><summary>Colour scheme palette</summary>

  ![Website colour scheme palette](docs/palette.png)

  </details>

### Typography

- The site uses [Fredoka](https://fonts.google.com/specimen/Fredoka) throughout, imported from [Google Fonts](https://fonts.google.com/). Fredoka is a retro-looking font which fits with the theme and aesthetic of the site.

    <details><summary>Fredoka font</summary>

    ![Fredoka font](docs/fredoka.png)

    </details>

### Icons

- [Bootstrap Icons](https://icons.getbootstrap.com/) have been used for **navigation items**, **alerts** and various **buttons**, utilised as classes in the `<i>` tag.

  <details><summary>Navigation icons</summary>

  ![Navigation icons](docs/nav_icons.png)

  </details>

  <details><summary>Alerts</summary>

  ![Success message](docs/success_message.png)
  ![Info message](docs/info_message.png)
  ![Warning message](docs/warning_message.png)
  ![Error message](docs/error_message.png)

  </details>

  <details><summary>Button</summary>

  ![Button](docs/button.png)

  </details>
  
### Favicon

- The **favicon** is the football from the logo, generated using [Favicon Generator](https://www.favicon-generator.org/).

  <details><summary>Favicon</summary>

  ![Favicon](docs/favicon.png)

  </details>

### Loading spinner

- The site utilises a **loading spinner** on the checkout page to illustrate that a page is loading. This is also the football from the logo, but with shadowing removed.

  <details><summary>Loading Spinner</summary>

  ![Loading spinner](docs/spinner.png)

  </details>


## Features

### Scope

- #### Minimum Viable Product

  To be viable as an eCommerce site for retro football shirts and meet the stated [Project Goals](#project-goals), the website **must have**:
         
- #### Additional Features (in scope)

  To provide a good user experience in line with the stated [Project Goals](#project-goals), the website **should have**:
   
- #### Future Ideas (not currently in scope)
  
   To provide a better user experience and better meet the stated [Project Goals](#project-goals), the website also **could have**:

### Python Functionality using Django

Python has been used to build the core backend application which underpins the site, utilising the [Django web framework](https://www.djangoproject.com/). In particular, Python and Django have been used to:

- Provide routing of pages, allowing meaningful URLs to be used to return pages and content to the user.
- Connect to the backend database to retrieve information and serve it to the site, and to allow creation, updating and deletion of records.
- Provide login functionality and security, ensuring only authorised users can access and edit particular information.
- Display flash messages to the user.

### Database

The backend application connects to a database hosted on [ElephantSQL](https://www.elephantsql.com/), which contains # models as outlined below.

#### MODEL DETAILS

### Page Elements and Interaction

The website is divided between public-facing pages which provide product details to external users sourced from the database, and admin pages (for logged in users) which allow admins to update product information in the database.

#### Public pages and elements

- **Header**: ...
         
    <details><summary>Header (lg)</summary>
          
    ![Header (lg)](docs/header_lg.png)

    </details>
        
    <details><summary>Header (sm)</summary>
          
    ![Header (sm)](docs/header_sm.png)

    </details>
        
    <details><summary>Header (xs)</summary>
          
    ![Header (xs)](docs/header_xs.png)

    </details><br>

- **Home page**: ...

    <details><summary>Home (lg)</summary>
    
    </details>

    <details><summary>Home (xs)</summary>

    </details><br>

- **OTHER PAGES**
  
  All elements are responsive, for example...

   
- **Flash messages**

- **403 (Forbidden)**: A 403 (Forbidden) error is displayed in the event that a user tries to browse to a page that they are not authorised for. The 403 page includes...

- **404 (Page Not Found)**: A 404 (Page Not Found) error is displayed in the event that a user tries to browse to a page that does not exist. The 404 page includes...

- **500 (Internal Server Error)**: A 500 (Internal Server Error) error is displayed in the event of an error in the application or the server. The 500 page includes...

#### Admin pages and elements

While all admin pages are fully responsive, screenshots below are shown in desktop format only, as they would be expected to be accessed primarily by desktop.

- **Login**: ...
  
    <details><summary>Login form</summary>
          
    ![Login form](docs/login.png)

    </details><br>
  
### JavaScript Functionality

#### jQuery

- The jQuery libary has been used to faciliate the use of JavaScript, in particular for adding event listeners.

#### Flip cards

- The flip card function on...


## Testing

### Automated testing

- #### HTML validation with [W3C Markup Validator](https://validator.w3.org/)


- #### CSS validation with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)


- #### JavaScript validation using [JSHint](https://jshint.com/)

- #### Python validation using [CI Python Linter](https://pep8ci.herokuapp.com/)

  
- #### Accessibility using [Lighthouse accessibility](https://developer.chrome.com/docs/lighthouse/accessibility/)

  Lighthouse audit scores (accessed through Chrome DevTools) show that the site is fully accessible and complies with best practices.

  <details><summary>Lighthouse scores</summary>

  ![Lighthouse scores](docs/lighthouse.png)

  </details>

### Manual Testing

#### User stories

#### User story screenshots

#### Feature testing
    
#### Browser and device compatibility

  The above features were tested on the following browsers and devices:

  | Browser        | Version                                  | Device                                      | Operating Sytem       | Results                                                        |
  |----------------|------------------------------------------|---------------------------------------------|-----------------------|----------------------------------------------------------------|
  | Firefox        | 120.0.1 (64-bit)                         | Dell Latitude E6420 laptop                  | Windows 10 Home       | Fully functional                                               |
  | Google Chrome  | 119.0.6045.199 (Official Build) (64-bit) | Dell Latitude E6420 laptop                  | Windows 10 Home       | Fully functional            |
  | Google Chrome  | 119.0.6045.163                           | Samsung Galaxy S9 SM-G960F                  | Android 10            | Fully functional            |
  | Google Chrome  | 119.0.6045.169                           | Apple iPad Pro (12.9-inch) (4th generation) | iPadOS 17.1.2         | Fully functional            |
  | Microsoft Edge | 119.0.2151.93 (Official build) (64-bit)  | Dell Latitude E6420 laptop                  | Windows 10 Home       | Fully functional            |
  | Safari         | 17.1.2                                   | Apple iPad Pro (12.9-inch) (4th generation) | iPadOS 17.1.2         | Fully functional            |

  In addition, a number of friends, family and colleagues tested the device on a range of devices and operating systems, with no oustanding issues. 

### Bugs and fixes



## Technologies Used

### Languages
- [HTML](https://html.spec.whatwg.org/multipage/)
  - Standard markup language for web pages
- [CSS](https://www.w3.org/Style/CSS/)
  - Adding style to HTML
- [JavaScript](https://www.w3schools.com/js/)
  - Adding interactive elements
- [Python](https://www.w3schools.com/python/)
  - Providing backend application
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/)
  - Templating language for page templates
 
### Frameworks
- [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
  - Overall layout and styling, and specific components as described above
- [Django web framework](https://www.djangoproject.com/)
  - Providing backend application and page routing

### Libraries
- [jQuery](https://jquery.com/)
  - Facilitating JavaScript functionality, in particular event listeners
- [Google Fonts](https://fonts.google.com)
  - [FONTNAMES] fonts
- [Bootstrap icons](https://icons.getbootstrap.com/)
  - Icons on navigation items, social media links, buttons and form elements

### APIs

### Platforms
- [ElephantSQL](https://www.elephantsql.com/)
  - Used for hosting database
- [Heroku](https://heroku.com/)
  - Deployment
- [Github](https://github.com/)
  - Storing code
- [Gitpod](https://gitpod.io/)
  - IDE used for project development

### Other Tools
- [Figma](https://www.figma.com/)
  - Wireframes
- [Coolors](https://coolors.co/)
  - Colour palette
- [Favicon Generator](https://www.favicon-generator.org/)
  - Website favicon
- [Am I Responsive](https://ui.dev/amiresponsive)
  - Montage of different devices displaying the site
- [Unsplash](https://unsplash.com/)
  - Images on Home, 403, 404, 500 pages
- [Fix the photo](https://fixthephoto.com/uk/online-gimp.html)
  - Image editing

## Deployment

### Live deployment

The site is deployed to Heroku: [View the live project here]()

### Deployment pre-requisites

In order to deploy the project successfully, you will need:

- An [ElephantSQL](https://www.elephantsql.com/) account, with a database...
- An Amazon Web Services account...

Free accounts on all of these platforms are sufficient.

### Local deployment

To deploy this project locally, you must first either [fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) or [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this [repository](https://github.com/nicksmith100/ms4-jumpersforgoalposts).

After forking or cloning the repository, within your IDE:

- Run ```pip3 install -r requirements.txt``` to install all dependencies.
- Create an ```env.py``` file for storing environment variables, ensuring it is added to ```.gitignore```.
- Add the following code to your ```env.py``` file, replacing the placeholder values with those identified under [Deployment pre-requisites](#deployment-pre-requisites) above.

  ```

  ```

### Deployment to Heroku

To deploy to [Heroku](https://www.heroku.com/):

1. In your IDE run `pip3 freeze > requirements.txt` to create/update a requirements.txt file containing project dependencies.
2. In your IDE run `echo web: python app.py > Procfile` to create a Procfile. Check that the file contains the text 'web: python app.py' and delete any blank lines at the bottom.
3. Push these two new files to the GitHub repository.
4. Login to Heroku, select 'Create New App', create a unique name for the app and select your nearest region. Click 'Create App'.
5. Navigate to the Deploy tab on Heroku dashboard and select Github, search for your repository by name and click 'connect'.
6. Navigate to 'settings', click reveal config vars and input the the following:

  | Key | Value |
  | :---: | :---: |

7. Go back to the Deploy tab and click on 'Enable Automatic Deploys'.
8. Click 'Deploy Branch'.
9. Once build is complete click on 'View' to launch the new app.

## Credits

### Code

- [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/layout/grid/)

Any other code snippets are credited in comments in the relevant files.

### Content

All written content is my own.

### Media

### Acknowledgements

- My Mentor [Rory Patrick Sheridan](https://github.com/Ri-Dearg) for many helpful pointers as always!
- Our Cohort Facilitator [...]() for providing helpful guidance on project requirements throughout.

### README content

- [Emma Hewson](https://github.com/emmahewson/mp3-swimmon#Deployment) - inspiration for elements of this README, especially Heroku deployment instructions.
- [Paul Woods](https://github.com/pawoods/project3/blob/main/README.md#deployment) - local deployment instructions.
