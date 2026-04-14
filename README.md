Running the program.
```sh
uv run python src/main.py
```

Symlink the configuration.
```sh
ln -sf "$(pwd)/config/com.hugohulsebosch.robocurtain.plist" ~/Library/LaunchAgents/com.hugohulsebosch.robocurtain.plist
launchctl load ~/Library/LaunchAgents/com.hugohulsebosch.robocurtain.plist
```

Unload when not unhappy.
```sh
launchctl unload ~/Library/LaunchAgents/com.hugohulsebosch.robocurtain.plist
```