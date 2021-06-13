# Web Scraping Homework - Mission to Mars
### File Shortcuts
* Jupyter Notebook: [mission_to_mars.ipynb](mission_to_mars.ipynb)
* Screenshots of final application 
* HTML template: [index.html](templates/index.html)
____________________________________________________________________________________________________________________________________________________________________
### Instructions
1. Scraping NASA Mars News
* Scrape the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

2. Scraping JPL Mars Space Images 
* Visit the url for the Featured Space Image site [here](https://spaceimages-mars.com).
* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
* Make sure to find the image url to the full size `.jpg` image.
* Make sure to save a complete url string for this image.

3. Mars Facts
* Visit the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.
* You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

4. MongoDB and Flask Application
* Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
5. Submit
