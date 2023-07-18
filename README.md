# Streamlit frontend for DQMonstersDB-FastAPI

## Intro - What is Dragon Quest Monsters?
Dragon Quest Monsters is a spin-off series based on the famous JRPG series, 
Dragon Quest. This database informs the user of game details (monsters, skills, 
items, etc.) of [Dragon Quest Monsters -- Terry's Wonderland](https://en.wikipedia.org/wiki/Dragon_Warrior_Monsters)
(also known as Dragon Warrior Monsters in the US). 

Released in Japan in 1998 for the Gameboy Color by Enix, it was compared to the 
Pokemon series due to their similar gameplay of taming and training monsters 
to battle other monsters via random encounters. However, gameplay differs with
its roguelike dungeon levels, the battle play, and the breeding system. 

The game is quite old and not many copies are in circulation. The current way 
to play the game is to buy "Dragon Quest Monsters -- Terry's Wonderland RETRO"
for the Nintendo Switch on the Japanese Nintendo eShop or on Google Play and 
Apple Store by setting your region to Japan (the game will be in Japanese). 
Otherwise, use an emulator and download the English version or buy a physical
cartridge.

## Project Description

This repository is the frontend for the DQMonstersDB FastAPI project 
<https://github.com/cmsato09/DQMonstersDB-API> using 
[Streamlit](https://streamlit.io/), a minimal open-source python framework 
primarily used to build and share data apps quickly. However, it can be used to 
create a quick frontend for anything in python. 

This framework was recommended to me to get a mvp out as soon as possible, 
rather than learning Javascript and React from the beginning (and most likely 
struggling through it and being frustrated about not getting the app out there). 
This way I can get feedback about the data being displayed. 

I am planning on eventually learning more about frontend using React and 
remaking the frontend.

## How to Run
This repo is deployed on [Streamlit Cloud](https://docs.streamlit.io/streamlit-cloud).

Go to https://dqmonstersdb.streamlit.app to access the app online.

![Homepage](image_readme/streamlit-screenshot-1.jpg)
![Monster Detail Page](image_readme/streamlit-screenshot-2.jpg)

## How to Run Locally 
### Run Streamlit repo locally using hosted FastAPI 
1. Clone this repo 
2. In the `helper_functions.py` file, make sure the line
`API_BASE = "https://dqmonstersdbapi-1-a1113227.deta.app"` is uncommented.
3. Run `streamlit run Home.py` in the terminal
4. The Streamlit app should automatically open http://localhost:8501 on your 
local browser. If not, type or copy/paste the address into your browser
of choice.

### Run both FastAPI and Streamlit locally
1. Clone both FastAPI [repo](https://github.com/cmsato09/DQMonstersDB-API) and 
this repo onto your local machine. 
2. Install all dependencies on virtual environment
3. Run `create_database.py` in the terminal to make the sqlite database from 
the csv files. `database.db` file should be generated.
4. Locally run FastAPI app
   1. Run `uvicorn main:app` in the terminal
   2. FastAPI should be running locally at http://127.0.0.1:8000 (or 
   http://localhost:8000)
   3. Go to http://127.0.0.1:8000/docs to access the interactive API 
   documentation using Swagger UI
5. Locally run Streamlit app
   1. Open new terminal for streamlit folder 
   2. In the `helper_functions.py` file, make sure the line pointing to deta,
   `API_BASE = "https://dqmonstersdbapi-1-a1113227.deta.app"` is ***commented***, and 
   `API_BASE = "http://localhost:8000"` is **uncommented**.
   3. Run `streamlit run Home.py` in the terminal
   4. The Streamlit app should automatically open http://localhost:8501 on your 
   local browser. If not, type or copy/paste the address into your 
   browser of choice.
   5. FastAPI must simultaneously run with the Streamlit app

## Resources used to make project
- Streamlit documentation <https://docs.streamlit.io/>
- community forum <https://discuss.streamlit.io/> 
- issues tab on the streamlit github repo
- python [pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html#user-guide) 

## Credits
This project was done with help and mentoring by [Bob Belderbos](https://github.com/bbelderbos) 
through the [Pybites Developer Mindset Program](https://pybit.es/catalogue/the-pdm-program/)

Thank you Bob for the support and help for making it fun to learn, struggle 
through, and just figuring it out.   
