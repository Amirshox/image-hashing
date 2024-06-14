# Image Hashing API

This FastAPI application provides an easy and efficient way to compute perceptual hash values for images, which can be
useful for detecting similar images or ensuring image integrity. This project is structured to be both simple and
extensible.

## Features

- **Perceptual Image Hashing**: Uses `phash` algorithm from the `imagehash` library to generate perceptual hashes of the
  images.
- **FastAPI Framework**: Utilizes FastAPI for efficient and easy to set up API endpoints with automatic interactive API
  documentation.
- **Environment Variable Management**: Uses python-dotenv to manage environment variables, allowing for flexible
  configuration.

## Installation

Before running the application, ensure you have Python installed on your system. You can then install the required
dependencies by following these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd image-hashing
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

The application uses environment variables for configuration. Set the path to where your media files are stored using
the MEDIA_PATH variable.

1. Copy the example.env file to .env:
    ```bash
        cp example.env .env
   ```
2. Edit the .env file to set your environment variables:

MEDIA_PATH=media # Directory where images will be stored

## Running the Application

To start the FastAPI application, run the following command:

```bash
uvicorn main:app
```

if you want to run application in other port, you can use the following command:

```bash
uvicorn main:app --port 8000
```

## Usage

Once the server is running, you can access the API in your web browser at http://127.0.0.1:8000/docs. This will display
the automatic interactive API documentation provided by FastAPI's Swagger UI.

Endpoints

* GET /: Returns a simple Hello World message.
* POST /image/hash: Computes the hash of an image file. You need to send a JSON request with the path to the image file:

```json
{
  "path": "path/to/your/image.jpg"
}
```