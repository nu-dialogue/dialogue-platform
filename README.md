# Text-based Dialogue Platform
This repository provides a text-based dialogue platform that operates on the Web.
## Setup
Python == 3.8
1. Build web server using software like nginx.
2. Clone repository
  ```
  git clone https://github.com/nu-dialogue/dialogue-platform.git
  ```
3. Install libraries
  - These are the libraries required to use GPT-3.5/4. If you use another model, you need to install the library corresponding to that model.
  ```
  pip install -r requirements.txt
  ```
4. Set API key
  - Set your OpenAI API key to the environment variable `OPENAI_API_KEY`.
  ```
  export OPENAI_API_KEY="<Your API key>"
  ```
## Files
- `log/`: Directory for log output
- `server.py`: Script that manage Web server
- `gpt_bot.py`: Script that generates speech using GPT-3.5/4
- `interface.py`: Script that defines HTML of dialogue Interface
- `start.sh`: Shell script for execution

## Launch the dialogue platform
```
bash start.sh
```

## License
[LICENSE](/LICENSE)

