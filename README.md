
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://avatars.githubusercontent.com/u/117038620?s=200&v=4" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Spotify cover extractor</h3>

  <p align="center">
    An extractor of Spotify album covers!
    <br />
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project 💁‍♂️

The Spotify Album Cover Extractor is a Python script that allows you to retrieve album covers from Spotify and save them as image files. Whether you want to create a personal music library with album artwork or explore your favorite artists' visual styles, this script makes it easy to collect high-quality album covers from Spotify's extensive catalog.

![spotify-cover-extractor](assets/canvas.png)

### Built With ✏️
This scripts was developed using the next technologies:

* ![Python][python-logo]
* ![OpenCv][opencv-logo]
* ![NumPy][numpy-logo]


<!-- GETTING STARTED -->
## Getting Started 🏁

### Prerequisites 🤓

Before you can use this script, you need to have the following installed on your system:
- ``python3.x``
- ```pip``` (Python Package Manager)


## Installation 😎

The install time should be around 10 minutes. It works on Linux, MacOS and Windows. 

For *Linux / MacOS* users, this process needs to be done in the **<u>Terminal</u>**. 🐧
<br>
For *Windows* users, this process needs to be done in the **<u>Windows Powershell</u>**. 🪟

1. Clone the repo.
   ```shell
   git clone https://github.com/VladTomici14/spotify-cover-extractor.git
   ```
2. Navigate to the script's directory location through the terminal.
    ```shell
    cd path/to/spotify-cover-extractor
    ```
3. Install **<u>OpenCV</u>**.
   ```shell
   pip install opencv-python
   ```
4. Install **<u>SpotiPy</u>**.
    ```shell
    pip install spotipy
    ```
5. Install **<u>NumPy</u>**.
    ```shell
    pip install numpy
    ```
6. Connect Spotify Developer to your Spotify account by [logging in or creating a free Spotify account here](https://developer.spotify.com/dashboard/).
7. Once in your dashboard, click the green “Create a Client ID” button to fill out the form to create an app or hardware integration.

![spotify create id](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ASxI3G0SoGb49nnTZMLUdA.png)

10. Create a new file named `credentials.py`.
11. Add the next class in the `credentials.py` file. Change the values to your API keys from the Spotify Developer platform.
    ```python
    class CREDENTIALS:
     SPOTIPY_CLIENT_ID = "YOUR_CLIENT_ID"
     SPOTIPY_CLIENT_SECRET = "YOUR_CLIENT_SECRET_ID"
     SPOTIPY_REDIRECT_URI="https://www.google.ro/"
    ```
12. Done ! 🥳

<!-- USAGE EXAMPLES -->
## Usage 🛠️

To use the script, all you need to do is run the ```main.py``` file. 

```sh
python3 main.py
```

After that, you need to paste the link of the album that you want to import.
```shell
enter the album link: 
```

The cover of the album will be downloaded as an image into the `/covers` directory. 


[python-logo]: https://img.shields.io/badge/python-0769AD?style=for-the-badge&logo=python&logoColor=white
[opencv-logo]: https://img.shields.io/badge/opencv-DD0031?style=for-the-badge&logo=opencv&logoColor=white
[numpy-logo]: https://img.shields.io/badge/numpy-0769AD?style=for-the-badge&logo=numpy&logoColor=white
