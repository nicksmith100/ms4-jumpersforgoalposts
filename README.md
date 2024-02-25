# Jumpers For Goalposts Website

![Jumpers For Goalposts logo](docs/logo.png)

This project creates an eCommerce website for a fictional business called Jumpers For Goalposts. It allows external users to browse and buy retro football shirts, and allows site admins to add, edit and update products. The site is designed to be responsive and accessible on a range of devices, making it easy to navigate for external users and site admins alike.

[View the live project here](https://jumpers-for-goalposts-13c54c4e6e2a.herokuapp.com/)

![Jumpers For Goalposts website displayed on various devices](docs/responsive_screens.png)


## Table of Contents

1. [Project Goals](#project-goals)
2. [Project Guide](#project-guide)
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

## Project Guide

I used [Code Institute](https://github.com/Code-Institute-Solutions)'s [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1) walkthrough as a guide throughout development. While it would be impractical to credit every part of Boutique Ado code within the code itself, this document will clearly explain the custom features which have been added over and above the Boutique Ado website.

## User Stories

A. As a **first-time visitor** I want to:
1. Establish what products are available on the site.
2. Browse products using easy-to-follow navigation.
3. Find answers to my questions.
  
B. As a **returning visitor** I want to:
1. Browse and search for specific products using a variety of methods.
2. Purchase selected products.
3. View details of my previous orders.  

C. As a **staff user** I want to:
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
  - Images and details of products for sale.
  - A way for potential customers to browse products.
  - A method for allowing customers to purchase selected products.
         
- #### Additional Features (in scope)

  To provide a good user experience in line with the stated [Project Goals](#project-goals), the website **should have**:
  - Sophisticated browsing, searching and list ordering functionality to allow customers to find products through a variety of methods.
  - A secure payment system utilising a recognised, trusted payment provider.
  - A user registration system, allowing users to save delivery details and view past orders.
  - An FAQ section to provide answers to the most commonly asked questions and minimise avoidable contact from customers.
  - Newsletter sign-up, allowing the business to keep customers up-to-date with news and special offers.
   
- #### Future Ideas (not currently in scope)
  
   To provide a better user experience and better meet the stated [Project Goals](#project-goals), the website also **could have**:
   - The option for registered users to select their favourite team(s), which would allow for prioritisation of those shirts when browsing, as well as alerts when new items relating to that team are added.
   - The ability for a superuser to dynamically update the team badges displayed on the front page, allowing them to promote different teams at different times based on current events (e.g. promoting the two teams appearing in a cup final).
   - A newsletter creation function, allowing admins to easily create and send newsletters via a form.
   - A wishlist feature, allowing users to add items to a virtual bag for purchase at a later date. 

### Python Functionality using Django

Python has been used to build the core backend application which underpins the site, utilising the [Django web framework](https://www.djangoproject.com/). In particular, Python and Django have been used to:

- Provide routing of pages, allowing meaningful URLs to be used to return pages and content to the user.
- Connect to the backend database to retrieve information and serve it to the site, and to allow creation, updating and deletion of records.
- Provide login functionality and security, ensuring only authorised users can access and edit particular information.
- Display messages to the user (via [Bootstrap Alerts](https://getbootstrap.com/docs/5.3/components/alerts/)).

### Database

The backend application connects to a Postgres database hosted on [Amazon Web Services](https://aws.amazon.com/free/database/).

#### Schema

 A number of models were created, as illustrated below. Here the application which the model belongs to is shown before the underscore.

![Database schema](docs/db_schema.png)

Below is a more detailed breakdown of these models and their basis.

##### Django models

- **user**: Part of the [Django allauth](https://docs.allauth.org/en/latest/) app, which provides secure authentication and registration. It is included above to illustrate its relationship with the userprofile model.

##### Models adapted from Boutique Ado

- **userprofile**: Allows an authenticated user to save default name and delivery information.
- **order**: Collects information on a customer's order for use in the checkout process.
- **orderlineitem**: Collects information on individual items in an order.
- **product**: Provides all relevant information about a product. While this is adapted from the Boutique Ado walkthrough, it has been adapted considerably. In particular, rather than a single category field it includes multiple categories linking to other models (**league**, **team** and **condition**), as well as multiple other fields relating to product characteristics (**home_away**, **season**, **player_issue**, **signed** and **year**). It also includes a **sold** field (boolean), allowing a product to marked as sold without deleting it from the database.

##### Custom models

- **league**: Allows both shirts and teams to be categorised based on the league from which they come.
- **team**: Allows products to be categorised by the team to which they belong. Also allows newsletter subscribers to indicate their favourite team.
- **condition**: Allows products to be categorised based on their condition.
- **subscriber**: Allows users to subscribe to a newsletter by providing their name and email address. Optionally allows users to indicate their favourite team and opt into updates about their favourite team only.
- **faq**: Allows admins to create questions and answers for display on the site.

#### Content

Database content was sourced from a [Football Kits Dataset](https://www.kaggle.com/datasets/afaksnmez/football-kits-dataset), provided by [safaksonmezz on Kaggle](https://www.kaggle.com/afaksnmez). The dataset comprises data scraped from a real website called [Classic Football Shirts](https://www.classicfootballshirts.co.uk/).

The data was cleaned, pruned, and then converted to JSON and formatted as a Django fixture for uploading to the database. Images were downloaded from the [Classic Football Shirts](https://www.classicfootballshirts.co.uk/) website, with dead links being removed.

### Page Elements and Interaction

The website provides different functionality depending on the user's credentials. In general:
- **Public users**: Can browse for products, add them to their bag and securely check out. In addition, they can view general site content including FAQs, and subscribe to the newsletter. They also have the ability to sign up to become a registered user.
- **Registered users**: As well as the above, they can update their profile with default contact and delivery information, and view past order history.
- **Staff users**: As well as the above, they can add/edit/delete products, view sold items, and add/edit/delete FAQs.
- **Superusers**: As well as the above, they can access an admin portal, allowing them to add/edit/delete users, and add additional fields to category models, e.g. additional leagues, teams and conditions. 

#### Header

<details><summary>Header</summary>
            
![Header (xl)](docs/header_xl.png)

</details><br>

All pages include a header with the site logo, a category menu, a search bar and a navigation menu:

- The **site logo** includes an anchor tag linking it to the homepage.
- The **category menu** includes a series of buttons providing different product views. The first button allows all available products to be viewed, sorted by different criteria, while the remaining buttons allow products to be viewed by category or feature (size, year, league, or special category).

  <details><summary>Category menu (all shirts)</summary>
            
  ![All shirts dropdown](docs/all_shirts_dropdown.png)

  </details>

  <details><summary>Category menu (leagues)</summary>
            
  ![Leagues dropdown](docs/leagues_dropdown.png)

  </details><br>
  
- The **search bar** allows all products to be searched by keyword.
- The **navigation menu** includes a dropown account menu, as well as links to FAQs, newsletter signup and shopping bag. The shopping bag provides an indication of number of items and bag total. The dropdown account menu provides an option to register or login, and for logged in users provides options to view their profile or logout. For logged in staff users it includes the additional options to add products or view sold products, while for superusers it includes a link to the admin menu.

  <details><summary>Account menu (logged out)</summary>
          
  ![Account menu (logged out)](docs/nav_menu_acc_logged_out.png)

  </details>

  <details><summary>Account menu (logged in)</summary>
          
  ![Account menu (logged in)](docs/nav_menu_acc_logged_in.png)

  </details>

  <details><summary>Account menu (staff)</summary>
          
  ![Account menu (staff)](docs/nav_menu_acc_staff.png)

  </details>

  <details><summary>Account menu (superuser)</summary>
          
  ![Account menu (superuser)](docs/nav_menu_acc_superuser.png)

  </details>

##### Responsive layout

- The category menu drops below the header at md and lg breakpoints.

  <details><summary>Header (md)</summary>
          
  ![Header (md)](docs/header_md.png)

  </details><br>

- The navigation menu collapses to a hamburger menu with vertical navigation menu on sm viewports and below. In this mode the search bar is moved to the bottom to provide a better aesthetic.

  <details><summary>Header (xs)</summary>
            
  ![Header (xs)](docs/header_xs.png)

  </details><br>

#### Home

<details><summary>Home page</summary>
            
![Homepage (xl)](docs/home_xl.png)

</details><br>

The home page includes a quick access menu comprising the club badges of the twelve most popular teams. Being a UK-based website, this includes England's "top six" and Scotland's "top two", as well as a selection of the most popular teams across Europe. Clicking any of the badges will display products filtered to that team, while clicking "Shop the whole collection" will display all available products. 

##### Responsive layout

- Badges are displayed at different sizes and configurations based on the viewport breakpoint.
- The background image is displayed horizontally or vertically depending on device orientation (this is true across all pages).
         
  <details><summary>Home (xs)</summary>
            
  ![Home (xs)](docs/home_xs.png)

  </details><br>

#### Products page

The products page displays all available products by default.

##### Product cards

- Each product is displayed in its own [Bootstrap Card](https://getbootstrap.com/docs/5.3/components/card/), including the product image, name, price, size and condition.
- Clicking the product image displays a [modal](https://getbootstrap.com/docs/5.3/components/modal/) with a full-size image.
- Clicking elsewhere on the product card flips it to reveal further details and an add-to-bag button.
- Clicking the add-to-bag button adds the product to the user's bag, changes the button to a remove-from-bag button, and displays a success alert.
- Clicking the remove-from-bag button removes it from the user's bag, changesthe button back to an add-to-bag button, and displays a warning alert.

  <details><summary>Products page - image modal and flipped card</summary>
              
  ![Products modal](docs/product_modal_xl.png)
  ![Products (xl)](docs/products_xl.png)

  </details>

  <details><summary>Products page - adding to bag and removing</summary>
              
  ![Product added](docs/product_added_xl.png)
  ![Product removed](docs/product_removed_xl.png)

  </details><br>

##### Page navigation

- [Pagination](https://docs.djangoproject.com/en/5.0/topics/pagination/) is used to manage the large number of products in the database. The number of products on each page is set to 36, as this is divisible by 2, 3 and 4 which are the possible number of cards in each row, thereby preventing any empty spaces in rows (except for the final row on the final page).

  <details><summary>Pagination</summary>
              
  ![Pagination](docs/pagination.png)

  </details><br>

- The page includes a back-to-top button to avoid the user having to scroll all the way back when there are large numbers of products on the page.

  <details><summary>Back-to-top button</summary>
              
  ![Back-to-top](docs/back_to_top.png)

  </details><br>

##### Searching, sorting and filtering

- Searching by keywords reveals any matching products and displays the search terms and number of results at the top of the products page. Similarly, selecting products by category or feature displays the relevant filter and number of results at the top of the page. In both cases the filter or search terms can be cancelled by clicking the "x" next to them.

  <details><summary>Keyword search</summary>
          
  ![Keyword search](docs/product_search.png)

  </details>

  <details><summary>Category filter</summary>
          
  ![Category filter](docs/product_team_filter.png)

  </details><br>

- Products can be sorted by a number of different criteria

  <details><summary>Product ordering</summary>
          
  ![Product ordering](docs/product_ordering.png)

  </details>

##### Admin functions

If the user is staff or superuser:

- Selecting "Sold products" in the account dropdown provides the same product view, but only lists products with the sold field set to true. All other functions are the same as above.

  <details><summary>Sold products</summary>
          
  ![Sold products](docs/sold_products.png)

  </details><br>

- The footer of the flipped product card includes "Edit" and "Delete" buttons. Clicking "Edit" takes the user to the relevant "Edit product" page, while clicking "Delete" triggers defensive programming, displaying cancel and confirm links to prevent accidental deletion.

  <details><summary>Edit and delete buttons</summary>
          
  ![Edit and delete buttons](docs/product_details_staff.png)
  ![Delete confirmation](docs/product_details_delete.png)

  </details>

##### Responsive layout
  
- The page utilises [Bootstrap's column classes](https://getbootstrap.com/docs/5.3/layout/columns/) to display between one and four cards in each row depending on breakpoint.

  <details><summary>Products (xs)</summary>
              
  ![Products (xs)](docs/products_xs.png)

  </details>

  <details><summary>Products (sm)</summary>
              
  ![Products (sm)](docs/products_sm.png)

  </details>

  <details><summary>Products (md)</summary>
              
  ![Products (xl)](docs/products_md.png)

  </details>

  <details><summary>Products (xxl)</summary>
              
  ![Products (xxl)](docs/products_xxl.png)

  </details><br>

   
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
