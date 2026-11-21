; Inno Setup script for the yt-view-bot desktop launcher.
[Setup]
AppName=YT View Bot
AppVersion=0.6.3
DefaultDirName={autopf}\YTViewBot
DefaultGroupName=YT View Bot
OutputBaseFilename=yt-view-bot-setup
Compression=lzma2
SolidCompression=yes

[Files]
Source: "dist\yt-view-bot.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "config\*"; DestDir: "{app}\config"; Flags: recursesubdirs

[Icons]
Name: "{group}\YT View Bot"; Filename: "{app}\yt-view-bot.exe"