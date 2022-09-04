## Assignment 

## Project Goal
To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

### Functionality

- API to constantly fetch Youtube search data every 10 seconds and store in database
- GET API to display video details with options like searching, sorting & pagination
- Search API to search video details according to title or description
- Dockerize the project.

### Development

1. Clone the project

`git clone https://github.com/karankhiani1109/youtube-search.git `

2. COPY keys to `config.py`

```
# Youtube API key
YOU_TUBE_DATA_API_KEY = 'AIzaSyB6_8ULZDIhVMGEogqAne_PNhZSk7TpgR0'

# Pagination page per limit(default)
PER_PAGE_LIMIT = 12 

```
3. Run
### Running with Docker Compose

To run the application
` docker-compose up `

To again build the image
` docker-compose build `

To stop the application
` docker-compose down `



4. Navigate to `http://127.0.0.1:5000` to see the app live

5. RUN the API ` http://127.0.0.1:5000/api ` to call YouTube API asyc with multiple threading and populate database with video details

6. RUN the GET API ` http://127.0.0.1:5000/videos ` to get video details with pagination

7. RUN the POST API ` http://127.0.0.1:5000/videos/filter_submit ` to filter out paginated videos with input search query
