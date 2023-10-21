# Polly Gen

## 1. Text Export
```text
# View > "Show Presenter Notes"
# Images: Exports as images
# https://support.apple.com/lv-lv/guide/keynote/tand1a4ee7c/mac
# https://discussions.apple.com/thread/252961553
set outTxt to ""
tell front document of application "Keynote"
	repeat with aSlide in slides
		tell aSlide
			set slideNum to "Slide " & slide number
			set presNotes to presenter notes as text
			set outTxt to outTxt & slideNum & return & presNotes & return & return
		end tell
	end repeat
	tell application "TextEdit"
		make new document at front
		set text of front document to outTxt
	end tell
end tell
```

## 2. Run polly.py
```shell
$ python3 polly.py
```



