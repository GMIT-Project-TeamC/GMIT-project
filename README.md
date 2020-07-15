# GMIT Project 
Describe the effect of covid on the market

# To run locally
Apply a free api key from [alpha vantage](https://www.alphavantage.co/) and save it in the main dir with name `api_key`

# Add dependencies 
Ideally in a virtualenv
``` zsh
pip install requirements.txt
```

# Add environment variable
To run, you should have a file named `api_key` containing your api key. Then in the terminal do the following.
```zsh
export API_KEY = api_key
jupyter notebook
``` 