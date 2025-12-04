# HTML Convert

The ultimate open-source solution for rendering HTML & CSS to any format. Self-host for complete control or use our managed cloud API for instant scalability.

## Features

- **Open Source Core**: Full access to the source code. Run it on your own infrastructure, customize it to your needs, and contribute back to the community.
- **Managed Cloud API**: Skip the DevOps. Use our high-performance, scalable API to convert HTML/CSS to images, PDFs, and more instantly.
- **Lightning Fast**: Optimized rendering engine ensures your conversions happen in milliseconds, not seconds.
- **Secure & Private**: Enterprise-grade security. Your data is processed securely and never stored longer than necessary.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation & Running

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/RuzDevSAS/htmlcsstoconvert.git
    cd htmlcsstoconvert
    ```

2.  **Run with Docker Compose:**

    This will build and start both the backend (FastAPI) and frontend (SvelteKit) services.

    ```bash
    docker-compose up --build
    ```

3.  **Access the application:**

    -   **Frontend**: Open [http://localhost:5173](http://localhost:5173) in your browser.
    -   **Backend API**: The API is available at [http://localhost:8000](http://localhost:8000).

## Project Structure

-   `backend/`: FastAPI application for handling conversions.
-   `frontend/`: SvelteKit application for the user interface.
-   `docker-compose.yml`: Docker Compose configuration for orchestrating the services.

## License

This project is licensed under the MIT License.
