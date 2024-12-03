# FinalYearProject
This Repository contains the documentation for my Final Year Project.

# Project Title
Missing Persons Route Optimisation.

This project is going to use various technologies to assess the nearby terrain where a person went missing to come up with a viable route to rescue the injured/lost party.

## Literature to Consider
Actually, as mad as it sounds, Mt. Chilliad from GTA 5 may prove useful as data sets probably already exist. Think 'already completed' model, not a custom approach.

To-Do List
- [x] Draw a bounding box around the summit of Carrauntoohil to set a search area.
- [x] Break the bounding box down into a 2d array of coordinates to create a 3d model.
- [x] Write a 2D Python Array to call the Google Elevation API for each point in the above bounding box.
- [x] Research algorithms for navigating 3d spaces. Some done, but more to do.
- [x] Research Libraries for 3D routes and n planning.

## API Pricing
![API Pricing](Screenshots/ElevationApiPricing.PNG)

## Links and Resources
[Point Cloud Visualization Python](https://learngeodata.eu/visualise-massive-point-cloud-in-python/)
[Pathfinding over 3D spaces](https://ascane.github.io/assets/portfolio/pathfinding3d-report.pdf)
[Artificial Intelligence - Modern Applications or something](https://aima.cs.berkeley.edu/)

The bulk of this project as it exists already is in apiCalls.ipynb.

Stadia Maps Elevation [API Pricing](https://stadiamaps.com/pricing/#credit-schedule)
5 credits per request at 200,000 free credits.
[gpxz.io](https://www.gpxz.io/#pricing)