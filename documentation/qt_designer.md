``` cd /usr/lib/x86_64-linux-gnu/qt5/bin/ ``` 
``` ./designer ```
# Export Design to UI
* Click File > Save As > yourname.ui
* Then you can convert the ui code to a python file.
    * ```pyuic5 -o ui/main_window_ui.py ui/main_window.ui```
