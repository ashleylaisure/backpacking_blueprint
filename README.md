# Backpacking Blueprint

#### Planning a thru-hike is exciting, but it can also be overwhelming. From finding the right trails to organizing gear, food, and resupply points, there’s a lot to keep track of. That’s where Backpacking Blueprint comes in.

Backpacking Blueprint is a comprehensive app designed for thru-hikers of all levels. Whether you're preparing for your first long-distance trek or your tenth, Backpacking Blueprint helps you simplify and streamline every part of the planning process.

![HomePage](https://file.notion.so/f/f/3b8dbac4-16cd-4f00-aab2-bad15b564ddb/c03f5cea-a55d-4b5a-b49b-36e4f72acdce/Screenshot_2025-06-16_171029.png?table=block&id=21413342-6c96-80ef-b060-e3cdd9bc431b&spaceId=3b8dbac4-16cd-4f00-aab2-bad15b564ddb&expirationTimestamp=1750456800000&signature=dAMkPmeMFskqJUIGyt38f55ULCZPQgAFRW6zJX480Ow&downloadName=Screenshot+2025-06-16+171029.png)
![Trail Details](https://file.notion.so/f/f/3b8dbac4-16cd-4f00-aab2-bad15b564ddb/0971e03b-61c7-47a0-b199-76326763c850/Screenshot_2025-06-16_171057.png?table=block&id=21413342-6c96-8014-b4f8-efbc4d6f7860&spaceId=3b8dbac4-16cd-4f00-aab2-bad15b564ddb&expirationTimestamp=1750456800000&signature=AGA4YeMQCixHUe6HH-psxUldpt3WBrDTvpIDVd0r-eo&downloadName=Screenshot+2025-06-16+171057.png)
![Gear Breakdown](https://file.notion.so/f/f/3b8dbac4-16cd-4f00-aab2-bad15b564ddb/06be6d2a-cb4e-4cb0-a2b6-9f208a1fbcd4/Screenshot_2025-06-16_171117.png?table=block&id=21413342-6c96-801f-8ebd-ffa0dd543d94&spaceId=3b8dbac4-16cd-4f00-aab2-bad15b564ddb&expirationTimestamp=1750456800000&signature=tPdnciKZHjfPZaEa0zUjrv4Wt6ADKxwHuATkZ2cGzKE&downloadName=Screenshot+2025-06-16+171117.png)

## Description

Growing up in Colorado, I developed a deep love for the outdoors and backpacking. It's something I’ve always wanted to do more of, but the stress of everyday life often makes planning a hiking trip—especially those lasting 3 to 5 days or even up to 3 weeks—feel overwhelming.

That’s what inspired me to create this app: a tool to take the stress out of trip planning and make it easier to actually get outside. With this app, you can organize all the small but important details—from coordinating travel to and from the trailhead, mapping out campsites, packing the right gear, and figuring out how much food you can realistically carry.

My hope is that this app empowers people to design their own adventures and finally get out there, instead of just dreaming about it.

## Table of Contents

- [Technologies Used](#technologiesused)
- [Features](#features)
- [Design](#design)
- [Project Next Steps](#nextsteps)
- [Deployed App](#deployment)
- [Contributors](#contributors)

## <a name="technologiesused"></a>Technologies Used

- **Django** – A high-level Python web framework that encourages rapid development and clean, pragmatic design. Django handles the backend logic, routing, authentication, and integrates seamlessly with the PostgreSQL database.

- **PostgreSQL** - A powerful, open-source object-relational database system used to store and manage application data efficiently and securely.

- **Python3** - 
- **JavaScript** - Adds interactivity to the frontend—for example, dynamic forms, animations, and responsive UI behavior.
- **CSS** - Used to style the application’s UI, ensuring a clean and responsive design across devices.
- **HTML5** - The standard markup language used to structure the web pages and content of the application.

- **@mapbox/mapbox-sdk** – Mapbox SDK for mapping services
---

## Features

 **User Authentication**
  - Django built in user authentication system
  - Django CSRF
  - Sign up as a new user
  - Log in with an existing account

**Hiking Adventure Management**
  - Create a new Adventure
    - Input: Name, start & end date.
    - Optional: Start location, total distance, elevation gain
    - Choose a cover image from a preset list (future: upload or Unsplash integration).
  - After creation, users are redirected to the Adventure Dashboard with:
    -Trip details
    -Interactive trailhead map
    -Auto-generated itinerary
    -Packing list
    -Navigation overview
  - Full CRUD functionality for each trip (Create, Read, Update, Delete).

**Main Features**
🗓 Itinerary
  - Add daily details: start/finish location, distance, elevation gain.
  - Notes section per day.
  - Locations auto-update on the main trail map.

🎒 Gear
  - Catalog and manage gear inventory.
  - Track brand, purchase link, price, ownership, and weight
  - Full CRUD on each item.
  - Assign/remove gear per trip (many-to-many relationship).
  - Backend converts all weights to pounds and calculates total gear weight.
  - Packing list reflects added gear with checkboxes for tracking.

🥾 Meal Plan (Pantry)
  - Store and manage favorite hiking foods.
  - Full CRUD for food items.
  - Auto-generated daily meal plan per adventure.
  - Add meals per day; automatic calorie & weight (lbs) calculations.
  - Helps balance nutritional needs with manageable carry weight.


## Wireframe Images

![WireFrames](https://file.notion.so/f/f/3b8dbac4-16cd-4f00-aab2-bad15b564ddb/58af2af8-161e-432d-8a24-545cc8261183/image.png?table=block&id=20813342-6c96-80f8-a587-d15eff90261e&spaceId=3b8dbac4-16cd-4f00-aab2-bad15b564ddb&expirationTimestamp=1750456800000&signature=TEfkH4TUbZuNlmga10Ikel1e8SFAHKHn9r_JL-wzhvA&downloadName=image.png)

## ERD

![dbStructure](https://file.notion.so/f/f/3b8dbac4-16cd-4f00-aab2-bad15b564ddb/0190afb5-4922-4dbd-844c-7baa716c1b67/image.png?table=block&id=21113342-6c96-801d-a090-d2fbf633f576&spaceId=3b8dbac4-16cd-4f00-aab2-bad15b564ddb&expirationTimestamp=1750456800000&signature=uFW-CQHAxhBvMb5ibMIVhHeFDdUSC6t__M0QICYEq6Q&downloadName=image.png)


## Notion Planning

🔗 [Notion Planning Board](https://www.notion.so/Backpacking-Blueprint-201133426c968053b415dc500678ebc5?source=copy_link)

## <a name="nextsteps"></a>Project Next Steps

#### Planned Features

- **User Profile & Dashboard**
  - View all upcoming tasks and trip overviews.
  - Bucket List & Countdown
  - Track future adventures.
- **Documents & Reservations**
  - Document Organizer
  - Store permits, reservations, etc.
  - Manage logistics to/from trailheads.
- **Trip Budgeting**
  - Expense and cost tracking per trip.
- **Sync & Share**
  - Collaborate with fellow travelers by sharing your trip plans
  - Let friends and family at home view your itinerary and preparations
  
****
#### Hiking API Integration

- **Search by campsite, trailhead, or location**
- **Add a new Adventure from search results**
- **Auto Sync location with itinerary**
- **topographic maps and offline sync**


## <a name="deployment"></a>Deployed Link

- [Backpacking Blueprint](https://backpacking-blueprint.onrender.com/)

# Github Repositories

[backpacking_blueprint](https://github.com/ashleylaisure/backpacking_blueprint.git)


## <a name="contributors"></a>Contributors

### Ashley Laisure - Lead Developer

- [LinkedIn](www.linkedin.com/in/ashley-laisure-6a9475354)

- [Github](https://github.com/ashleylaisure)

## Works Cited:

- [How to Create Signals](https://www.geeksforgeeks.org/how-to-create-and-use-signals-in-django/)
- [Mapbox](https://docs.mapbox.com/help/getting-started/map-developer-journey/)
- [Django Calculations](https://www.youtube.com/watch?v=oHJF9mfswzo)
- [Todo Checkbox](https://www.google.com/search?q=django+todo+checbox+done&sca_esv=5c42990244f538cb&sxsrf=AE3TifPS-YVdOUb3c0Qyf26ikDl2nDHwIQ%3A1749648470145&source=hp&ei=VoRJaPveBqrT5NoPkYuaqAc&iflsig=AOw8s4IAAAAAaEmSZiJY_vt57vZtmKWVmru3mxokqT5j&ved=0ahUKEwj74au8vOmNAxWqKVkFHZGFBnUQ4dUDCBk&uact=5&oq=django+todo+checbox+done&gs_lp=Egdnd3Mtd2l6IhhkamFuZ28gdG9kbyBjaGVjYm94IGRvbmUyBxAhGKABGAoyBxAhGKABGApIikZQAFi-PnAAeACQAQCYAaYBoAG9EaoBBDE4Lja4AQPIAQD4AQGYAhigApYSwgIEECMYJ8ICChAjGIAEGCcYigXCAgsQLhiABBjRAxjHAcICERAuGIAEGLEDGNEDGIMBGMcBwgIIEAAYgAQYsQPCAhEQABiABBixAxiDARjHAxiKBcICDhAuGIAEGLEDGNEDGMcBwgILEAAYgAQYsQMYgwHCAggQLhiABBixA8ICCxAuGIAEGLEDGIMBwgILEC4YgAQYsQMY5QTCAgUQABiABMICBRAuGIAEwgIGEAAYFhgewgIIEAAYgAQYogTCAgUQIRigAcICBRAhGJ8FwgIHECEYChirApgDAJIHBDE3LjegB__6AbIHBDE3Lje4B5YSwgcGMC4xNi44yAdE&sclient=gws-wiz)
