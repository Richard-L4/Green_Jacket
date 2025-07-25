# Green_Jacket <img src="static/images/masters-badge.jpg" alt="Masters Badge" width="24" height="24">
---
## Overview
---
The **Green Jacket** project is a clean, user-friendly e-commerce site built for fans of masters-style general items. It allows users to browse and purchase items with ease, whether shopping as a guest or as a registered user.

The platform provides a smooth shopping experience with optional user registration for those who want to save items, leave item reviews, and speed up future checkouts. Admin users can manage inventory directly from the front end, making updates to items fast and efficient.

The design and development of the site follow modern best practices, incorporating a strong focus on user experience, full CRUD functionality, mobile-first responsive design, and Agile development methodology.

Live link to project [Green_Jacket](https://green-jacket-club-904896471b2f.herokuapp.com/)

---

# Green Jacket
![Home page](static/images/home-page.png).

# 🛍️ User Experience (UX)

This e-commerce platform prioritises an intuitive and user-friendly shopping experience:

- **Simplicity:** The interface is clean and item-focused, making it easy for users to browse items without distractions.

- **Privacy-Focused Accessibility:** Users can shop and complete purchases without needing to register, preserving privacy and reducing friction.

- **Account Benefits:** Registered users can save items for later, write and manage reviews, and store checkout details for future convenience.

- **Interaction:** The platform allows logged-in users to post, edit, and delete reviews on items, encouraging meaningful engagement.

- **Responsiveness:** Built using a mobile-first approach, the site performs smoothly on all devices, from the smallest smartphones to large desktop screens.

---

# 🔄 CRUD Functionality

The platform supports full **CRUD** (Create, Read, Update, Delete) operations, ensuring dynamic content interaction:

- **Create:** Users can create accounts, write item reviews, and save items to their saved list. Admins can add new items via the front end.

- **Read:** All users can browse and view items, reviews, and order details without needing to log in.

- **Update:** Logged-in users can update their reviews and profile details. Admin users can edit item information.

- **Delete:** Users can delete their own reviews and saved items. Admins have the ability to delete items.

This structure enables efficient content and user management, both from a user and administrator perspective.

---

# 🧩 Five Planes of User Experience Design

## 🔹 Strategy Plane
**Goal:** To provide a simple, secure, and satisfying online shopping experience for users interested in general masters-style items.

## 🔹 Scope Plane
- **Features:** Item listing pages, item detail views, shopping trolley, checkout system with Stripe integration, user authentication, review system, profile management, and a checkout confirmation page.
- **Content:** Item descriptions, images, user reviews, and dynamic saved items.

## 🔹 Structure Plane
- Clear site navigation: Home → Items → Item Details → Trolley → Checkout → Order Summary.
- Logical user flows support both guest checkout and account-based shopping.

## 🔹 Skeleton Plane
- Layouts are optimised for mobile-first use with responsive menus, easy tap targets, and a streamlined trolley/checkout process.

## 🔹 Surface Plane
- Clean, modern design with consistent fonts, spacing, and color palette.
- The focus is on simplicity and trust to enhance the shopping experience.

---

# 🧪 Agile Development Principles

This project followed Agile methodologies throughout its development cycle:

- **Iterative Design:** Features were implemented stage by stage and tested regularly.
- **Continuous Feedback:** User and peer feedback guided refinements in layout and functionality.
- **User-Centric Priorities:** Design and feature decisions were made with the end-user’s needs as the primary focus.
- **Adaptability:** The development process remained flexible, accommodating technical challenges and evolving user needs.

---

# 📱 Mobile-First Strategy

The site was designed from the ground up with a mobile-first philosophy:

- Layouts and components were optimised first for small screens, then enhanced via media queries for larger devices.
- Touch-friendly buttons, streamlined navigation, and quick-loading content improve usability and speed on mobile networks.
- Lightweight assets and performance-conscious development improve experience on both low and high-speed connections.

---

# ✅ Summary

This online shopping platform delivers a clean, responsive, and privacy-conscious experience for both guests and registered users. With robust user interaction features, flexible account options, admin-friendly item management, and secure Stripe payment integration, the site is well-positioned for future growth and user retention. Whether on desktop or mobile, users can browse, shop, and interact with ease.

---

##  Wireframes

Using wireframes allows me to create a simple, visual blueprint of the website early in the design process. This helps me focus on the overall layout, content placement, and navigation without getting distracted by colors, fonts, or images. By mapping out the structure first, I can quickly test different ideas and make changes easily before any coding begins. Wireframes also ensure that the site will be user-friendly and logically organized, ultimately saving time and effort during development and helping communicate my vision clearly to others involved in the project.

### Home page Laptop

![Home page laptop](static/images/Home-page-wirframe.png)

### Who We Are Laptop

![Who we are page laptop](static/images/who-we-are-wireframe.png)

### Items Laptop

![Items page laptop](static/images/items-wireframe.png)

### Items Details Laptop

![Item Details page laptop](static/images/item-detials-wireframe.png)

### Home page Tablet

![Home page Tablet](static/images/home-tablet-wireframe.png)

### Who We Are Tablet

![Who We Are page Tablet](static/images/who-we-are-tablet-wireframe.png)

### Items Tablet

![Items page Tablet](static/images/items-page-tablet-wireframe.png)

### Items Details Tablet

![Item Details page Tablet](static/images/item-details-tablet-wireframe.png)

### Home page Mobile

![Home page Mobile](static/images/home-mobile-wireframe.png)

### Who We Are Mobile

![Home page Mobile](static/images/home-mobile-wireframe.png)

### Items Mobile

![Items page Mobile](static/images/items-mobile-wireframe.png)

### Items Details Mobile

![Item Details page Mobile](static/images/item-details-mobile-wireframe.png)

---

[Back to Top](#top)

## User Stories

User Stories can be found at [Masters](https://github.com/users/Richard-L4/projects/9) on my GitHub profile.

---

## Features

### Site Pages

- **Homepage**

    - The Green Jacket homepage features a striking hero image of a scenic golf course, emphasizing its “Masters Gifts” collection with a clear call-to-action to visit the pro shop. A clean navigation bar offers quick links to item categories, a search function, and account details, while a banner promotes free delivery on orders over £100. The footer provides social media icons and a copyright note, giving the page a polished, professional look.

![screenshot](static/images/home-page.png)

  **Favicon Icon**
  
  - The favicon icon is the famous colonial style clubhouse of Augusta National Golf Course.

![screenshot](static/images/clubhouse.jpg)

  **Items Page**

  - A page for users to browse the items on the site. Features include filters to narrow down the users preferences, and clickable items to go to the items detail page. Item deatils has a review section that can be added to by signed-in users, that also have an edit and delete function.

- Items page.
![screenshot](static/images/items-page.png)
- Item details page.
![screenshot](static/images/item-detail-log-out.png)
- Item details page with login reminder for non logged in users to "Save Item For Later".
![screenshot](static/images/item-detail-login-reminder.png)
- Bottom of Item details page for logged out users.
![screenshot](static/images/item-detial-btm-log-out.png)
- Top of Item details page for logged in users.
![screenshot](static/images/item-detail-log-in.png)
- Bottom of Item details page for logged in users.
![screenshot](static/images/item-details-btm-log-in.png)
- Leave a Review modal.
![screenshot](static/images/leave-a-review.png)
- Edit a Review page.
![screenshot](static/images/edit-review.png)
- Delete a Review page.
![screenshot](static/images/delete-review.png)
- Item image page.
![screenshot](static/images/item-image.png)
- Edit item page top.
![screenshot](static/images/edit-item-top.png)
- Edit item page bottom.
![screenshot](static/images/edit-iem-tbm.png)
- Delete item page.
![screenshot](static/images/delete-item.png)

---

- **Trolley and Checkout Pages**
    - Trolley page. Displays any items that the user has currenlty added to their shopping trolley. Has the option to increase or decrease the quantity of each item in the trolley, aswell as an option to remove the item completely.
    - Checkout Page. Displays the order summary so the user can double check what they are purchasing along with a payment details form for the name, address, phone number, email address and secure Stripe card payment form.

- Trolley toast to say item / s have been added to Trolley page.
![screenshot](static/images/go-to-trolley-toast.png)
- Trolley page.
![screenshot](static/images/trolley.png)
- Top of Checkout page.
![screenshot](static/images/checkout-top.png)
- Bottom of Checkout page.
![screenshot](static/images/checkout-btm.png)
- Checkout Success page.
![screenshot](static/images/checkout-success.png)


- **Who We Are Page**

    - Who We Are page. This page is the "Who We Are" section of the Green Jacket website. It introduces Masters Merchandise, describing its dedication to quality and tradition with classic Masters-style items. The page also provides contact information and displays the store's location on an embedded Google Map.

![screenshot](static/images/who-we-are.png)


- **Register Page**

    - Register Page. Displays a form that new users of the site can fill in and make an account. The form is short, simple, and clean to encourage users to use it.

![screenshot](static/images/sign-up.png)

- **Confirm Email Page**

![screenshot](static/images/confirm-email.png)

- **Login Page**

    - Login Page. Displays a login form that existing users can use to log in to the site. Two simple input fields for username and password make it easy for users to log in to their account. A Forgot Password link takes users to another page where they can recover their password.

![screenshot](static/images/login.png)


- **Profile Page**

    - Profile page. Displays a user's profile information. Lets a user see their relevant profile information in a clean and simple way, and contains an edit form that users can use to update their profile information. It also displays any current and previous orders they have with a link to view the details.

![screenshot](static/images/profile.png)

- **Logout Page**

    - Logout Page. A simple page confirming that the user has logged out of their account. Displays a log in again button in case the user wishes to log back in.

![screenshot](static/images/log-out.png)


- **Custom 404 / 500 error Pages**

    - Custom error 404 page. This displays a simple error page that lets the user know that there has been an error loading the url with a button to take them back to the home-page of the site.

    - Custom error 500 page. This displays a simple error page that lets the user know that there has been an error loading the url with a button to take them back to the home-page of the site.

![screenshot](static/images/404-page.png)

![screenshot](static/images/500-page.png)

   **Change Password Page**

![screenshot](static/images/change-password.png)

   **Forgot Password Page**

![screenshot](static/images/forgot-password.png)

   **Password Reset Page**

![screenshot](static/images/password-reset.png)

   **Bad Token Page (reset-password-from-key)**


The `password_reset_from_key.html` template is shown when you visit the unique password reset link sent to your email.

- If the link (token) is **valid**, it shows the form to set a new password.
- If you have **already used the link once** (e.g., you changed the password successfully), and then try to use the same link again (by going back to the email), the token is no longer valid.  
  In this case, the **"Bad Token"** message appears, which comes from the `password_reset_from_key.html` template.


![screenshot](static/images/password-reset-from-key.png)

   **Verify Email Page**

![screenshot](static/images/verify-email.png)

---

## ✅ Functionality Test Table

| Page Name           | Feature / Button / Function               | Expected Outcome                                                | Actual Outcome |
|---------------------|-------------------------------------------|------------------------------------------------------------------|----------------|
| Home                | Navbar: Home                              | Redirects to homepage                                            | Passed         |
|                     | Navbar: Items                            | Redirects to item listing page                                  | Passed         |
|                     | Navbar: Login                             | Redirects to login page                                          | Passed         |
|                     | Navbar: Register                          | Redirects to registration page                                   | Passed         |
|                     | Navbar: Logout (when logged in)           | Logs out user and redirects to homepage                          | Passed         |
|                     | View Item link                           | Opens selected item’s detail page                               | Passed         |
| Items               | Add to Trolley button                    | Adds item to trolley and updates trolley icon/count             | Passed         |
| Item Detail         | Item image & description                 | Displays correct item information                               | Passed         |
|                     | Save for Later button (logged in only)    | Saves item to user’s saved list                                 | Passed         |
|                     | Leave Review form (logged in only)        | Submits review and displays it under the item                   | Passed         |
|                     | Edit Review button (author only)          | Opens review in edit mode                                        | Passed         |
|                     | Delete Review button (author only)        | Deletes user’s own review                                        | Passed         |
|                     | Review visibility (guest)                 | Guests can view all reviews                                      | Passed         |
| Trolley             | Update Quantity                         | Increases or decreases item quantity and updates total price     | Passed         |
|                     | Remove Item                             | Deletes item from trolley                                       | Passed         |
| Checkout            | Stripe Payment                          | Processes test payment using Stripe                              | Passed         |
|                     | Order Confirmation Page                 | Displays summary of order and payment status                     | Passed         |
|                     | Order Confirmation Email                | Sends order details to user’s email                              | Passed         |
| Account (Registered)| Profile Edit                            | Updates user profile and saves changes                           | Passed         |
|                     | Save for Later                          | Displays saved items                                            | Passed         |
| Admin Functions     | Add Item (front end)                    | Adds new item and shows in listing                              | Passed         |
|                     | Edit Item                              | Updates item details and saves changes                          | Passed         |
|                     | Delete Item                            | Removes item from the store                                     | Passed         |
| Forms               | Login / Register Forms                  | Validates inputs and redirects appropriately                     | Passed         |
|                     | Review / Profile Forms                  | Submits valid data and shows success/error messages              | Passed         |
| Navigation/Footer   | All links and icons                     | Route correctly and open in new tabs where applicable            | Passed         |
| All Pages           | Mobile Responsiveness                   | Scales appropriately on mobile, tablet, and desktop              | Passed         |
|                     | Touch Buttons & Tap Targets             | All clickable items work correctly on small screens              | Passed         |
|                     | Hover States / Visual Feedback          | Buttons and links highlight on hover/focus                       | Passed         |

---

[Back to Top](#top)

---

## 🎨 UX Principles Behind the Features

The design of the Green Jacket e-commerce platform follows the Five Planes of User Experience to ensure usability, clarity, and satisfaction across all user roles:

### 🔹 Strategy
The site is strategically designed to provide a smooth, intuitive shopping experience. Key features—like guest checkout, item reviews, saved items, and streamlined Stripe integration—are implemented to support both user convenience and business goals.

### 🔹 Scope
The platform enables users to browse and buy items easily, "save items for later", and leave feedback through reviews. Registered users benefit from personalised profiles, while admins can manage inventory directly from the front end—all within the defined scope of a lightweight, general goods store.

### 🔹 Structure
Navigation is clear and predictable, guiding users from item listings to detail views, the trolley, and a secure checkout process. Interaction flows—such as saving items or leaving reviews—are logically placed and easy to follow.

### 🔹 Skeleton
The interface is minimal and intuitive, focusing on usability. Key actions like “Add to Trolley,” “Save for Later,” and “Checkout” are visually distinct and mobile-optimised, ensuring quick access with minimal cognitive load.

### 🔹 Surface
Visually, the site uses consistent styling, readable typography, and calming colours to build trust. Elements such as buttons, review sections, and checkout summaries use subtle hover states and clear visual hierarchy to guide user focus.

---

By designing with these UX principles in mind, the Green Jacket platform creates a seamless and satisfying experience for all users—from first-time guests to returning customers and site administrators.


## 🧪 Manual Testing

Each major feature of the Green Jacket e-commerce site was manually tested to ensure it functioned as intended. This included:

### 🛍️ Item Listing and Detail Pages
- **Item Listing Page:** Items display in a responsive grid layout. All item images, names, and "View Details" links were tested for accurate routing to individual item pages.
- **Item Detail Page:** Shows item image, description, price, reviews, and interactive buttons (add to trolley, save for later). All display elements and links were tested for accuracy.

### 🛒 Trolley and Checkout Pages
- Adding and removing items from the trolley was tested for proper quantity updates and total price calculations.
- Stripe checkout was tested using test card credentials to simulate successful payments.
- Confirmation page correctly displays order summary.
- Order confirmation email was received after checkout.

### 👥 User Account Features
- **Registration and Login:** Tested for proper form validation, password confirmation, and error handling.
- **Profile Creation & Editing:** Verified that users can update their information and that changes persist across sessions.
- **Save for Later:** Items could be saved and removed successfully.
- **Reviews:** Logged-in users could add, edit, and delete their own reviews. Validation and error messages functioned correctly.

### ⚙️ Admin Functionality (Front End)
- Admin users successfully accessed front-end item management features to add, edit, and delete items.
- Item updates appeared in real time and routed correctly across the site.

### 🔁 Forms
All forms (Login, Registration, Review, Profile) were tested for:
- Input validation and error messaging
- Correct routing upon submission
- Data persistence after successful input

### 🔗 Navigation and Footer
- All navigation links, logo redirects, and footer elements were manually tested for correct routing.
- Social icons and contact links opened the correct destinations in new tabs when applicable.

---

## 📱 Responsiveness Testing

- Site tested manually using Google Chrome and Mozilla Firefox.
- Layout and features checked across screen sizes:
  - Mobile (320px–480px)
  - Tablet (768px)
  - Desktop (1024px+)
- Developer tools used to simulate various devices and orientations.
- All interactive elements (buttons, forms, navigation) were tested for touch friendliness and proper scaling.

---

### Bugs Found and Fixes

| Bug Description | Fix Applied | Status |
|------------------|-------------|--------|
| In "Who We Are" I had this "main class="container-fluid class", which I thought would be a good way to apply a CSS style to customize the footer, BUT it caused a transparent ovelay which prevented link icons from working across the site.| My mentor explained the class was too generic and I needed to create a specific class . The solution, add "about" to the class "main class="container-fluid about". | Fixed |

**Note on Documentation**:  
Due to the focus of the development of the site, and uncertanty as to the scale of bugs (whether very minor, or more complex), screenshots of bugs were not taken. However, descriptions and outcomes of each fix have been recorded.

---

## 🗃️ Data Models

This project uses Django ORM with the following data models and relationships.

---

### 👤 User & UserProfile

- `User` — Django’s built-in authentication model.  
- `UserProfile` — Extends the User model with default delivery information and links to orders.

**Fields:**
- `user` (OneToOneField to `User`)
- `default_phone_number`
- `default_street_address1`
- `default_street_address2`
- `default_town_or_city`
- `default_county`
- `default_postcode`
- `default_country`

---

### 📦 Item

Items available in the store.

**Fields:**
- `category` (ForeignKey to `Category`)
- `sku`
- `name`
- `description`
- `has_sizes` (Boolean)
- `price`
- `featured_image`

**Relationships:**
- One item can:
  - Appear in many `OrderLineItem`s  
  - Be saved by many users (`SavedItem`)  
  - Have many `Review`s

---

### 🏷️ Category

Organizes items into sections.

**Fields:**
- `name`
- `friendly_name`
- `parent` (self-referencing ForeignKey for subcategories)

---

### 🛒 Order

Represents a completed user purchase.

**Fields:**
- `user_profile` (ForeignKey to `UserProfile`)
- `full_name`
- `email`
- `phone_number`
- `street_address1`
- `street_address2`
- `town_or_city`
- `county`
- `postcode`
- `country`
- `order_number` (UUID)
- `date`
- `order_total`
- `delivery_cost`
- `grand_total`
- `original_trolley` (JSON snapshot)
- `stripe_pid`

---

### 📦 OrderLineItem

Represents an individual item in an order.

**Fields:**
- `order` (ForeignKey to `Order`)
- `item` (ForeignKey to `Item`)
- `item_size`
- `quantity`
- `lineitem_total`

---

### ❤️ SavedItem

Allows users to save items for later (wishlist-like feature).

**Fields:**
- `user` (ForeignKey to `User`)
- `item` (ForeignKey to `Item`)
- `saved_at` (auto timestamp)

**Constraints:**
- A user can only save each item once (unique constraint on `user` + `item`)

---

### 📝 Review

User-written reviews for items.

**Fields:**
- `user` (ForeignKey to `User`)
- `item` (ForeignKey to `Item`)
- `review_text`
- `created_at`
- `updated_at`

**Constraints:**
- A user can only review an item once (unique constraint on `user` + `item`)

---

## 🔗 Entity Relationship Summary

| Model A       | Relationship        | Model B                 |
|---------------|---------------------|--------------------------|
| User          | One-to-One          | UserProfile              |
| UserProfile   | One-to-Many         | Order                    |
| Category      | One-to-Many         | Item                     |
| Category      | One-to-Many (self)  | Category (subcategories) |
| Item          | One-to-Many         | OrderLineItem            |
| Item          | One-to-Many         | SavedItem                |
| Item          | One-to-Many         | Review                   |
| Order         | One-to-Many         | OrderLineItem            |
| User          | One-to-Many         | SavedItem                |
| User          | One-to-Many         | Review                   |

---

  **Entity Relationship Diagram (ERD)**

![Alt text](static/images/ERD.png "ERD")

---

## Database Schema

### User
| Field       | Type     | Description              |
|-------------|----------|--------------------------|
| id          | PK       | Primary Key              |
| username    | String   | Unique username          |
| email       | String   | Email of the user        |
| password    | String   | Hashed password          |
| first_name  | String   | User’s first name        |
| last_name   | String   | User’s last name         |
| is_active   | Boolean  | Whether the user is active |
| date_joined | DateTime | Timestamp when user joined |

---

### UserProfile
| Field                  | Type     | Description                       |
|------------------------|----------|-----------------------------------|
| id                     | PK       | Primary Key                       |
| user_id                | FK       | One-to-One link to User           |
| default_phone_number   | String   | Default phone number              |
| default_street_address1| String   | Default primary street address    |
| default_street_address2| String   | Default secondary street address  |
| default_town_or_city   | String   | Default town or city              |
| default_county         | String   | Default county                    |
| default_postcode       | String   | Default postal code               |
| default_country        | String   | Default country                   |

---

### Category
| Field        | Type      | Description                          |
|--------------|-----------|--------------------------------------|
| id           | PK        | Primary Key                          |
| name         | String    | Unique category name                 |
| friendly_name| String    | Display-friendly name                |
| parent_id    | FK (self) | Parent category (for subcategories)  |

---

### Item
| Field         | Type     | Description                          |
|---------------|----------|--------------------------------------|
| id            | PK       | Primary Key                          |
| category_id   | FK       | Foreign Key to Category              |
| sku           | String   | Unique stock-keeping unit identifier |
| name          | String   | Name of the item                     |
| description   | Text     | Description of the item              |
| has_sizes     | Boolean  | Whether the item has size variants   |
| price         | Decimal  | Price of the item                    |
| featured_image| String   | URL or path to featured image        |

---

### Order
| Field           | Type     | Description                          |
|-----------------|----------|--------------------------------------|
| id              | PK       | Primary Key                          |
| user_profile_id | FK       | Foreign Key to UserProfile           |
| full_name       | String   | Full name for the order              |
| email           | String   | Contact email                        |
| phone_number    | String   | Phone number                         |
| street_address1 | String   | Primary street address               |
| street_address2 | String   | Secondary street address             |
| town_or_city    | String   | Town or city                         |
| county          | String   | County                               |
| postcode        | String   | Postal code                          |
| country         | String   | Country                              |
| order_number    | UUID     | Unique order identifier              |
| date            | DateTime | Date the order was placed            |
| order_total     | Decimal  | Total price of the order             |
| delivery_cost   | Decimal  | Delivery cost                        |
| grand_total     | Decimal  | Order total + delivery               |
| original_trolley| JSON     | JSON snapshot of the cart            |
| stripe_pid      | String   | Stripe Payment Intent ID             |

---

### OrderLineItem
| Field          | Type     | Description                          |
|----------------|----------|--------------------------------------|
| id             | PK       | Primary Key                          |
| order_id       | FK       | Foreign Key to Order                 |
| item_id        | FK       | Foreign Key to Item                  |
| item_size      | String   | Size of the item (if applicable)     |
| quantity       | Integer  | Quantity of the item                 |
| lineitem_total | Decimal  | Total cost for this line item        |

---

### SavedItem
| Field       | Type     | Description                          |
|-------------|----------|--------------------------------------|
| id          | PK       | Primary Key                          |
| user_id     | FK       | Foreign Key to User                  |
| item_id     | FK       | Foreign Key to Item                  |
| saved_at    | DateTime | Timestamp when saved                 |
| **Constraint** | Unique (user_id, item_id) | A user can save an item only once |

---

### Review
| Field       | Type     | Description                          |
|-------------|----------|--------------------------------------|
| id          | PK       | Primary Key                          |
| user_id     | FK       | Foreign Key to User                  |
| item_id     | FK       | Foreign Key to Item                  |
| review_text | Text     | Review content                       |
| created_at  | DateTime | Creation timestamp                   |
| updated_at  | DateTime | Last updated timestamp               |
| **Constraint** | Unique (user_id, item_id) | A user can review an item only once |
  
---

## Languages Used

- **HTML**:  
  Used for the main site content, including the structure of each page.
  
- **CSS**:  
  Used for the main site design and layout, providing styling for elements like headings, text, images, and buttons.
  
- **JavaScript**:  
  Used for user interaction on the site, adding interactivity like form validation and dynamic content changes.
  
- **Python**:  
  Used as the back-end programming language, handling server-side logic, database operations, and dynamic content generation.

---  

### Future Features

- 🔹 **Most Popular**  

Users will see a visual  image to let them know which item is the most popular per category.

- 🔹 **Suggested Purchases**  

Users will receive an adive suggestion of other simialr items that others users have purchased based on what they have bought.

- 🔹 **Newsletter subscription** 
 
Users can sign up to receive regular email updates with new offers and for a varying subscription fee get discounts of either individual items and or bulk buys.

---

## Deployment

The live deployed application can be found deployed on [Heroku](https://green-jacket-club-904896471b2f.herokuapp.com/).

### Cloudinary 

The site uses [Cloudinary](https://cloudinary.com/) to host all static files due to the fact that Heroku cannot.

Follow these steps in order to use Cloudinary.

Create a Cloudinary account:

- Go to Cloudinary and sign up for a free account.

- After signing up, you'll be provided with an API Key, API Secret, and Cloud Name, which you'll need to integrate Cloudinary into your Django project.

Install the Cloudinary package: 
- In your terminal, run the following command to install the Cloudinary Python package: `pip install cloudinary`

Update settings.py: 
- In your Django project, open settings.py and add 'cloudinary' to the INSTALLED_APPS list:
    ``` 
    INSTALLED_APPS = [
    ...
    'cloudinary',
    ]
    ```
Add Cloudinary credentials
- Add the following Cloudinary configuration with your Cloud Name, API Key, and API Secret from your Cloudinary account.

Update Models to Use CloudinaryField
- Cloudinary's CloudinaryField will allow you to store images and files in Cloudinary directly from your Django models.

Migrate Changes made to any models

Configure Media Files in Production
- Set up Heroku environment variables: Add the Cloudinary credentials to your Heroku app’s config vars

---

[Back to Top](#top)

## Validations

For details about input validations, see [Validations and Lighthouse Testing](./validations.md).

---

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the drop-down menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA) and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars** and set your environment variables.

| Key | Value |
| --- | --- |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | user's own value |
| `CLOUDINARY_API_KEY` | user's own value |
| `CLOUDINARY_API_SECRET` | user's own value |
| `CLOUDINARY_URL` | user's own value |
| `EMAIL_HOST_PASS` | user's own value |
| `EMAIL_HOST_USER` | user's own value |
| `STRIPE_PUBLIC_KEY` | user's own value |
| `STRIPE_SECRET_KEY` | user's own value |
| `STRIPE_WH_SECRET` | user's own value |


Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs to be updated using:
- `pip freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
    - `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault('SECRET_KEY', "user's own value")
os.environ.setdefault('DEVELOPMENT', '1')
os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ["CLOUDINARY_CLOUD_NAME"] = "user's own value"
os.environ["CLOUDINARY_API_KEY"] = "user's own value"
os.environ["CLOUDINARY_API_SECRET"] = "user's own value"
os.environ.setdefault('STRIPE_PUBLIC_KEY', "user's own value")
os.environ.setdefault('STRIPE_SECRET_KEY', "user's own value")
os.environ.setdefault('STRIPE_WH_SECRET', "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python manage.py makemigrations`
- Migrate the data to the database: `python manage.py migrate`
- Create a superuser: `python manage.py createsuperuser`
- Load fixtures (if applicable): `python manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python manage.py runserver`

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/Richard-L4/Green_Jacket) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
    - `git clone https://github.com/Richard-L4/Green_Jacket`
7. Press Enter to create your local clone.


#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Richard-L4/Green_Jacket)
2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Stripe

[Stripe](https://stripe.com) was used to process the payments. The functionality for this came from the Boutique Ado walkthrough and I did not vary from that walkthrough. Stripe uses a published key and a secret key in order for it to work. The secret key is not something that is available but the creator. These keys are set in my Heroku config settings.

As in the walkthrough I tested Stripe by listening to events and creating payment intents. This works at the time of writing.

![stripe1](static/images/stripe.png)

### Stripe deployment

This project uses [Stripe](https://stripe.com) to handle the e-commerce payments.

Create a Stripe account and login, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://green-jacket-club-904896471b2f.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)


### Gmail - email confirmation

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for account verification and order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (verify your password and account)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
	- Any custom name, such as "Django" or web-piano-academy
- You'll be provided with a 16-character password (API key).
	- Save this somewhere locally, as you cannot access this key again later!
	- `EMAIL_HOST_PASS` = user's 16-character API key
	- `EMAIL_HOST_USER` = user's own personal Gmail email address

![stripe1](static/images/email-order.png)

  ## Credits & Acknowledgements

### All photo's

### [MMOGOLF](https://www.mmogolf.com/2025-masters/)

### [Masters.com](https://www.masters.com/index.html/)

### Entire site: [Bootstrap](https://getbootstrap.com)

### Entire site: [Django documentation](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#ref-templates-builtins-tags)

### Entire site: [Code institute walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+BA101N+5/courseware/4201818c00aa4ba3a0dae243725f6e32/d3188bf68530497aa5fba55d07a9d7d7/)

**Note:** Chat Gpt used for spelling and grammar checks as a result of increased Microsoft subscription charges, and as an aid for general troubleshooting suggestions.

---

### My mentor Brian Macharia for his continued support and guidance.

---

[Back to Top](#top)

---