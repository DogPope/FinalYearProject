[Pathfinding Algorithms Article by Medium](https://medium.com/@sampeach/how-to-use-pathfinding-algorithms-with-satellite-images-part-1-4faf429e091e)  
[Part Two of the above Article](https://medium.com/@sampeach/how-to-use-pathfinding-algorithms-with-satellite-images-part-2-77562d4a94f3)  
[Elevation API from Google](https://developers.google.com/maps/documentation/elevation/start)  
[Drones to support Search and Rescue](https://www.researchgate.net/publication/370695486_Drone_Swarms_to_Support_Search_and_Rescue_Operations_Opportunities_and_Challenges)  
[Search and Rescue using UAVs](https://www.sciencedirect.com/science/article/abs/pii/S095741742100378X)  
[Ecological Impact Report](https://www.tii.ie/media/yuzcxigv/waterville-bridge-reactive-maintenance-works-natura-impact-statement.pdf)

[Not sure if this is relevant, but it's interesting regardless.](https://www.technolynx.com/post/reinventing-pathfinding-with-ai-driven-navigation-systems)  
[Something similar to what I'm trying to do](https://www.technologyreview.com/2024/05/30/1092988/ai-directed-drones-could-help-find-lost-hikers-faster/)  
[This one contains useful information on Photogrammetry](https://ikarus3d.com/media/3d-blog/the-comprehensive-guide-to-aerial-photogrammetry/)

## For Maps
[GeoHack. Summit of Carrauntoohil](https://geohack.toolforge.org/geohack.php?pagename=Carrauntoohil&params=51.999445_N_9.742693_W_type:mountain_scale:100000)  
[Distance Calculator](https://latlongdata.com/distance-calculator/)

## Useful 3D map stuff
[Elevation API](https://elevationapi.com/about) Mostly does 3d maps. Could be useful regardless.

## Elevation APIs
[Elevation-API Europe](https://www.elevation-api.eu)
`curl 'https://www.elevation-api.eu/v1/elevation/lat/lng?json'`
Rate: Less than TEN PER SECOND. That would take forever for any major project.  
[Open-Elevation](https://www.open-elevation.com/) Didn't work when I last tried it. Maybe some other time.  
[Actual Dataset on Elevations](https://srtm.csi.cgiar.org/)  
[Open-Mateo](https://open-meteo.com/en/docs/elevation-api) Only 10000 calls per day. Final estimate 16 days.  
[Open-Topo-Data](https://www.opentopodata.org/) Okay, this ones even worse. 1000 calls per day. Would be finished in 160 days, or 5 months.  